import functools
from flask import current_app, jsonify, render_template, request, session
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def token_auth(view_func):
    """
    @return: 检查用户登录状态
    """

    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        """
        装饰器
        @param args:
        @param kwargs:
        @return:
        """
        # Token验证
        token = request.headers.get('Authorization') or request.args.get('token')
        user = load_token(token)
        username = user.get('username', '')

        if username:
            current_app.logger.debug(f'用户Token验证成功, 用户: {username}')
            return view_func(*args, **kwargs)

        current_app.logger.debug(f'用户Token验证失败')

        if '/api/' in request.path:  # API请求, 返回json
            denied_page = jsonify({'code': -403, 'msg': 'Access to this resource on the server is denied!'})
        else:  # 不是API请求, 转到错误页
            denied_page = render_template('base_error.html',
                                          page_title='403 Forbidden',
                                          page_info='Token认证失败.'), 403
            return denied_page
        return denied_page

    return wrapper


def load_token(token):
    """
    加载Token
    @param token:
    @return:
    """
    user = {}
    if not token:
        return user
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        token = token.replace('token ', '')
        user = s.loads(token)
    except Exception as e:
        current_app.logger.error(f'Token读取失败, {e}')
        user = {}
        pass
    return user
