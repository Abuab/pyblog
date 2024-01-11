from flask import Blueprint, render_template, request
from .models import Student

blue = Blueprint("blue", __name__, template_folder='../templates', static_folder='../static')	# 将template_folder='../templates'放在这里也可以

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/')
def index():
    return '深深太平洋底深深伤心'

@blue.route('/nihao/')
def index():
    return 'WTF!'

@blue.route('/hello/')
def hello():
    return render_template('index.html')

@blue.route('/kevin/')
def kevin():
    user_agent=request.headers.get('User_Agent')
    return 'Hello, Kevin!\nuser_agent is %s\n' %user_agent

@blue.route('/addstudent/')
def add_student():
    student = Student()
    student.s_name = 'kevin'
    student.s_age = 18
    student.save()
    return '数据添加成功'
