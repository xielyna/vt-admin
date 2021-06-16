"""
@File    : exts.py
@Date    : 2019-12-28
@Author  : zhucong
@Desc    : 扩展
"""
from concurrent.futures import ThreadPoolExecutor
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.base.funcs.dbfunc import tolist, todict


db = SQLAlchemy()

executor = ThreadPoolExecutor(50)


# 初始化
def config_ext(app):
    """
    配置扩展
    @param app:
    @return:
    """
    # 允许跨域访问api
    cors = CORS(app)

    db.init_app(app)
    # db查询结果序列化
    db.Model.todict = todict
    db.Model.tolist = tolist