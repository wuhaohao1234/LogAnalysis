from applications.extensions import db
from applications.models.base_model import BaseModel


class Task(db.Model, BaseModel):
    __tablename__ = 'scan_tasks'
    uid = db.Column(db.Integer, comment='发起用户ID')
    url = db.Column(db.String(128), comment='扫描地址')
    task_type_id = db.Column(db.Integer, comment='任务类型 ID')
    task_status_id = db.Column(db.Integer, default=1, comment='任务状态 ID')

    def __init__(self, uid, url='127.0.0.1', task_type_id=1):
        self.uid = uid
        self.url = url
        self.task_type_id = task_type_id
