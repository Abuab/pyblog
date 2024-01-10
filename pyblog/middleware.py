import logging
import os
import re
import uuid
import json
from flask import request, g
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


def load_middleware(app):

    def register_logging(app, log_name="kevin.log", log_folder="kevin_logs"):
        # 创建logger对象。传入logger名字
        app.logger.setLevel(logging.INFO)
        logs_storage_path = os.path.dirname(os.path.realpath('__file__')) + '/' + log_folder
        if not os.path.exists(logs_storage_path):
            os.makedirs(logs_storage_path)
        log_file_str = logs_storage_path + os.sep + log_name
        logging.basicConfig(level=logging.INFO)
        # interval滚动周期
        # when="MIDNIGHT",interval表示每天0点为更新点，每天生成一个文件
        # backupCount表示日志保存个数
        handler = TimedRotatingFileHandler(
            filename=log_file_str, when="MIDNIGHT", interval=1,backupCount=365,encoding="utf-8"
        )
        handler.setLevel(logging.INFO)
        handler.suffix = "%Y-%m-%d.log"
        # extMatch是编译好正则表达式，用于匹配日志文件名后缀
        # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
        handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s")
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)

    register_logging(app)

    @app.before_request
    def before():
        g.requestId = uuid.uuid4().hex
        print("hello", request.url)

    @app.after_request
    def after(response):
        app.logger.info(json.dumps({
            "AccessLog": {
                "status_code": response.status_code,
                "method": request.method,
                "ip": request.headers.get('X-Real-IP', request.remote_addr),
                "url": request.url,
                "referer": request.headers.get('Referer'),
                "agent": request.headers.get("User-Agent"),
                "requestId": str(g.requestId),
            }
        }, ensure_ascii=False
        ))
        return response
