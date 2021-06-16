"""
@File    : routes.py
@Date    : 2020-10-20
@Author  : zhucong
@Desc    : 路由文件
"""

from . import blueprint
from .funcs.api import api_login

# 在这里统一注册路由
blueprint.add_url_rule('/api/login', view_func=api_login, methods=['POST'])
