from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1>Home</h1>"

# 同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中
@app.route("/signin", methods=["GET"])
def asignin_form():
    return """<form action="/signin" method="post">\
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign in</button></p>
    </form>
    """

@app.route("/signin", methods=["POST"])
def signin():
    # 需要从request对象读取表单内容：
    if request.form["username"] == "admin" and request.form["password"] == "password":
        return "<h1>hello, admin</h1>"
    return "<h1>bad username of password</h1>"

if __name__ == '__main__':
    app.run()