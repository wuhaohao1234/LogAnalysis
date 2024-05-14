from flask import Blueprint, Flask

from .get_captcha import bp as captcha_bp
from .site_root import bp as site_root_bp
from .report import bp as report_bp
from .probe import  bp as probe_bp

common_bp = Blueprint('common', __name__, url_prefix='/')


def register_common_bps(app: Flask) -> None:
    common_bp.register_blueprint(captcha_bp)
    common_bp.register_blueprint(site_root_bp)
    common_bp.register_blueprint(report_bp)
    common_bp.register_blueprint(probe_bp)

    app.register_blueprint(common_bp)
