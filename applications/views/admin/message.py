from flask import Blueprint

from applications.common import render_template_mixin
from applications.extensions import admin_login_required
from applications.models.base_model import to_table
from applications.models.message import Message

bp = Blueprint('message', __name__, url_prefix='/message')


@bp.get('/')
@admin_login_required
def message_manage():
    return render_template_mixin('admin/message_manage.html')


@bp.get('/list')
@admin_login_required
def message_list():
    messages = Message.query.filter(Message.delete_at.is_(None)).all()
    return to_table(messages)
