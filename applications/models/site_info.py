from applications.extensions import db
from applications.models.base_model import BaseModel


class SiteInfo(db.Model, BaseModel):
    __tablename__ = 'site_info'
    title = db.Column(db.String(64), default='', comment='网站标题')
    logo = db.Column(db.String(128), default='', comment='网站 logo')
    site_url = db.Column(db.String(256), comment='网站 url')
    keywords = db.Column(db.String(128), comment='网站关键词')
    description = db.Column(db.Text, default='', comment='网站描述')
    tel = db.Column(db.String(128), comment='联系电话')
    site_email = db.Column(db.String(128), comment='管理员邮箱')
    site_copyright = db.Column(db.String(128), comment='网站版权信息')

