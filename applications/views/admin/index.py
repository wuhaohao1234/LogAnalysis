from flask import Blueprint, redirect, url_for

from applications.common import render_template_mixin
from applications.extensions import admin_login_required

bp = Blueprint('index', __name__, url_prefix='/')


@bp.get('/')
@bp.get('/index')
@admin_login_required
def index():
    return redirect(url_for('admin.site.info'))
