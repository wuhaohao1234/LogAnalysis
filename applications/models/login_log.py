from applications.extensions import db
from applications.models.base_model import BaseModel


class LoginLog(db.Model, BaseModel):
    __tablename__ = 'login_log'
    uid = db.Column(db.Integer)
    url = db.Column(db.String(256))
    method = db.Column(db.String(10))
    ip = db.Column(db.String(258))
    user_agent = db.Column(db.String(256))
    description = db.Column(db.String(128))
    success = db.Column(db.Integer)
