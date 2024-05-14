from flask import Blueprint, Flask

from .passport import bp as passport_bp
from .index import bp as index_bp
from .user import bp as user_bp
from .login_log import bp as login_log_bp
from .site import bp as site_bp
from .task import bp as tasks_bp
from .message import bp as message_bp

admin_bps = Blueprint('admin', __name__, url_prefix='/admin')


def register_admin_bps(app: Flask) -> None:
    admin_bps.register_blueprint(passport_bp)
    admin_bps.register_blueprint(index_bp)
    admin_bps.register_blueprint(user_bp)
    admin_bps.register_blueprint(login_log_bp)
    admin_bps.register_blueprint(site_bp)
    admin_bps.register_blueprint(tasks_bp)
    admin_bps.register_blueprint(message_bp)

    app.register_blueprint(admin_bps)
