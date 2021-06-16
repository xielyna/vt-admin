"""
@File    : todict.py
@Date    : 2020-09-11
@Author  : zhucong
@Desc    : None
"""


def tolist(res=None):
    """
    序列化sqlalchemy查询结果list为dict
    @param res: 查询结果
    @return:
    """
    return [r.todict() for r in res if r]


def todict(self):
    """
    序列化sqlalchemy查询结果为dict
    :return: 序列化之后的dict
    """
    rdata = {}
    for c in self.__table__.columns:
        key = c.name
        value = getattr(self, c.name)
        if type(value) == int:
            rdata[key] = int(value)
        elif type(value) == float:
            rdata[key] = float(value)
        elif type(value) == bool:
            rdata[key] = bool(value)
        elif value is None:
            rdata[key] = ''
        else:
            rdata[key] = str(value)
    return rdata
