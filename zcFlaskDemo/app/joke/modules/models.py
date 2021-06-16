"""
@File    : data.py
@Date    : 2020-07-30
@Author  : zhucong
@Desc    : None
"""
import datetime
from app.exts import db


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    content = db.Column(db.Text())
    create_by = db.Column(db.String())
    create_at = db.Column(db.DateTime(), default=datetime.datetime.now)
