from flask import Flask
from pyblog.ext import init_ext
from pyblog.settings import envs
from pyblog.views import init_blue
from pyblog.middleware import load_middleware

def create_app(env):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')	# template_folder='../templates'或者将这句放在views.py里的blue那里也可以
    # 初始化项目的配置
    app.config.from_object(envs.get(env))
    # 初始化 非路由相关 扩展库
    init_ext(app)
    # 路由初始化
    init_blue(app)
    load_middleware(app)
    return app
