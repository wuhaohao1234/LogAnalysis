from functools import wraps

from flask import request, current_app, redirect, url_for
from flask_login import current_user
from flask_login.config import EXEMPT_METHODS


def user_login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in EXEMPT_METHODS or current_app.config.get("LOGIN_DISABLED"):
            pass
        elif not current_user.is_authenticated or current_user.is_admin:
            return redirect(url_for(current_app.config.get("USER_LOGIN_VIEW")) + '?m')

        # flask 1.x compatibility
        # current_app.ensure_sync is only available in Flask >= 2.0
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view
