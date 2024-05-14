from flask import Blueprint
from flask_login import current_user
from sqlalchemy import and_

from applications.common import render_template_mixin
from applications.extensions import user_login_required, db
from applications.models import LoginLog, User
from applications.models.base_model import to_table
from applications.models.vo.login_log_vo import LoginLogVo

bp = Blueprint('login_log', __name__, url_prefix='/log')


@bp.get('/mine')
@user_login_required
def mine_log():
    return render_template_mixin('loganalysis/mine_log.html')

@bp.route('/login_log', methods=['GET', 'POST'])
@user_login_required
def login_log():
    logs = db.session.query(LoginLog, User).filter(LoginLog.delete_at.is_(None)).join(
        User, LoginLog.uid == User.id).order_by(
        LoginLog.create_at.desc()).filter(LoginLog.uid == current_user.id)
    # logs = LoginLog.query.order_by(LoginLog.create_at.desc()).filter_by(uid=current_user.id)

    l_list = []
    for log, user in logs:
        log_vo = LoginLogVo(
            id=log.id,
            uid=log.uid,
            username=user.username,
            url=log.url,
            ip=log.ip,
            description=log.description,
            success=log.success,
            user_agent=log.user_agent,
            role=user.role,
            create_at=log.create_at
        )
        l_list.append(log_vo)
    return to_table(l_list)


@bp.get('/new_login_list')
def new_log_list():
    logs = db.session.query(LoginLog, User).join(
        User, LoginLog.uid == User.id).filter(
            and_(LoginLog.success, User.delete_at.is_(None), User.role != '管理员')
        ).order_by(LoginLog.create_at.desc()).limit(10).all()

    l_list = []
    for log, user in logs:
        log_vo = LoginLogVo(
            id=log.id,
            uid=log.uid,
            username=user.username,
            url=log.url,
            ip=log.ip,
            description=log.description,
            success=log.success,
            user_agent=log.user_agent,
            role=user.role,
            create_at=log.create_at
        )
        l_list.append(log_vo)
    return to_table(l_list)