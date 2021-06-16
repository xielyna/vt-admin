"""
@File    : api.py
@Date    : 2020-10-20
@Author  : zhucong
@Desc    : API接口函数页面
"""

from flask import current_app, jsonify, request
from app.user.modules.models import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def api_login():
    """
    API
    @return:
    """
    # 读POST过来的username和password
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username or not username:  # 没有提供必要信息
        data = {'code': -1, 'msg': '请POST内容过来登录呀. username 和 password'}
        return jsonify(data)

    # 直接查库, 取结果咯
    user = User.query.filter(User.username == username, User.password == password).first()
    if not user:  # 没有结果, 返回个错误
        data = {'code': -1, 'msg': '无效的用户名或密码'}
        return jsonify(data)

    # 生成Token
    token_exp_sec = 7200  # Token超时时间
    serial = Serializer(current_app.config["SECRET_KEY"], expires_in=token_exp_sec)
    token = serial.dumps({"username": user.username}).decode('utf-8')  # 把用户名加入Token里面去, 下次传递过来就可以读出用户名
    data = {
        'token': token,
        'expires_in': token_exp_sec
    }
    data = {'code': 1, 'msg': '登录成功', 'data': data}
    return jsonify(data)
