from datetime import datetime

from applications.extensions import db
from applications.models.base_model import BaseModel


class Message(db.Model, BaseModel):
    __tablename__ = 'message'
    content = db.Column(db.String(256), comment='内容')
    from_id = db.Column(db.Integer, comment='来源 ID')
    to_id = db.Column(db.Integer, comment='目标 ID')
    type_id = db.Column(db.Integer, comment='消息类型 ID')

    def __init__(self, content, from_id, to_id, type_id=1):
        self.content = content
        self.from_id = from_id
        self.to_id = to_id
        self.type_id = type_id