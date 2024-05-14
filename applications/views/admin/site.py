from flask import Blueprint, request

from applications.common import render_template_mixin
from applications.common.utils.http import success_api
from applications.extensions import admin_login_required, db
from applications.models import SiteInfo

bp = Blueprint('site', __name__, url_prefix='/site')


@bp.get('/info')
@admin_login_required
def info():
    return render_template_mixin('admin/site_info.html')


@bp.post('/info')
@admin_login_required
def update_info():
    req = request.form
    title = req.get('title')
    logo = req.get('logo')
    url = req.get('url')
    description = req.get('description')
    keywords = req.get('keywords')
    tel = req.get('tel')
    email = req.get('email')
    site_copyright = req.get('copyright')

    site_info = SiteInfo.query.first()
    site_info.title = title
    site_info.logo = logo
    site_info.url = url
    site_info.description = description
    site_info.keywords = keywords
    site_info.tel = tel
    site_info.email = email
    site_info.site_copyright = site_copyright
    db.session.add(site_info)
    db.session.commit()
    return success_api(msg='网站信息更新成功')