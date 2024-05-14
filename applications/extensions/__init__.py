from flask import Flask

from .init_jinja2 import init_jinja2
from .init_sqlalchemy import db, ma, init_databases

from applications.extensions.init_login import init_login_manager
from applications.extensions.init_sqlalchemy import init_databases
from applications.extensions.init_session import init_session
from .init_user_login import user_login_required
from .init_admin_login import admin_login_required
from .init_error_views import init_error_views


def init_plugins(app: Flask) -> None:
    init_login_manager(app)
    init_databases(app)
    init_session(app)
    init_jinja2(app)
    init_error_views(app)

