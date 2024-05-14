from flask import Blueprint, current_app, url_for, redirect, session
from flask_login import current_user

bp = Blueprint('site_root', __name__, url_prefix='/')


@bp.route('/', methods=['get', 'post'])
def site_root():
    if current_user is not None and current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for(current_app.config.get("ADMIN_ROOT_VIEW")))
    return redirect(url_for(current_app.config.get("SITE_ROOT_VIEW")))
