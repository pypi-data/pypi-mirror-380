import tutils.thpe as thpe
import tio.tfile as tf
import tlog.tlogging as tl

log = tl.log


def deploy_npm_yaml_antd_npmlink_handler(
    branch, version="10.1", module="rtc", npmlink=False
):
    rtcstudioRoot, rtcstudio, branch_item = thpe.lookupRtcStudioBranch(branch)  # type: ignore
    if branch_item:
        __branch = rtcstudio["versions"][f"rtc{version}"]
        yaml_ant_path = (
            __branch["yaml_ant_path"]
            if npmlink
            else __branch["yaml_ant_path"].replace("/cygdrive/c/", "c:/")
        )
        reactPath = __branch["yaml_ant_path"].replace("/cygdrive/c/", "c:/")
        moduleName = branch_item["name"]
        modulePath = f"{reactPath}{moduleName}"
        # ts.pipeline('cd ' + modulePath, 'npmlink' if npmlink else 'js')
        useJsCopy = "" if npmlink else "js"
        target = __branch[module]
        node_modules_target = f"{reactPath}{target}/node_modules/{moduleName}/es"
        tf.sync_folder(f"{modulePath}/es", node_modules_target)
