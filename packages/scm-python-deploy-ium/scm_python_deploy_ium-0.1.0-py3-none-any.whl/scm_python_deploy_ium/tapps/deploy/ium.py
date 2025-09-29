import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.tssh as tssh
import tutils.context_opt as tcontext

log = tl.log


def deploy_eium_do_ant_install(
    siu_root: str, eium: dict, branch_item: dict, target: str, dru_run=False
):
    cmds = thpe.eium_start_ant_task(siu_root, eium, branch_item)
    thpe.eium_disable_antivirus(cmds)
    current_folder = os.path.abspath(".")
    if current_folder == os.path.abspath(os.path.join(siu_root, "siu")):
        # the clean.all target is not required in rebuild.all
        if not target:
            cmds.append(f"{thpe.PREFIX_CALL}iumant clean.all")
    else:
        cmds.append(thpe.EIUM_CLEAN_BUILD)
    if target:
        log.info(
            f"custom ant target is {target}, search target alias mapping or invoke it directly"
        )
        target_mapping = tcontext.merge_design_runtime(
            eium, branch_item, "ant/targetAlias"
        )
        ant_runtime_target_cmd = (
            target_mapping[target] if target in target_mapping else "ant " + target
        )
        cmds.append(f"{thpe.PREFIX_CALL}{ant_runtime_target_cmd}")
    else:
        ant_runtime_target_cmd = tcontext.merge_design_runtime(
            eium, branch_item, "buildCmd"
        )
        cmds.append(f"{thpe.PREFIX_CALL}{ant_runtime_target_cmd}")
    thpe.override_file_after_build(siu_root, eium, branch_item, cmds)
    if dru_run:
        for cmd in cmds:
            print(cmd)
    else:
        ts.pipeline(*cmds)


def deploy_push_ium_cli_xml_files_handler():
    user_home_dir = os.path.expanduser("~")
    for ium_dir in ["ium_cli_xml", "ium_chints"]:
        ium_meta_dir = os.path.join(user_home_dir, ".ium", ium_dir)
        for ium_cli_xml_file in tf.listdir(ium_meta_dir):
            abs_file = os.path.join(ium_meta_dir, ium_cli_xml_file)
            os.path.isfile(abs_file) and ium_cli_xml_file.startswith(
                "B."
            ) and os.path.splitext(ium_cli_xml_file)[
                1
            ] == ".yaml" and deploy_zip_and_push_ium_cli_xml_file(
                ium_meta_dir, ium_cli_xml_file
            )
        hosts = [
            "root@10.43.173.10:/app/backup/work-tools/eium/cli",
            "root@192.168.50.246:/app/backup/work-tools/eium/cli",
        ]
        tssh.init_vilink_handler(hosts, 22, ium_meta_dir, ".tar")


def deploy_ium_patch_ium_handler(branch):
    java_cmd = "java"
    latest_patch = "D:\\snap_share\\eIUM9.0FP02\\eIUM90FP02Patch.SNAPSHOT-latest.patch"
    patch_args = "-A NonActivatedInstall=true"
    siu_target = "C:\\SIU_92"
    cmds = []
    if branch.startswith("92"):
        cmds.append(
            java_cmd + " -jar " + latest_patch + " " + siu_target + " " + patch_args
        )
    ts.pipeline(*cmds)


def deploy_ium_git_clone_handler(branch, repo_name="ium-dev"):
    current_folder = os.path.abspath(".")
    repo_folder = os.path.join(current_folder, repo_name)
    if not os.path.exists(repo_folder):
        log.error(f"{repo_folder} not exists, please correct the repo name")
        return
    branch_folder = os.path.join(current_folder, branch)
    if os.path.exists(branch_folder):
        log.error(
            f"{branch_folder} is exists, please input an new branch name that you want to checkout"
        )
        return
    tf.mkdir_if_absent(f"{branch_folder}/.git/logs")
    tf.copy(f"{repo_folder}/.git/HEAD", f"{branch_folder}/.git")
    cmds = []
    for folder in [
        "hooks",
        "info",
        "objects",
        "refs",
        "logs/refs",
        "config",
        "packed-refs",
    ]:
        branch_git_folder = os.path.abspath(f"{branch_folder}/.git/{folder}")
        repo_git_folder = os.path.abspath(f"{repo_folder}/.git/{folder}")
        # tf.removeIfPresent(branch_git_folder)
        window_link = "mklink" if os.path.isfile(repo_git_folder) else "mklink /D /J"
        cmds.append(
            f"ln -s {repo_git_folder} {branch_git_folder}"
            if thpe.is_linux
            else f"{window_link} {branch_git_folder} {repo_git_folder}"
        )
    # for file in [ 'config', 'packed-refs' ]:
    cmds.append(f"cd {branch_folder}")
    cmds.append(f"git checkout -f {branch}")
    ts.pipeline(*cmds)


