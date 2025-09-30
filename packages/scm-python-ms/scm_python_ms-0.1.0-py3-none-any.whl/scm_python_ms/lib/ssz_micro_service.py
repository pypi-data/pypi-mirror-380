"""
git log -10 --name-only --pretty=%H
find what changed in the latest commit as list(module name)
"""

import os, sys
import tlog.tlogging as tl
import tio.tfile as tf

from tio.tcli import *
from tapps.ssz_micro_service.jar_processor import AppProcessor
from tapps.ssz_micro_service.etc_processor import EtcProcessor
from tapps.ssz_micro_service.ssh_processor import SSHProcessor
import tapps.code.maven as code_maven
from typing import Union

# 判断当前 Python 版本
if sys.version_info >= (3, 10):
    # Python 3.10 及以上版本使用 | 符号
    ContextDateType = dict | bool
else:
    # Python 3.9 及以下版本使用 Union
    ContextDateType = Union[dict, bool]


log = tl.log
flags = [
    (
        "w:",
        "workspace=",
        "workspace root path of git project",
        ["syncapp"],
    ),
    ("d:", "deploy=", "the deploy root path", ["syncapp"]),
    ("r", "force", "force update all", ["syncapp"]),
    ("c:", "context=", "the json file of variables", ["syncapp"]),
]

opp = OptParser(flags)


@cli_invoker(
    "syncapp"
)  # genate the app from new or update the change from app projects/target
def sync_app(deploy: str, workspace="", force=False, context=False):
    context, deploy, workspace, sourcecode, version = parameters(
        deploy, workspace, context
    )
    both = True

    appProcessor = AppProcessor(version, deploy, workspace, sourcecode)
    appProcessor.sync(force, both)
    if context:
        log.info(f"start etc and ssh handler with deploy:{deploy} context:{context}")
        ep = EtcProcessor(
            version=version,
            deploy=deploy,
            workspace=workspace,
            sourcecode=sourcecode,
            context=context,
        )
        ep.sync()
        sp = SSHProcessor(
            version=version,
            deploy=deploy,
            workspace=workspace,
            sourcecode=sourcecode,
            context=context,
        )
        sp.sync()


def parameters(deploy: str, workspace: str, context: ContextDateType):
    context = opp.data if opp.data else context
    deploy = os.path.abspath(deploy)
    workspace = os.path.abspath(workspace)
    sourcecode = f"{workspace}/sourcecode"
    version = code_maven.code_maven_get_version_handler(
        workspace=workspace, clear_snapshot=False
    )
    return context, deploy, workspace, sourcecode, version


def main():
    pass


if __name__ == "__main__":
    main()
