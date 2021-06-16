"""
@File    : routes.py
@Date    : 2020-10-20
@Author  : zhucong
@Desc    : 路由文件
"""

from . import blueprint
from .funcs.page import page_index
from .error import *

blueprint.add_url_rule('/', view_func=page_index)
