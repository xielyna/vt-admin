"""
@File    : config.py
@Date    : 2019-12-28
@Author  : zhucong
@Desc    : 配置文件
"""
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """
    基础配置
    """

    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    DATE_FORMAT = '%Y-%m-%d'
    TIME_FORMAT = '%H:%M:%S'

    # COOKIE和SESSION
    SECRET_KEY = 'KnScxZPFcl03PjUfBR'
    SESSION_COOKIE_NAME = 'zsession'
    SESSION_KEY_PREFIX = 'zt_'
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=3)
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=3)

    # jsonfiy设置
    JSON_AS_ASCII = False

    # 日志设置
    LOG_LEVEL = 'DEBUG'
    LOG_PATH = Path(BASE_DIR, 'logs')
    Path(LOG_PATH).mkdir(parents=True, exist_ok=True)

    # 数据库
    DATABASE_PATH = Path(BASE_DIR, 'data.db')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_NATIVE_UNICODE = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_POOL_SIZE = 5
    # SQLALCHEMY_POOL_TIMEOUT = 5
    SQLALCHEMY_POOL_RECYCLE = 2
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        """
        初始化APP
        @param app:
        """
        pass


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG = True

    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = False


class TestConfig(Config):
    """
    测试环境配置
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    生产环境配置
    """
    DEBUG = False
    LOG_LEVEL = 'INFO'


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
