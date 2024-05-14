from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from applications.extensions.init_sqlalchemy import db
from applications.models.base_model import BaseModel


class User(db.Model, BaseModel, UserMixin):
    __tablename__ = 'user'
    username = db.Column(db.String(128), comment='用户名')
    password = db.Column(db.String(128), comment='哈希密码')
    nickname = db.Column(db.String(128), comment='昵称')
    avatar = db.Column(db.String(256), comment='头像', default="/static/system/images/avatar.jpg")
    phone = db.Column(db.String(32), comment='电话号码')
    email = db.Column(db.String(128), comment='邮箱')
    role = db.Column(db.String(128), default='普通会员', comment='用户角色')
    enable = db.Column(db.Integer, default=1, comment='是否启用')
    is_admin = False

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2')

    def validate_password(self, password):
        return check_password_hash(self.password, password)

