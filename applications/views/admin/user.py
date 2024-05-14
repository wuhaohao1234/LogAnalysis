from datetime import datetime

from flask import Blueprint, request
from flask_login import login_required, current_user
from sqlalchemy import and_

from applications.common import render_template_mixin
from applications.common.utils.http import fail_api, success_api
from applications.extensions import admin_login_required, db
from applications.models import User
from applications.models.base_model import to_table
from applications.views.admin.passport import logout

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.get('/change_password')
@admin_login_required
def change_password():
    return render_template_mixin('admin/change_password.html')

@bp.post('/change_password')
@admin_login_required
def change_password_post():
    req = request.form
    old_password = req.get('oldpassword')
    new_password = req.get('newpassword')
    confirm_password = req.get('confirmpassword')
    user = User.query.get(current_user.id)
    if user.role == '管理员':
        if not user.validate_password(old_password):
            return fail_api(msg='原密码不正确')
        if new_password != confirm_password:
            return fail_api(msg='两次密码不同')
        user.set_password(new_password)
        db.session.commit()
        logout()
        return success_api(msg='密码修改成功')
    else:
        return fail_api(msg='权限不正确')

@bp.get('/manage')
@login_required
def user_manage():
    return render_template_mixin('admin/user_manage.html')

@bp.get('/list')
@admin_login_required
def user_list():
    users = User.query.filter(and_(User.id != 1, User.delete_at.is_(None))).all()
    return to_table(users)


@bp.get('/set_admin')
@admin_login_required
def set_admin():
    uid = request.args.get('id')
    opt = request.args.get('opt')
    user = User.query.get(uid)
    if opt == 'yes':
        user.role = '管理员'
        msg = '设置管理员权限成功'
    else:
        user.role = '普通会员'
        msg = '取消管理员权限成功'
    user.update_at = datetime.now()
    db.session.commit()
    return success_api(msg=msg)


@bp.get('/set_active')
@admin_login_required
def set_active():
    uid = request.args.get('id')
    opt = request.args.get('opt')
    user = User.query.get(uid)
    if opt == 'lock':
        user.enable = 0
        msg = '账户锁定成功'
    else:
        user.enable = 1
        msg = '账户激活成功'
    user.update_at = datetime.now()
    db.session.commit()
    return success_api(msg=msg)