from datetime import datetime
from typing import Dict

from flask import json
from sqlalchemy.orm import class_mapper

from applications.common.utils.complex_encoder import ComplexEncoder
from applications.extensions.init_sqlalchemy import db


class BaseModel:
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='ID')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, comment='更新时间')
    delete_at = db.Column(db.DateTime, comment='删除时间')

    def set_dict(self, data: Dict):
        if data is None:
            return None

        for attr in dir(self):
            if not attr.startswith('_') and attr in data.keys():
                setattr(self, attr, data[attr])
        return self

    @staticmethod
    def from_response(model_class, resp_fields: Dict[str, str]):
        return BaseModel.from_dict(model_class, resp_fields)

    @staticmethod
    def from_json(model_class, json_str):
        if json_str is None or len(json_str) == 0:
            return None
        model_dict = json.loads(json_str)
        return BaseModel.from_dict(model_class, model_dict)

    @staticmethod
    def from_dict(model_class, model_dict: Dict[str, str]):
        if model_dict is None or len(model_dict) == 0:
            return None

        model_obj = model_class()
        for attr in dir(model_obj):
            if not attr.startswith('_') and attr in model_dict.keys():
                setattr(model_obj, attr, model_dict[attr])

        return model_obj

    def clear_none(self):
        for attr in dir(self):
            if not attr.startswith('_') and getattr(self, attr) is None:
                setattr(self, attr, '')
        return self

    def to_json(self):
        model_dict = self.to_dict()
        return json.dumps(model_dict, cls=ComplexEncoder, ensure_ascii=False)

    def to_dict(self):
        columns = [c.key for c in class_mapper(self.__class__).columns]
        return dict((c, getattr(self, c)) for c in columns)


# models 数据转换 json
def list2json(models):
    models_list = [m.to_dict() for m in models]
    json_data = json.dumps(models_list, cls=ComplexEncoder, ensure_ascii=False)
    return json_data


# layui 表格数据
def to_table(models):
    count = len(models)
    return '{"code": 0, "msg": "success", "count": ' + str(count) + ', "data": ' + list2json(models) + '}'
