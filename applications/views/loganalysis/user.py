import os

from flask import Blueprint, request, session, current_app
from flask_login import current_user
from sqlalchemy import and_
from werkzeug.utils import secure_filename

from applications.common import render_template_mixin
from applications.common.utils.http import success_api, fail_api
from applications.extensions import db, user_login_required
from applications.models import User, LoginLog
from applications.models.base_model import to_table
from applications.models.vo.login_log_vo import LoginLogVo
from applications.views.loganalysis.passport import logout

bp = Blueprint('user', __name__, url_prefix='/')


# 注册新用户页面
@bp.get('/register')
def register():
    return render_template_mixin('loganalysis/register.html')


# 添加新用户
@bp.post('/register')
def register_post():
    req = request.form
    username = req.get('username')
    password = req.get('password')
    confirm_password = req.get('confirm_password')
    code = req.get('captcha').__str__().lower()

    if not username or not password or not confirm_password:
        return fail_api(msg="用户名或密码没有输入")

    if not code:
        return fail_api(msg="验证码没有输入")

    s_code = session.get("code", None)
    session["code"] = None
    if not all([code, s_code]):
        return fail_api(msg="参数错误")

    if code != s_code:
        return fail_api(msg="验证码错误")
    user = User.query.filter_by(username=username).first()

    if password != confirm_password:
        return fail_api(msg="两次密码输入的不同")

    if user:
        return fail_api(msg="用户名已存在")

    new_user = User.from_response(User, request.form)
    new_user.set_password(new_user.password)
    db.session.add(new_user)
    db.session.commit()

    return success_api('注册成功')


@bp.get('/update')
@user_login_required
def update():
    return render_template_mixin('loganalysis/update_info.html')


@bp.post('/update')
@user_login_required
def update_post():
    user = User.query.get(current_user.id).set_dict(request.form)

    avatar_file = request.files['avatar']
    if avatar_file.filename != '':
        filename = secure_filename(avatar_file.filename)
        upload_path = current_app.config['AVATAR_UPLOAD_FOLDER']
        file_path = os.path.join(upload_path, filename)
        avatar_file.save(file_path)
        user.avatar = upload_path + '/' + filename
    db.session.commit()
    return success_api(msg='信息更新成功')


@bp.get('/change_password')
@user_login_required
def change_password():
    return render_template_mixin('loganalysis/mine_change_password.html')


@bp.post('/change_password')
def change_password_post():
    if not current_user.is_authenticated:
        return fail_api(msg='您还没有登录')
    if current_user.is_authenticated and current_user.is_admin:
        return fail_api(msg='权限不正确')

    req = request.form
    old_password = req.get('oldpassword')
    new_password = req.get('newpassword')
    confirm_password = req.get('confirmpassword')

    if not old_password or not new_password or not confirm_password:
        return fail_api(msg='参数错误')

    if new_password != confirm_password:
        return fail_api(msg='两次密码不同')

    user = User.query.get(current_user.id)
    if not current_user.validate_password(old_password):
        return fail_api(msg='原密码不正确')
    user.set_password(new_password)
    db.session.commit()
    logout()
    return success_api(msg='密码修改成功')


@bp.get('/mine')
@user_login_required
def mine():
    return render_template_mixin('loganalysis/mine.html')


@bp.post('/mine')
@user_login_required
def mine_user_update():
    ...


@bp.get('/new_register_list')
def new_register_list():
    users = User.query.filter(and_(User.delete_at.is_(None), User.role != '管理员')).order_by(
        User.create_at.desc()).limit(10).all()
    return to_table(users)
