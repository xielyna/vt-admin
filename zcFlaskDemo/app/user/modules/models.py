"""
@File    : data.py
@Date    : 2020-07-30
@Author  : zhucong
@Desc    : None
"""

from app.exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)

