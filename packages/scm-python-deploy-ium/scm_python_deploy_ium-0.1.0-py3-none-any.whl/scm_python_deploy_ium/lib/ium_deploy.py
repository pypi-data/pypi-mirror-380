import tlog.tlogging as tl
import tapps.deploy.ium as deploy_ium
import tapps.deploy.snap as deploy_snap
import tapps.deploy.gwt as deploy_gwt
import tapps.deploy.mvn as deploy_mvn
import tapps.deploy.npm as deploy_npm
import tapps.deploy.war as deploy_war

from tio.tcli import *
from ping3 import ping

log = tl.log
# for each new plugin, please register cmd/sh in ${SCM_PYTHON_SH_HOME}/bin
# use for SUB_PLUGIN_NAME helper, for example xxxxx

# name= means that name follow string parameter
# mandatory is by func with default parameter
flags = [
    (
        "d",
        ["dry_run", "dry-run", "norun"],
        "dry run",
        ["install/opswar", "install/ciswar", "install/ium"],
    ),
    ("s", "source", "source:jar", "install", "install/mvn"),
    ("j", "jdk8", "use jdk8 to build", "install", "install/mvn"),
    ("b", "nobuild", "skip build", "install", "install/mvn", "install/rtc"),
    ("p:", "pom=", "-f pom.xml", "install", "install/mvn"),
    ("l", "npmlink", "use npmlink or js", "install/npmlink", "install/rtc"),
    ("v:", "version=", "version like 10.1", "install/npmlink", "install/rtc"),
    ("m:", "module=", "module name like rtc", "install/npmlink", "install/rtc"),
    ("w", "web", "build react web", "install/rtc"),
    ("k", "backend", "build total backend for dependency", "install/rtc"),
    (
        "t",
        "git",
        "back to git repo and deploy to cloud",
        "install/opswar",
        "install/ciswar",
        "install/plugins",
        "install/rtc",
    ),
    (
        "r:",
        "branch=",
        "branch 90_cpe, build which branch",
        [
            "install/ium",
            "install/opsclear",
            "install/opswar",
            "install/ciswar",
            "install/pushopswar",
            "install/pushciswar",
            "install/plugins",
            "install/patch",
        ],
    ),
    ("t:", "target=", "ant target[package.plugin]", "install/ium"),
    ("r:", "branch=", "sync which npm package like antd", "install/npmlink"),
    ("r:", "branch=", "which gwt branch to compile, [2.9.0,master]", "install/gwt"),
    ("r:", "branch=", "new branch name", "install/clone"),
    ("n:", "reponame=", "by git repo name", "install/clone"),
    (
        "u:",
        "user=",
        "user name in remote",
        ["install/pushopswar", "install/pushciswar"],
    ),
    (
        "n:",
        "host=",
        "hostname or ip",
        ["install/pushopswar", "install/pushciswar"],
    ),
]


opp = OptParser(flags)

"""
编译mvn项目
相关配置文件
sample.yaml:    sh/etc/build.install.sample.yaml
runtime.yaml:   ${hostname}/etc/build.install.runtime.yaml
"""


@cli_invoker("install/|mvn")  # build project use mvn
def mvn_install(pom=None, source=False, jdk8=False, nobuild=False):
    deploy_mvn.do_mvn_install(pom, source, jdk8, nobuild)


@cli_invoker(
    "install/ium"
)  # build project use ant for ium, current folder must be in siu or it's sub folder
def eium_ant_install(branch=None, target=None, dry_run=False):
    siu_root, eium, branch_item = deploy_ium.eium_lookup_branch(branch)
    deploy_ium.deploy_eium_do_ant_install(siu_root, eium, branch_item, target, dry_run)


@cli_invoker("install/opsclear")  # clear the unused class for ops console
def eium_ops_clear(branch=None):
    siu_root, eium, branch_item = deploy_ium.eium_lookup_branch(branch)
    if branch_item:
        deploy_ium.eium_clear_for_ops(siu_root, eium, branch_item)


