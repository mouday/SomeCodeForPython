from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response
import time
import os
import datetime
import pymysql
# 每个视图函数至少要有一个参数，通常被叫作request
"""
param : HttpRequest
return : HttpResponse
一个视图就是Python的一个函数
函数第一个参数的类型是HttpRequest；它返回一个HttpResponse实例
"""


def hello(request):
    return HttpResponse("hello world!")


def index(request):
    # assert False   使用断言抛出异常，替代print
    return render_to_response("base.html", locals())

def show_time(request):
    current_time=time.strftime("%H:%M:%S")
    return render_to_response("time.html", locals())

def show_date(request):
    current_time = time.strftime("%Y-%m-%d")
    return render_to_response("date.html",locals())

def show_current_datetime(request):
    now = datetime.datetime.now()  # 服务器的内部时钟
    # html = "<html><body>It is now %s<body></html>" % now
    t = Template("<html><body>my name is {{ name }}</body></html>")
    html = t.render(Context({"name": "Jack"}))
    return HttpResponse(html)


def show_datetime(request,offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours , it will be %s <body></html>" % (offset, dt)
    return HttpResponse(html)

def test(request):
    # with open(r"index.html", 'r') as f:
    # 获取自身所在的文件所在的目录
    # path = os.path.join(os.path.dirname(__file__), "templates").replace("\\", "/")
    t = get_template("index.html") # 获取模板文件
    d = {"name": "Jack", "items": ["item1", "item2", "item3"]}
    html=t.render(d) #传入字典
    return HttpResponse(html)

def shortcuts_test(request):
    time=datetime.datetime.now()
    return render_to_response("app/time.html", locals())

def name_list(request):
    db = pymysql.connect(user="root", db="mydb", passwd="123456", host="localhost")
    cursor = db.cursor()
    cursor.execute("SELECT name FROM mytb ORDER BY id")
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response("name_list.html", {"names": names})
