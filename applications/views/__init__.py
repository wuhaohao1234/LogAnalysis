from flask import Flask

from applications.views.common import register_common_bps
from applications.views.loganalysis import register_webshell_bps
from applications.views.admin import register_admin_bps


def init_bps(app: Flask) -> None:
    register_webshell_bps(app)
    register_admin_bps(app)
    register_common_bps(app)