@cli_invoker(
    "install/opswar"
)  # build war for ops console, current folder must be in siu or it's sub folder
def eium_ops_war(branch=None, git=False, dry_run=False):
    siu_root, eium, branch_item = deploy_ium.eium_lookup_branch(branch)
    if branch_item:
        deploy_war.eium_zip_eium_war(siu_root, eium, branch_item, git, "ops", dry_run)


@cli_invoker(
    "install/pushopswar"
)  # after build war for ops console, push war to remote server
def eium_push_ops_war(branch=None, host="eium-9801.shao.sh", user="snap"):
    siu_root, eium, branch_item = deploy_ium.eium_lookup_branch(branch)
    if branch_item:
        deploy_ium.eium_push_eium_war(siu_root, eium, branch_item, host, user, "ops")


@cli_invoker(
    "install/ciswar"
)  # build war for cis ui, current folder must be in siu or it's sub folder
def eium_cis_war(branch=None, git=False, dry_run=False):
    siu_root, eium, branch_item = deploy_ium.eium_lookup_branch(branch)
    if branch_item:
        deploy_war.eium_zip_eium_war(siu_root, eium, branch_item, git, "cis", dry_run)


@cli_invoker(
    "install/pushciswar"
)  # after build war for ops console, push war to remote server
def eium_push_cis_war(branch=None, host="eium-9801.shao.sh", user="snap"):
    siu_root, eium, branch_item = deploy_ium.eium_lookup_branch(branch)
    if branch_item:
        deploy_ium.eium_push_eium_war(siu_root, eium, branch_item, host, user, "cis")


@cli_invoker(
    "install/gwt"
)  # build gwt sdk, current folder don't care, read from install.runtime.yaml
def deploy_gwt_sdk_handler(branch):
    deploy_gwt.deploy_gwt_sdk_handler(branch)


@cli_invoker(
    "install/plugins"
)  # build ium plugins for ops cloud poc, current folder must be in siu or it's sub folder
def eium_build_plugins(branch=None, git=False):
    siu_root, eium, branch_item = deploy_ium.eium_lookup_branch(branch)
    if branch_item:
        deploy_ium.eium_do_build_plugins(siu_root, eium, branch_item, git)


@cli_invoker("install/only")  # just deploy file skip build
def disablerouter():
    deploy_mvn.do_mvn_install(nobuild=True)
    print("deprectated, use install --nobuild to replace it")


@cli_invoker("install/npmlink")  # sync yaml-antd* module to studio-web/node_modules
def deploy_npm_yaml_antd_npmlink_handler(
    branch, version="10.1", module="rtc", npmlink=False
):
    deploy_npm.deploy_npm_yaml_antd_npmlink_handler(branch, version, module, npmlink)


@cli_invoker(
    "install/rtp"
)  # build rtp studio and deploy, git=True means to deploy to colud
def build_and_deploy_for_rtp(version="90fp02"):
    deploy_mvn.do_maven_build(version, "rtp")


@cli_invoker(
    "install/rtc"
)  # build rtc studio and deploy, git=True means to deploy to colud
def deploy_snap_build_and_deploy_for_rtc_handler(
    version="10.1",
    git=False,
    module="rtc",
    backend=False,
    web=False,
    npmlink=False,
    nobuild=False,
):
    deploy_snap.deploy_snap_build_and_deploy_for_rtc_handler(
        version, git, module, backend, web, npmlink, nobuild
    )


@cli_invoker(
    "install/pushiumcli"
)  # from ~/.ium folder to parse B.xxx.yaml, and bundle ium cli xml file and load to nginx server
def deploy_push_ium_cli_xml_files_handler():
    deploy_ium.deploy_push_ium_cli_xml_files_handler()


@cli_invoker(
    "install/patch"
)  # patch to SIU installation, name=src, branch=91/92/103/104
def deploy_ium_patch_ium_handler(branch):
    deploy_ium.deploy_ium_patch_ium_handler(branch)


@cli_invoker("install/clone")  # git clone from exist repo, minium disk usage""
def deploy_ium_git_clone_handler(branch, repo_name="ium-dev"):
    deploy_ium.deploy_ium_git_clone_handler(branch, repo_name)
