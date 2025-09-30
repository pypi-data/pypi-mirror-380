import os
import tlog.tlogging as tl
from tapps.ssz_micro_service.context_processor import *  # type: ignore

log = tl.log


class EtcProcessor(ContextProcessor):
    def get_code_template_path(self):
        return f"{self.workspace}/build/installation/deploy/app/etc"

    def get_deploy_to_path(self):
        return self.get_deploy_etc_path()
