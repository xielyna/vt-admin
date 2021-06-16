"""
@File    : page.py
@Date    : 2020-10-20
@Author  : zhucong
@Desc    : 页面函数文件
"""

from flask import render_template

from app.base.config import PAGE_DESC, PAGE_TITLE


def page_index():
    """
    首页
    @return:
    """
    return render_template('base_page.html', page_title=PAGE_TITLE, page_info=PAGE_DESC), 200
