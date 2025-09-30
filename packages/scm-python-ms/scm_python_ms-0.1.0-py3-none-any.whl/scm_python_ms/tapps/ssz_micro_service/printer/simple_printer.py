"""
git log -10 --name-only --pretty=%H
find what changed in the latest commit as list(module name)
"""

import platform, os, traceback
import tlog.tlogging as tl
import tio.tfile as tf

log = tl.log


class SimplePrinter:
    def __init__(
        self,
        version="1.1.0-SNAPSHOT",
        deploy="unkown",
        workspace="unkown",
        sourcecode="unkown",
        project="unkown",
    ):
        self.workspace = workspace
        self.version = version
        self.deploy = deploy
        self.app = f"{deploy}/app"
        self.sourcecode = sourcecode
        self.project = project
        self.is_windows = platform.platform().startswith("Win")
        log.debug("-------------simplePrinter-------__init__ " + project)

    @staticmethod
    def get_maven_projects(workspace):
        try:
            return [""] + tf.readlines(f"{workspace}/sourcecode/projects.txt")
        except Exception as e:
            log.info(f"{workspace}/sourcecode/projects.txt not found")
            return [""]

    @staticmethod
    def read_last_build_sha1(workspace):
        try:
            with open(f"{workspace}/lastsha1.txt", "r+") as fo:
                sha1 = fo.readline().strip()
            return sha1
        except Exception as e:
            log.warning(e)
        return "unknown"

    def get_last_build_sha1(self):
        return SimplePrinter.read_last_build_sha1(self.workspace)

    def print_code_project_path(self):
        log.info(f"[{self.sourcecode}/{self.project}]")

    def get_deploy_rpc_path(self):
        return f"{self.app}/{self.project}"

    def get_deploy_shell_path(self):
        return f"{self.app}/bin"

    def get_deploy_etc_path(self):
        return f"{self.app}/etc"

    def get_deploy_build_path(self):
        return f"{self.app}/build"

    def get_deploy_dump_path(self):
        return f"{self.app}/dump"

    def get_deploy_logs_path(self):
        return f"{self.app}/logs"

    def get_deploy_lib_path(self):
        return f"{self.app}/lib"

    def get_code_rpc_target_path(self):
        return f"{self.sourcecode}/{self.project}/target/"

    def get_code_rpc_lib_path(self):
        return f"{self.sourcecode}/{self.project}/target/lib/"

    def get_jar_file(self):
        return f"{self.project}-{self.version}.jar"

    def get_app_projects(self):
        return [
            os.path.basename(os.path.dirname(pom_file))
            for pom_file in tf.search_file_in_folder_to_match_text(
                self.workspace,
                "pom.xml",
                r"<rpcMainClass>.+</rpcMainClass>",
                exact_match_file_name=True,
            )
        ]

    def write_warning(self, fo):
        if self.is_windows:
            fo.write("@echo the file is genearted by script, do not modify it\n")
        else:
            fo.write("# the file is genearted by script, do not modify it\n")
