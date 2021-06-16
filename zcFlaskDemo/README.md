# zcFlaskDemo

---

## 部署说明

```
# 创建虚拟环境
python3 -m venv .venv

# 激活虚拟环境
call .venv/Scripts/activate.bat		# cmd
source .venv/bin/activate			# bash

# 安装依赖
pip3 install -r requirements.txt

```

````
│  blueprint.py				蓝本注册, 什么是蓝本呢?就是一个项目大了, 定义路由就很复杂
│  config.py				程序配置文件
│  exts.py					插件统一在这里初始化
│  log.py					日志, 我这里做了个拦截, 全交给第三方库loguru处理
│  __init__.py				创建App
│
├─base						基础App, 这个App是在根目录, 不能删除
│  │  config.py				每个App单独再弄个配置, 只给这个App用
│  │  error.py				定义全局错误页
│  │  routes.py				当前App的路由
│  │  __init__.py			注册蓝本
│  │
│  ├─funcs					公共函数
│  │      dbfunc.py
│  │      page.py			页面函数
│  │
│  ├─modules				公共模块
│  ├─static					静态资源目录
│  │      favicon.ico
│  │
│  └─templates				模板目录
│          base_error.html	模板
│          base_page.html	模板
│
├─joke						第二个App
│  │  routes.py				路由
│  │  __init__.py
│  │
│  ├─funcs
│  │      api.py			Api函数
│  │      __init__.py
│  │
│  └─modules
│          models.py		第二个App的数据模型
│
└─user						第三个App
    │  routes.py			路由
    │  __init__.py
    │
    ├─funcs
    │      api.py			Api函数
    │      auth.py			用户验证函数
    │      __init__.py
    │
    └─modules
            models.py		第三个App的数据模型

```

````

---

## 登录

`POST` `{host}/user/api/login`

```
{
"username": "test",
"password": "123"
}
```

## 获取笑话列表

`GET` `{host}/joke/api/list?token={token}`
token 也可以用 request header 传递, 具体看代码
