import logging
import os
from datetime import timedelta
from urllib.parse import quote_plus as urlquote

from dotenv import load_dotenv


# 应用配置类
class BaseConfig:
    SUPERADMIN = 'admin'

    USER_LOGIN_VIEW = 'loganalysis.passport.login'
    ADMIN_LOGIN_VIEW = 'admin.passport.login'
    ADMIN_ROOT_VIEW = 'admin.index.index'
    SITE_ROOT_VIEW = 'loganalysis.index.index'

    UPLOADED_PHOTOS_DEST = 'static/upload'
    UPLOADED_FILES_ALLOW = ['gif', 'jpg', 'png']
    UPLOADS_AUTOSERVE = True

    AVATAR_UPLOAD_FOLDER = 'static/uploads/avatar'
    REPORT_UPLOAD_FOLDER = 'static/uploads/report'

    SCAN_API_URL = 'http://127.0.0.1:8888/start'
    ADD_REPORT_URL = 'http://192.168.3.78:5500/log_analysis/task/add_report'

    # layui 主题设置
    LAYUI_THEME = 'layui-bg-blue'

    # JSON配置
    JSON_AS_ASCII = False

    SECRET_KEY = "myadmin"

    # mysql 配置
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_DATABASE = "log_analysis"

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
    SQLALCHEMY_ECHO = False
    # 默认日志等级
    LOG_LEVEL = logging.INFO

    """
    session
    """

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    SESSION_TYPE = "filesystem"  # 默认使用文件系统来保存会话

    # 会话是否持久化
    SESSION_USE_SIGNER = True  # 是否对发送到浏览器上 session 的 cookie 值进行加密
    SESSION_PERMANENT = False

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{self.MYSQL_USERNAME}:{urlquote(self.MYSQL_PASSWORD)}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}?charset=utf8mb4"
        # self.update_database_uri()

    def update_database_uri(self):
        self.SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{self.MYSQL_USERNAME}:{urlquote(self.MYSQL_PASSWORD)}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}?charset=utf8mb4"


class DevelopmentConfig(BaseConfig):
    # mysql 配置
    # mysql 配置
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 63306
    MYSQL_DATABASE = "log_analysis"

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    # 数据库的配置信息
    # 开启 sql 查询语句显示
    SQLALCHEMY_ECHO = True

    # 默认日志等级
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    # mysql 配置
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 63306
    MYSQL_DATABASE = "log_analysis"

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
    SQLALCHEMY_ECHO = False


class HomeConfig(BaseConfig):
    # mysql 配置
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "192.168.3.29"
    MYSQL_PORT = 3306
    MYSQL_DATABASE = "log_analysis"

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    SQLALCHEMY_ECHO = True
    # 默认日志等级
    LOG_LEVEL = logging.DEBUG


class RaspConfig(BaseConfig):
    # mysql 配置
    MYSQL_USERNAME = "rasp"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "192.168.3.40"
    MYSQL_PORT = 3306
    MYSQL_DATABASE = "log_analysis"

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    SQLALCHEMY_ECHO = True
    # 默认日志等级
    LOG_LEVEL = logging.DEBUG


# 根据配置 .env 提取 config 类
def get_app_config_obj():
    config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'home': HomeConfig,
        'rasp': RaspConfig,
        'default': DevelopmentConfig
    }
    # 加载 flask 环境配置文件
    load_dotenv(override=True, verbose=True)
    # 获取当前配置类名
    config_name = os.getenv('FLASK_ENV', default='default')

    return config[config_name]
