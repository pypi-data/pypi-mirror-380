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
BUILD_CMD = "buildCmd"


def deploy_gwt_sdk_handler(branch):
    eium, branch_item = thpe.lookup_branch_by_type(branch, "install/products/gwt")
    if branch_item:
        sdk_build_gwt(eium, branch_item)


def sdk_build_gwt(gwt, branch_item):
    build_cmd = (
        branch_item[BUILD_CMD]
        if BUILD_CMD in branch_item
        else tcontext.load_item(gwt, BUILD_CMD)
    )
    GWT_TOOLS = "gwt-tools"
    JDK8 = "jdk8"
    version = branch_item["version"]
    src = branch_item["src"]
    cmds = []
    tf.ensure_change_dir(cmds, src)
    build_context = thpe.eium_init_build_context(tcontext.load_item(gwt, JDK8))
    thpe.eium_start_java_task(cmds, build_context)
    cmds.append(
        build_cmd
        + " -Dgwt.tools="  # type: ignore
        + tcontext.load_item(gwt, GWT_TOOLS)
        + " -Dgwt.version="
        + version
    )
    ts.pipeline(*cmds)
