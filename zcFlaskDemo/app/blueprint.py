"""
@File    : blueprint.py
@Date    : 2020-05-13
@Author  : zhucong
@Desc    : 注册蓝图
"""

import os
from importlib import import_module


def config_blueprint(app):
    """
    配置蓝图, 自动注册带有routes.py的蓝图
    @param app:
    """
    app_path = os.path.abspath(os.path.dirname(__file__))
    apps = os.listdir(app_path)
    apps = [f for f in apps if os.path.exists(os.path.join(app_path, f, 'routes.py'))]
    # print(f' * Blueprint registered: {apps}')
    for module_name in apps:
        module = import_module(f'app.{module_name}.routes')
        app.register_blueprint(module.blueprint)
