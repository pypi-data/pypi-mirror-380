import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext

log = tl.log


def do_mvn_install(pom=None, source=False, jdk8=False, nobuild=False):
    build_mapping = thpe.load_install_yaml("build")
    current_path = os.path.abspath(".")
    buildCmd = tcontext.load_item(build_mapping, "install/buildCmd")
    prefixCmd = tcontext.load_item(build_mapping, "install/prefixCmd")
    excludeJars = tcontext.load_item(build_mapping, "install/excludeJars")
    for project in tcontext.load_item(build_mapping, "install/projects"):
        workspace = project["workspace"]
        if current_path.startswith(workspace):
            buildCmd = project["buildCmd"] if "buildCmd" in project else buildCmd
            buildCmd = (buildCmd + " source:jar") if source else buildCmd
            buildCmd = (buildCmd + " -f " + pom) if pom else buildCmd
            prefixCmd = project["prefixCmd"] if "prefixCmd" in project else prefixCmd
            _jdk8 = project["jdk8"] if "jdk8" in project else None
            if not nobuild:
                if (not jdk8) and _jdk8 and current_path not in _jdk8:
                    ts.pipeline(prefixCmd, buildCmd)
                else:
                    ts.raw(buildCmd)
            deploy = project["deploy"] if "deploy" in project else None
            if deploy:
                excludeJars = (
                    project["excludeJars"] if "excludeJars" in project else excludeJars
                )
                jar = _findDeployJar(current_path, excludeJars)
                deploys = deploy if isinstance(deploy, list) else [deploy]
                if jar:
                    for dl in deploys:
                        if "@" in dl:
                            ts.raw("scp " + jar + " " + dl)
                        else:
                            tf.copy(jar, dl)
                else:
                    log.info("have no the match jar, skip deploy to " + str(deploy))


def _findDeployJar(path: str, excludeJars: list[str]):
    if not os.path.exists(path + "/target"):
        return None
    for jar in os.listdir(path + "/target"):
        if (jar.endswith(".jar") or jar.endswith(".war")) and not jar in [
            jar for line in excludeJars if jar.endswith(line)
        ]:
            return path + "/target/" + jar
    return None


def __maven_pipeline(
    cmds: list[str], product_item, branch_item, module_home, pom_files=None
):
    build_context = {}
    build_context[thpe.EIUM_JDK_ROOT] = os.path.abspath(
        tcontext.merge_design_runtime(product_item, branch_item, thpe.EIUM_JDK_ROOT)
    )
    # because hardcode mvn in rtc code, so m3_home is mandatory
    m3_home = os.path.abspath(
        tcontext.merge_design_runtime(product_item, branch_item, thpe.EIUM_MAVEN_ROOT)
    )
    build_context[thpe.EIUM_MAVEN_ROOT] = m3_home
    m3_bin_cmd = os.path.join(m3_home, "bin", "mvn")
    m3_setting_xml = os.path.abspath(
        tcontext.merge_design_runtime(
            product_item, branch_item, thpe.EIUM_MAVEN_SETTINGS
        )
    )
    log.info(f"new m3 setting xml is {m3_setting_xml}")
    old_m3_setting_xml = os.path.join(m3_home, "conf", "settings.xml")
    backup_m3_setting_xml = None
    if m3_setting_xml and not m3_setting_xml == old_m3_setting_xml:
        backup_m3_setting_xml = tf.backup(old_m3_setting_xml)
        tf.copy(m3_setting_xml, old_m3_setting_xml)
    thpe.eium_start_java_task(cmds, build_context, product_item, branch_item)
    # change mvnCmd as mvn parameters
    mvnCmd = tcontext.merge_design_runtime(product_item, branch_item, "mvnCmd")
    mvnCmd = f"{m3_bin_cmd} {mvnCmd}"
    if "prefixCmd" in product_item:
        cmds.append(product_item["prefixCmd"])
    if not pom_files:
        pom_files = branch_item["mavens"]
    for maven in pom_files:
        pom_file = (
            os.path.abspath(os.path.join(module_home, maven))
            if maven.endswith(".xml")
            else os.path.abspath(os.path.join(module_home, maven, "pom.xml"))
        )
        thpe.exec_with_failure_exit(
            cmds,
            (
                f"{thpe.PREFIX_CALL}{maven}"
                if maven.startswith("mvn")
                else f"{thpe.PREFIX_CALL}{mvnCmd} -f {pom_file}"
            ),
        )
    return old_m3_setting_xml, backup_m3_setting_xml


def do_maven_build(version: str, module: str):
    rtcRoot, product_item, branch_item = thpe.lookupRtcBranch("", version, module)
    cmds: list[str] = []
    old_m3_setting_xml, backup_m3_setting_xml = __maven_pipeline(
        cmds, product_item, branch_item, rtcRoot
    )
    ts.pipeline(*cmds)
    if old_m3_setting_xml and backup_m3_setting_xml:
        log.info(f"restore {backup_m3_setting_xml} to {old_m3_setting_xml}")
        tf.copy(backup_m3_setting_xml, old_m3_setting_xml)
        tf.remove_if_present(backup_m3_setting_xml)
