from applications.extensions import db
from applications.models.base_model import BaseModel


class LoginLogVo(db.Model, BaseModel):
    __tablename__ = ''
    uid = db.Column(db.Integer)
    url = db.Column(db.String(256))
    method = db.Column(db.String(10))
    ip = db.Column(db.String(258))
    user_agent = db.Column(db.String(256))
    description = db.Column(db.String(128))
    success = db.Column(db.Integer)
    username = db.Column(db.String(128))
    role = db.Column(db.String(128))

    def __init__(self, id, uid, username, url, ip, description, success, user_agent, role, create_at):
        self.id = id
        self.uid = uid
        self.username = username
        self.url = url
        self.ip = ip
        self.description = description
        self.success = success
        self.user_agent = user_agent
        self.role = role
        self.create_at = create_at
