from applications.extensions import ma
from marshmallow import fields


class LogOutSchema(ma.Schema):
    id = fields.Integer()
    method = fields.Str()
    uid = fields.Str()
    url = fields.Str()
    description = fields.Str()
    ip = fields.Str()
    user_agent = fields.Str()
    success = fields.Bool()
    create_at = fields.DateTime()
