from flask import Flask
from jinja2 import Environment


def init_jinja2(app: Flask) -> None:
    # 修改 jinja2 变量定界符
    app.jinja_env.variable_start_string = '{{{'  # 修改变量开始符号
    app.jinja_env.variable_end_string = '}}}'  # 修改变量结束符号
