from flask import Flask, current_app
from flask_login import LoginManager


def init_login_manager(app: Flask) -> None:
    login_manager = LoginManager()
    login_manager.init_app(app)
    with app.app_context():
        login_view = current_app.config.get('ADMIN_LOGIN_VIEW')
    login_manager.login_view = login_view

    @login_manager.user_loader
    def load_user(user_id):
        from applications.models import User
        user = User.query.get(int(user_id))
        if user.role == '管理员':
            user.is_admin = True
        return user
