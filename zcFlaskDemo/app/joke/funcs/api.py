"""
@File    : api.py
@Date    : 2020-10-20
@Author  : zhucong
@Desc    : API接口函数页面
"""
from app.exts import db
from flask import current_app, jsonify, request
from app.joke.modules.models import Joke
from app.user.funcs.auth import token_auth


@token_auth
def api_joke_list():
    """
    API
    @return:
    """
    # 读POST过来的username和password
    jokes = Joke.query.all()
    jokes_list = db.Model.tolist(jokes)  # 这里我自己为db.Model扩展了一个方法, 可以快速的将查询结果转换为list
    data = {'code': 0, 'msg': f'成功读取到{len(jokes)}条数据', 'data': jokes_list}
    return jsonify(data)
