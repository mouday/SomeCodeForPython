from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

# 同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中
@app.route("/signin", methods=["GET"])
def asignin_form():
    return render_template("form.html")

@app.route("/signin", methods=["POST"])
def signin():
    # 需要从request对象读取表单内容：
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "password":
        return render_template("signin-ok.html",username=username)
    return render_template("form.html", message="bad username or password",username=username)

if __name__ == '__main__':
    app.run()