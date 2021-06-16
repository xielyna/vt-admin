"""
@File    : log.py
@Date    : 2021-05-27
@Author  : zhucong
@Desc    : 配置Flask日志
"""

import logging
from pathlib import Path

from loguru import logger


class LogInterceptHandler(logging.Handler):
    """
    日志拦截, 交给logru处理
    """

    def emit(self, record):
        """
        拦截处理
        """
        try:
            log_level = logger.level(record.levelname).name
        except ValueError:
            log_level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(log_level, record.getMessage())


def config_log(app):
    """
    配置日志
    @param app:
    """

    log_path = app.config.get('LOG_PATH')

    log_level = app.config.get('LOG_LEVEL').upper() or 'DEBUG'
    log_levels = list(set(['ERROR', log_level]))

    print(f' * Log level is {log_levels}')

    for level in log_levels:
        log_level_path = Path(log_path, f"{level.lower()}.log")
        logger.add(sink=log_level_path, level=level, encoding="utf-8", enqueue=True, diagnose=True, rotation="00:00", retention="7 days")

    # 第三方库日志级别调整
    # for log in ['werkzeug', 'chardet', 'urllib3', 'requests', 'flask_caching']:
    #     logging.getLogger(log).setLevel('WARNING')

    logging.basicConfig(handlers=[LogInterceptHandler()], level=log_level)
