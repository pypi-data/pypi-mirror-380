import os
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
from .printer.simple_printer import SimplePrinter
import tutils.context_opt as tcontext
import tutils.ttemplate as ttemplate
import tutils.thpe as thpe
from datetime import datetime, timezone, timedelta

log = tl.log


class ShellProcessor(SimplePrinter):
    def __init__(self, dc: SimplePrinter, project: str):
        SimplePrinter.__init__(
            self, dc.version, dc.deploy, dc.workspace, dc.sourcecode, project
        )

    def get_code_template_path(self):
        return f"{self.workspace}/build/installation/deploy/app/bin"

    def write_sh(self, process_template_dict: dict):
        log.info(f"sh_path={self.get_deploy_shell_path()},self.project={self.project}")
        cloned_context = {"PROJECT_NAME": self.project, "WORKSPACE": self.workspace}
        ttemplate.handle_template_for_common_scripts(
            self.get_deploy_shell_path(),
            process_template_dict,
            cloned_context,
            comments="",
            allow_escape_char=True,
        )

    def sync(self, process_template_dict: dict):
        try:
            self.write_sh(process_template_dict)
        except Exception as e:
            log.error(e)


class LibProcessor(SimplePrinter):
    def __init__(self, dc: SimplePrinter, project):
        self.jar_container = dc.jar_container
        SimplePrinter.__init__(
            self, dc.version, dc.deploy, dc.workspace, dc.sourcecode, project
        )

    def unique_jar_in_lib(self):
        jar_container = self.jar_container
        rpcLibPath = self.get_code_rpc_lib_path()
        for file in os.listdir(rpcLibPath):
            if file not in jar_container:
                jar_container[file] = rpcLibPath
            else:
                oldFile = jar_container[file] + "/" + file
                newFile = rpcLibPath + "/" + file
                if os.stat(newFile).st_ctime > os.stat(oldFile).st_ctime:
                    jar_container[file] = rpcLibPath

    def sync(self, force=False):
        log.info(f"syncApp[{self.project} [{force}]]")
        rpc_path = self.get_deploy_rpc_path()
        tf.remove_dirs(rpc_path)
        tf.mkdir_if_absent(rpc_path)
        rpc_jar = self.get_jar_file()
        rpc_jar_path = os.path.join(rpc_path, rpc_jar)
        if not os.path.exists(rpc_jar_path):
            force = True
        else:
            force = not tf.sha1(self.get_code_rpc_target_path() + rpc_jar) == tf.sha1(
                rpc_jar_path
            )
        if force:
            tf.remove_if_present(rpc_jar_path)
            tf.copy(self.get_code_rpc_target_path() + rpc_jar, rpc_path)


class AppProcessor(SimplePrinter):
    jar_container = {}

    def sync_jar_to_lib(self, force=False):
        lib = self.get_deploy_lib_path()
        log.info(f"syncJarToLib [{lib}]")
        removes = []
        exists = []
        jar_container = self.jar_container
        tf.mkdir_if_absent(lib)
        for file in os.listdir(lib):
            if file not in jar_container:
                removes.append(file)
            else:
                exists.append(file)
        for file in jar_container.keys():
            if file not in exists:
                tf.copy(os.path.join(jar_container[file], file), lib)
            else:
                if not tf.sha1(os.path.join(jar_container[file], file)) == tf.sha1(
                    os.path.join(lib, file)
                ):
                    tf.remove_if_present(os.path.join(lib, file))
                    tf.copy(os.path.join(jar_container[file], file), lib)
        for file in removes:
            absolute_file = os.path.join(lib, file)
            if os.path.isfile(absolute_file):
                tf.remove_if_present(absolute_file)
            else:
                tf.remove_dirs(absolute_file)

    def sync(self, force=False, both=False):
        ms_template = thpe.load_yaml_file_with_variable(
            f"{self.workspace}/build/installation/deploy/app/template/micro-service.template.sample.yaml"
        )
        ms_shell_process_template_dict = tcontext.load_item_support_dot(
            ms_template, f"ms.shell.process"
        )
        for project in self.get_app_projects():
            try:
                sp = ShellProcessor(self, project)
                # 每个project都相同
                shell_from = sp.get_code_template_path()
                shell_path = sp.get_deploy_shell_path()
                sp.sync(ms_shell_process_template_dict)
                pp = LibProcessor(self, project)
                pp.print_code_project_path()
                pp.unique_jar_in_lib()
                pp.sync(force)
                log.info(f"shell{pp.get_deploy_shell_path()}")
            except Exception as e:
                log.error(e)
        self.sync_shell(ms_template, shell_from, shell_path)
        self.sync_jar_to_lib(force)
        self.sync_other_folder(
            tcontext.load_item_support_dot(ms_template, f"ms.runtime.folders")
        )
        self.sync_scm_yaml_handler()

    def sync_shell(self, ms_template: dict, shell_from: str, shell_path: str):
        self.sync_shell_bootstrap(ms_template)
        for file in os.listdir(shell_from):
            file = os.path.join(shell_from, file)
            if os.path.isfile(file):
                tf.copy(file, shell_path)

    def sync_other_folder(self, runtime_paths: list[str]):
        for path in runtime_paths:
            operated_path = os.path.join(self.app, path)
            tf.remove_dirs(operated_path)
            tf.mkdir_if_absent(operated_path)

    def sync_shell_bootstrap(self, ms_template: dict):
        cloned_context = {"VERSION": self.version, "WORKSPACE": self.workspace}
        ttemplate.handle_template_for_common_scripts(
            self.get_deploy_shell_path(),
            tcontext.load_item_support_dot(ms_template, f"ms.shell.bootstrap"),
            cloned_context,
            comments="",
            allow_escape_char=True,
        )

    def sync_scm_yaml_handler(self):
        scm_yaml_file = os.path.join(self.workspace, "build", "scm.yaml")
        # 设置东八区
        tz = timezone(timedelta(hours=8))
        # 当前时间
        now = datetime.now(tz)
        # 格式化输出
        formatted = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + now.strftime("%z")
        cloned_context = {
            "maven:project.version": self.version,
            "BUILD_TIME": formatted,
            "WORKSPACE": self.workspace,
        }
        tcontext.write_to_file_with_replace(
            target_file=os.path.join(self.get_deploy_build_path(), "scm.yaml"),
            lines=tf.readlines(scm_yaml_file, allowEmpty=True, allowStrip=False),
            context=cloned_context,
            auto_crlf=False,
            allow_escape_char=True,
        )
        scm_yaml_index = 1
        current_folder = os.path.abspath(".")
        for file_name in ts.call_cmd(f'git show --pretty="" --name-only'):
            file_name = file_name.rstrip()
            abs_file_name = os.path.join(current_folder, file_name)
            if "scm/scm.yaml" in file_name:
                tcontext.write_to_file_with_replace(
                    target_file=os.path.join(
                        self.get_deploy_build_path(), f"{scm_yaml_index}.scm.yaml"
                    ),
                    lines=tf.readlines(
                        abs_file_name, allowEmpty=True, allowStrip=False
                    ),
                    context=cloned_context,
                    auto_crlf=False,
                    allow_escape_char=True,
                )
                scm_yaml_index += 1


def main():
    pass


if __name__ == "__main__":
    main()
