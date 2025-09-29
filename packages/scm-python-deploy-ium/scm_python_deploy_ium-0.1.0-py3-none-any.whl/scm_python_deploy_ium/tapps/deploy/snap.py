import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.tssh as tssh
import tutils.context_opt as tcontext
from . import mvn as deploy_mvn

log = tl.log


def deploy_snap_build_and_deploy_for_rtc_handler(
    version="10.1",
    git=False,
    module="rtc",
    backend=False,
    web=False,
    npmlink=False,
    nobuild=False,
):
    rtcRoot, reactstudio, branch_item = thpe.lookupRtcBranch(
        module, version, module if backend else "reactstudio"
    )
    if branch_item:
        module_home = rtcRoot  # branch_item['home']
        cmds = ["c:"]
        if npmlink:
            antdModules = ["action", "redux", "work", "antd"]
            for antdModule in antdModules:
                cmds.append(
                    f"{thpe.PREFIX_CALL}deploy npmlink -v {version} -m {module} -l -r {antdModule}"
                )
                cmds.append(thpe.EXIT_IF_ERROR)
        if web:
            web_folder = os.path.abspath(os.path.join(module_home, branch_item["web"]))
            cmds.append(f"cd {web_folder}")
            cmds.append(thpe.EXIT_IF_ERROR)
            cmds.append(f"{thpe.PREFIX_CALL}yarn build")
            cmds.append(thpe.EXIT_IF_ERROR)
        if not nobuild:
            deploy_mvn.__maven_pipeline(cmds, reactstudio, branch_item, module_home)  # type: ignore
        if git:
            deploy = branch_item["deploy"]
            for target in deploy["targets"]:
                to = target["to"]
                restart = target["restart"]
                for from_jar in deploy["from"]:
                    from_jar = os.path.abspath(os.path.join(module_home, from_jar))
                    cmds.append(f"scp {from_jar} {to}")
                    cmds.append(thpe.EXIT_IF_ERROR)
                if restart:
                    cmds.append(restart)
        ts.pipeline(*cmds)
    else:
        log.error(f"{module}{version} not found in yaml")
