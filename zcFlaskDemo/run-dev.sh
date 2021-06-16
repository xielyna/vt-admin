#!/usr/bin/env bash

# 激活虚拟环境
source .venv/bin/activate

# 设置环境
export FLASK_ENV=development

# 启动
flask run -h 0.0.0.0 -p 8882
