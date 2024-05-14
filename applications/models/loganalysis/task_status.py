from applications.extensions import db
from applications.models.base_model import BaseModel


class TaskStatus(db.Model, BaseModel):
    __tablename__ = 'task_status'
    status = db.Column(db.String(32), comment='状态')
