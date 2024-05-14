from flask import Blueprint, session, redirect, url_for, render_template, request
from flask_login import current_user, login_user, login_required, logout_user

from applications.common import render_template_mixin
from applications.common.login_log import login_log
from applications.common.utils.http import fail_api, success_api
from applications.models import User, SiteInfo

bp = Blueprint('passport', __name__, url_prefix='/passport')


# 登录
@bp.get('/login')
def login():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin.index.index'))
    return render_template_mixin('admin/login.html')


# 登录
@bp.post('/login')
def login_post():
    req = request.form
    username = req.get('username')
    password = req.get('password')
    remember = bool(req.get('remember-me'))
    code = req.get('captcha').__str__().lower()

    if not username or not password:
        return fail_api(msg="用户名或密码没有输入")
    if not code:
        return fail_api(msg="没有输入验证吗")

    s_code = session.get("code", None)
    session["code"] = None

    if not all([code, s_code]):
        return fail_api(msg="参数错误")

    if code != s_code:
        return fail_api(msg="验证码错误")

    user = User.query.filter_by(username=username).first()

    if not user:
        return fail_api(msg="不存在的用户")

    if user.enable == 0:
        return fail_api(msg="用户被暂停使用")

    if user.role != "管理员":
        return fail_api(msg="您没有权限访问该页面")

    if username == user.username and user.validate_password(password):
        # 登录
        login_user(user, remember=remember)
        # 记录登录日志
        login_log(request, uid=user.id, is_access=True)
        # 授权路由存入session
        role = current_user.role
        session['permissions'] = role
        return success_api(msg="登录成功")
    login_log(request, uid=user.id, is_access=False)
    return fail_api(msg="用户名或密码错误")


# 退出登录
@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if current_user.role == '管理员':
        logout_user()
        session.pop('permissions')
        return success_api(msg="注销成功")
    return fail_api(msg="您没有登录")