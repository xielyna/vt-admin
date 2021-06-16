"""
@File    : __init__.py
@Date    : 2020-10-20
@Author  : zhucong
@Desc    : 创建App; 加载配置, 扩展, 日志等.
"""

import os
from flask import Flask

from app.blueprint import config_blueprint
from app.config import config
from app.exts import config_ext
from app.log import config_log


# 将创建app的动作封装成一个函数
def create_app(config_name=None):
    """
    创建App
    @param config_name:
    @return:
    """

    config_name = os.getenv('FLASK_ENV') or 'default'

    # 创建app实例对象
    app = Flask(__name__, static_folder=None)

    # 加载配置
    app.config.from_object(config.get(config_name))
    config.get(config_name).init_app(app)

    # 加载扩展
    config_ext(app)
    config_log(app)
    config_blueprint(app)

    return app
