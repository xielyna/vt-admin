"""
@File    : error.py
@Date    : 2019-12-28
@Author  : zhucong
@Desc    : 定义蓝图错误页
"""
from . import blueprint
from flask import jsonify, render_template, request


@blueprint.app_errorhandler(400)
def page_400(error):
    """
    400
    @param error:
    @return:
    """
    page_code = 400
    page_title, page_info = str(error).split(':')
    if '/api/' in request.url:
        return jsonify({'code': -page_code, 'msg': page_title})
    else:
        return render_template('base_error.html', page_title=page_title, page_info=page_info), page_code


@blueprint.app_errorhandler(401)
def page_401(error):
    """
    401
    @param error:
    @return:
    """
    page_code = 401
    page_title, page_info = str(error).split(':')
    if '/api/' in request.url:
        return jsonify({'code': -page_code, 'msg': page_title})
    else:
        return render_template('base_error.html', page_title=page_title, page_info=page_info), page_code


@blueprint.app_errorhandler(403)
def page_403(error):
    """
    403
    @param error:
    @return:
    """
    page_code = 403
    page_title, page_info = str(error).split(':')
    if '/api/' in request.url:
        return jsonify({'code': -page_code, 'msg': page_title})
    else:
        return render_template('base_error.html', page_title=page_title, page_info=page_info), page_code


@blueprint.app_errorhandler(404)
def page_404(error):
    """
    404
    @param error:
    @return:
    """
    page_code = 404
    page_title, page_info = str(error).split(':')
    if '/api/' in request.url:
        return jsonify({'code': -page_code, 'msg': page_title})
    else:
        return render_template('base_error.html', page_title=page_title, page_info=page_info), page_code


@blueprint.app_errorhandler(405)
def page_405(error):
    """
    405
    @param error:
    @return:
    """
    page_code = 405
    page_title, page_info = str(error).split(':')
    if '/api/' in request.url:
        return jsonify({'code': -page_code, 'msg': page_title})
    else:
        return render_template('base_error.html', page_title=page_title, page_info=page_info), page_code


@blueprint.app_errorhandler(500)
def page_500(error):
    """
    500
    @param error:
    @return:
    """
    page_code = 500
    page_title, page_info = str(error).split(':')
    if '/api/' in request.url:
        return jsonify({'code': -page_code, 'msg': page_title})
    else:
        return render_template('base_error.html', page_title=page_title, page_info=page_info), page_code
