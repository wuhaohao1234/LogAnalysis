from applications.extensions import db
from applications.models.base_model import BaseModel


class TaskListVo(db.Model, BaseModel):
    __tablename__ = 'task_list_vo'
    uid = db.Column(db.Integer, comment='发起用户ID')
    username = db.Column(db.String(128), comment='用户名')
    url = db.Column(db.String(128), comment='扫描地址')
    task_status = db.Column(db.String(32), comment='任务状态')
    task_type = db.Column(db.String(32), comment='类型')

    def __init__(self, id, username, url, task_type, task_status, create_at, update_at):
        self.id = id
        self.username = username
        self.url = url
        self.task_type = task_type
        self.task_status = task_status
        self.create_at = create_at
        self.update_at = update_at


