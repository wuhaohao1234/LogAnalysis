from applications.extensions import db
from applications.models.base_model import BaseModel


class ScanRole(db.Model, BaseModel):
    __tablename__ = 'scan_roles'
    role_name = db.Column(db.String(64), comment='角色名称')