import os
import json
import abc, traceback
import tlog.tlogging as tl
import tio.tfile as tf
import tutils.context_opt as tcontext
from .printer.simple_printer import *

log = tl.log


class ContextProcessor(SimplePrinter, metaclass=abc.ABCMeta):
    def __init__(
        self,
        version: str,
        deploy: str,
        workspace: str,
        sourcecode: str,
        context: dict,
    ):
        log.info("init ContextProcessor from constructor ")
        self.context = tcontext.flatten_dict(context)
        SimplePrinter.__init__(self, version, deploy, workspace, sourcecode, "unknown")
        self.init_context_variables()
        log.debug(self.context)

    def init_context_variables(self):
        self.context["context.workspace"] = self.workspace
        self.context["context.version"] = self.version
        self.context["context.deploy"] = self.deploy
        self.context["context.deploy.app"] = self.app
        self.context["context.deploy.app.bin"] = self.get_deploy_shell_path()
        self.context["context.deploy.app.etc"] = self.get_deploy_etc_path()
        self.context["context.deploy.app.dump"] = self.get_deploy_dump_path()
        self.context["context.deploy.app.logs"] = self.get_deploy_logs_path()

    def is_binary_file(self, path):
        return path.endswith(".jks") or path.endswith(".zip")

    def sync_file(self, file: str, template_path: str, deploy_path: str):
        template_file = (
            f"{template_path}/{file}" if os.path.isdir(template_path) else template_path
        )
        log.info(f"sync[{template_file}]")
        # if it is binary file, only copy it
        if self.is_binary_file(template_file):
            log.info(f"{template_file} is binary, copy it to target path")
            tf.copy(template_file, f"{deploy_path}/{file}")
            return
        with open(template_file, "r+", encoding="utf-8") as foread:
            deploy_file = os.path.join(deploy_path, file)
            with open(deploy_file, "w", encoding="utf-8") as fowrite:
                for line in foread.readlines():
                    fowrite.write(
                        tcontext.replace_by_context(context=self.context, line=line)
                    )

    @abc.abstractmethod
    def get_code_template_path(self) -> str:
        pass

    @abc.abstractmethod
    def get_deploy_to_path(self) -> str:
        pass

    def sync(self):
        template_path = self.get_code_template_path()
        deploy_path = self.get_deploy_to_path()
        tl.mkdir_if_absent(deploy_path)
        for file in os.listdir(template_path):
            try:
                self.sync_file(file, template_path, deploy_path)
            except Exception as e:
                log.error(e)
                log.error(traceback.format_exc())


def main():
    pass


if __name__ == "__main__":
    main()
