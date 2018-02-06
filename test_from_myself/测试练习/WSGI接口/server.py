from wsgiref.simple_server import make_server
from hello import application

httpd =make_server("", 8000, application)
print("server http on port 8000...")

# httpd.handle_request()  # 处理一个request之后立即退出程序

httpd.serve_forever()  # 开启监听

# WSGI：Web Server Gateway Interface
# python server.py来启动WSGI服务器
# Ctrl+C终止服务器
