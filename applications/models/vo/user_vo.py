from flask_login import current_user

from applications.extensions import db
from applications.models.vo.base_vo import BaseVo


class UserVo(BaseVo):
    username = db.Column(db.String(128), comment='用户名')
    nickname = db.Column(db.String(128), comment='昵称')
    avatar = db.Column(db.String(256), comment='头像', default="/static/images/avatar.jpg")
    role = db.Column(db.String(128), default='普通会员', comment='用户角色')
    is_authenticated = False
    is_admin = False
    if current_user is not None:
        is_authenticated = True

    @staticmethod
    def get_vo(user_obj=current_user):
        if user_obj is None:
            return None
        user_vo = UserVo()
        for attr in dir(user_vo):
            if not attr.startswith('_') and hasattr(user_obj, attr):
                setattr(user_vo, attr, getattr(user_obj, attr))
        return user_vo.clear_none()
