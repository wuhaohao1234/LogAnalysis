from applications.extensions import db
from applications.models.base_model import BaseModel


class TaskType(db.Model, BaseModel):
    __tablename__ = 'task_type'
    type = db.Column(db.String(32), comment='类型')