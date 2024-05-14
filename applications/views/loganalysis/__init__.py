from flask import Flask, Blueprint

from .user import bp as user_bp
from .message import bp as message_bp
from .login_log import  bp as login_log_bp
from .passport import bp as passport_bp
from .index import bp as index_bp
from .task import bp as task_bp
from .about import bp as about_bp

log_analysis_bp = Blueprint('loganalysis', __name__, url_prefix='/loganalysis')


def register_webshell_bps(app: Flask) -> None:
    log_analysis_bp.register_blueprint(user_bp)
    log_analysis_bp.register_blueprint(message_bp)
    log_analysis_bp.register_blueprint(login_log_bp)
    log_analysis_bp.register_blueprint(passport_bp)
    log_analysis_bp.register_blueprint(index_bp)
    log_analysis_bp.register_blueprint(task_bp)
    log_analysis_bp.register_blueprint(about_bp)
    app.register_blueprint(log_analysis_bp)
