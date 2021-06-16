"""
@File    : __init__.py
@Date    : 2020-10-07
@Author  : zhucong
@Desc    : None
"""
import os
from flask import Blueprint

pathname = os.path.basename(os.path.dirname(__file__))
blueprint = Blueprint(
    pathname,
    __name__,
    url_prefix='/',
    template_folder='templates',
    static_folder='static'
)
