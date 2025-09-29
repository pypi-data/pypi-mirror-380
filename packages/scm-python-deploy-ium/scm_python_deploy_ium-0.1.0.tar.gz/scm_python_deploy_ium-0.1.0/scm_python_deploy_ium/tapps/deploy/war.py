import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext

log = tl.log


def eium_zip_eium_war(
    siu_root, eium, branch_item, git, web_cfg_name="ops", dry_run=False
):
    excludings = tcontext.merge_design_runtime(
        eium, branch_item, f"{web_cfg_name}/excludings"
    )
    web_app_modules = thpe.eium_get_web_app_modules(siu_root, excludings)
    # eium_clear_for_ops(siu_root, eium, branch_item)
    cmds = thpe.eium_start_ant_task(siu_root, eium, branch_item)
    thpe.eium_disable_antivirus(cmds)
    depend_plugins = tcontext.merge_design_runtime(
        eium, branch_item, f"{web_cfg_name}/dependPlugins"
    )
    war_module = tcontext.merge_design_runtime(
        eium, branch_item, f"{web_cfg_name}/warModule"
    )
    war_module_folder: str = (
        war_module["folder"] if war_module and "folder" in war_module else "web-console"
    )
    war_module_output: str = (
        war_module["output"]
        if war_module and "output" in war_module
        else f"{war_module_folder}.war"
    )
    if depend_plugins:
        for plugin in depend_plugins:
            plugin_folder = os.path.join(siu_root, "siu", "plugins", plugin)
            cmds.append("cd " + plugin_folder)
            if os.path.exists(os.path.join(plugin_folder, "build")):
                cmds.append(thpe.EIUM_CLEAN_BUILD)
            cmds.append(thpe.EIUM_DEFAULT_BUILD_CMD)
    web_root = os.path.join(siu_root, "siu", "apps", "web")
    cmds.append("rm -f " + os.path.join(web_root, "*.class" + " /s"))
    # put war modeule folder on the end in list
    web_app_modules.remove(war_module_folder)
    web_app_modules.append(war_module_folder)
    for web_module in web_app_modules:
        web_module_folder = os.path.join(web_root, web_module)
        cmds.append("cd " + web_module_folder)
        cmds.append(thpe.EXIT_IF_ERROR)
        if os.path.exists(os.path.join(web_module_folder, "build")):
            cmds.append(thpe.EIUM_CLEAN_BUILD)
        cmds.append(
            thpe.EIUM_DEFAULT_BUILD_CMD
            if web_module != war_module_folder
            else thpe.EIUM_DEFAULT_WAR_BUILD_CMD
        )
        cmds.append(thpe.EXIT_IF_ERROR)
    if git:
        war_deploy_url = tcontext.merge_design_runtime(
            eium, branch_item, f"{web_cfg_name}/war_deploy_url"
        )
        tf.copy(
            web_root + f"/{war_module_folder}/build/*.war", war_deploy_url["localPath"]
        )
        cmds = ["cd " + war_deploy_url["localPath"]]
        cmds.append(thpe.EXIT_IF_ERROR)
        cmds.append("D:")
        cmds.append(war_deploy_url["deployCmd"])
        cmds.append(thpe.EXIT_IF_ERROR)
    thpe.override_file_after_build(siu_root, eium, branch_item, cmds)
    if dry_run:
        for cmd in cmds:
            print(cmd)
    else:
        ts.pipeline(*cmds)
