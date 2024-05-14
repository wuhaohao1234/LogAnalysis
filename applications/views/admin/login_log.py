from flask import Blueprint

from applications.common import render_template_mixin
from applications.extensions import admin_login_required, db
from applications.models import LoginLog, User
from applications.models.base_model import to_table
from applications.models.vo.login_log_vo import LoginLogVo

bp = Blueprint('login_log', __name__, url_prefix='/log')



@bp.get('/')
@admin_login_required
def login_log():
    return render_template_mixin('admin/log_manage.html')


@bp.get('/list')
@admin_login_required
def log_list():
    logs = db.session.query(LoginLog, User).filter(
        LoginLog.delete_at.is_(None)).join(
        User, LoginLog.uid == User.id).order_by(
        LoginLog.create_at.desc()).all()
    # logs = LoginLog.query.logic_all_json(LogOutSchema)

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
