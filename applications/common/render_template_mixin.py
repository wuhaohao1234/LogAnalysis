from flask import render_template, current_app
from flask_login import current_user

from applications.models import SiteInfo
from applications.models.vo.user_vo import UserVo


def render_template_mixin(template_name, opt=None):
    site_info = SiteInfo.query.first()
    user_vo = UserVo.get_vo(current_user)
    layui_theme = current_app.config["LAYUI_THEME"]
    if user_vo is not None:
        user_vo.clear_none()
    return render_template(template_name, site_info=site_info.clear_none(), user=user_vo, layui_theme=layui_theme , opt=opt)
