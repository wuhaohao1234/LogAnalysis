from applications.extensions import db
from applications.models.base_model import BaseModel


class TaskReport(db.Model, BaseModel):
    __tablename__ = 'scan_report'
    scan_id = db.Column(db.Integer, comment='任务 ID')
    report_path = db.Column(db.String(256), comment='报告内容地址')

    def __init__(self, scan_id, report_path=None):
        self.scan_id = scan_id
        self.report_path = report_path
