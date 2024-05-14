# 获取验证码
from flask import session, Blueprint

from applications.common.get_captcha import get_captcha

bp = Blueprint('get_captcha', __name__, url_prefix='/')


@bp.get('/getCaptcha')
def get_page_captcha():
    resp, code = get_captcha()
    session["code"] = code
    return resp
