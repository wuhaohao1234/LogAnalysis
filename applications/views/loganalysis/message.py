from datetime import datetime

from flask import Blueprint, request
from flask_login import current_user, login_required
from sqlalchemy import func, and_, or_

from applications.common import render_template_mixin
from applications.common.utils.http import success_api, fail_api
from applications.extensions import user_login_required, db
from applications.models.base_model import to_table
from applications.models.message import Message

bp = Blueprint('user_bp', __name__, url_prefix='/message')


@bp.route('/send', methods=['GET'])
@login_required
def send():
    ...


def send_message(from_id, to_id, content):
    if not from_id or not to_id or not content:
        return fail_api(msg='参数错误')
    message = Message(from_id=from_id, to_id=to_id, content=content)
    db.session.add(message)
    db.session.commit()
    return success_api(msg='发送成功')


@bp.get('/mine')
@user_login_required
def get_min_msg():
    return render_template_mixin('loganalysis/mine_msg.html')


@bp.get('/new_count')
def new_message_count():
    message_count = db.session.query(func.count(Message.id)).filter(
        and_(Message.update_at.is_(None),
             or_(Message.from_id == current_user.id, Message.to_id == current_user.id))
    ).first()[0]
    if message_count > 0:
        return success_api(msg=str(message_count))

    return fail_api(msg='没有新消息')


@bp.get('/delete')
@login_required
def delete_message():
    message_id = request.args.get('id')
    message = Message.query.get(message_id)
    if message is None:
        return fail_api(msg='删除失败')
    message.delete_at = datetime.now()
    db.session.commit()
    return success_api('删除成功')


@bp.route('/list', methods=['GET'])
@user_login_required
def message_list():
    messages = Message.query.filter(
        and_(Message.delete_at.is_(None), or_(Message.from_id == current_user.id, Message.to_id == current_user.id))
    ).order_by(Message.create_at.desc()).all()
    rep_json = to_table(messages)
    for message in messages:
        if message.update_at is None:
            msg = Message.query.get(message.id)
            msg.update_at = datetime.now()
    db.session.commit()
    return rep_json

