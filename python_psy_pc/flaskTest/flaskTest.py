from flask import Flask

print(__name__)
app=Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

if __name__=="__main__":
    app.run()

