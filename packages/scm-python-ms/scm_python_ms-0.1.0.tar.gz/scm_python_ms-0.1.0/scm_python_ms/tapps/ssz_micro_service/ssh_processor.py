import os
import tlog.tlogging as tl
import tio.tfile as tf
from tapps.ssz_micro_service.context_processor import *

log = tl.log


class SSHProcessor(ContextProcessor):
    def get_code_template_path(self):
        return "not support"

    def get_deploy_to_path(self):
        return os.path.join(self.deploy, "ssh")

    def sync(self):
        if "k8s.ssh.path" in self.context:
            tf.mkdir_if_absent(self.get_deploy_to_path())
            root = self.context["k8s.ssh.path"]
            for file in os.listdir(root):
                tf.copy(
                    os.path.join(root, file),
                    os.path.join(self.get_deploy_to_path(), file),
                    True,
                )
        else:
            log.warning("k8s.ssh.path not found in context")