def deploy_zip_and_push_ium_cli_xml_file(ium_meta_dir: str, ium_cli_xml_file: str):
    log.info(f"zip and push from meta {ium_cli_xml_file}")
    abs_xml_file = os.path.join(ium_meta_dir, ium_cli_xml_file)
    base_name, ext_name = os.path.splitext(ium_cli_xml_file)
    work_dir = os.path.join(ium_meta_dir, base_name)
    tf.mkdir_if_absent(work_dir)
    for xml_file in tf.yaml_load(abs_xml_file):
        tf.copy(xml_file, work_dir)
        xml_file.endswith(".chints") and tf.copy(f"{xml_file[0:-7]}.java", work_dir)
    tf.tar(work_dir, os.path.join(ium_meta_dir, base_name))


def eium_lookup_branch(branch):
    if not branch:
        build_context = thpe.eium_find_branch_build_context()
        branch = build_context[thpe.EIUM_VERSION]
    return thpe.lookup_branch_by_type(branch, "install/products/eium", "siu")


def eium_push_eium_war(siu_root, eium, branch_item, host, user, web_cfg_name="ops"):
    war_module = tcontext.merge_design_runtime(
        eium, branch_item, f"{web_cfg_name}/warModule"
    )
    war_module_folder = (
        war_module["folder"] if war_module and "folder" in war_module else "web-console"
    )
    war_module_output = (
        war_module["output"]
        if war_module and "output" in war_module
        else f"{war_module_folder}.war"
    )
    web_root = os.path.join(siu_root, "siu", "apps", "web")
    war_file = os.path.join(web_root, war_module_folder, "build", war_module_output)
    print(web_cfg_name, war_module_folder, war_file)
    remote = f"root@{host}:/opt/SIU_{user}/newconfig/web"
    passwd = None
    port = 22
    recursive = False
    log.info(f"host is {host}, user is {user}")
    tssh.put(remote, passwd, war_file, port, recursive)


def eium_do_build_plugins(siu_root, eium, branch_item, git):
    plugins = tcontext.merge_design_runtime(eium, branch_item, "plugins")
    cmds = thpe.eium_start_ant_task(siu_root, eium, branch_item)
    plugin_root = os.path.join(siu_root, "siu", "plugins")
    for plugin in plugins:
        cmds.append("cd " + os.path.join(plugin_root, plugin))
        cmds.append(thpe.EXIT_IF_ERROR)
        cmds.append(thpe.EIUM_DEFAULT_BUILD_CMD)
        cmds.append(thpe.EXIT_IF_ERROR)
    if git:
        plugin_deploy_info = tcontext.merge_design_runtime(
            eium, branch_item, "pluginDeploy"
        )
        plugin_suffix = plugin_deploy_info["pluginSuffix"]
        cmds = []
        plugin_deploy_info_targets = []
        for plugin in plugins:
            plugin_build = os.path.join(plugin_root, plugin, "build")
            plugin_deploy_info_targets.append(plugin + plugin_suffix)
            target_path = (
                plugin_deploy_info["localPath"] + "\\" + plugin + plugin_suffix
            )
            tf.mkdir_if_absent(target_path)
            cmds.append("copy /Y " + plugin_build + "\\*.jar " + target_path)
        cmds.append("cd " + plugin_deploy_info["localPath"])
        cmds.append(thpe.EXIT_IF_ERROR)
        cmds.append("D:")
        cmds.append(
            plugin_deploy_info["deployCmd"] + " " + " ".join(plugin_deploy_info_targets)
        )
        cmds.append(thpe.EXIT_IF_ERROR)
    thpe.override_file_after_build(siu_root, eium, branch_item, cmds)
    ts.pipeline(*cmds)


def eium_clear_for_ops(siu_root, eium, branch_item):
    rm_cmd = "rm -f" if thpe.is_linux else "del"
    ts.call(
        f"{rm_cmd} "
        + os.path.join(siu_root, "siu", "apps", "web", "web-core", "src", "*.class")
        + " /s"
    )
    ts.call(
        f"{rm_cmd} "
        + os.path.join(
            siu_root, "siu", "siupkg", "core_classes", "org", "slf4j", "impl", "*.class"
        )
    )
    # don't del the rdm.jar or Can't find bundle for base name com.hp.usage.web.rdm.client.i18n.validationmsgs, locale en_US
    # it is mandatory to remove rdm.jar in 90_cpe or the nullexception will be thrown
    if branch_item["name"] == "9.0":
        excludings = tcontext.merge_design_runtime(eium, branch_item, "ops/excludings")
        web_app_modules = thpe.eium_get_web_app_modules(siu_root, excludings)
        for web_module in ["web-core", "web-console"]:
            web_app_modules.remove(web_module)
        for web_module in web_app_modules:
            ts.call(
                f"{rm_cmd} "
                + os.path.join(
                    siu_root,
                    "siu",
                    "apps",
                    "web",
                    "web-console",
                    "build",
                    "docroot",
                    "WEB-INF",
                    "lib",
                    f"{web_module}.jar",
                )
            )
