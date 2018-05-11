"""逻辑接口
"""
import logic
from flask import Flask

app=Flask(__name__)

@app.route("/")# 定义接口名
def home_page():# 接口方法
    home_data=logic.get_home() #逻辑函数
    return home_data

@app.route("/books")
def books():
    books_data = logic.get_books()
    return books_data

@app.route("/book/<book_id>")
def book(book_id):
    book_data = logic.get_book(book_id)
    return book_data

@app.route("/students")
def students():
    students_data = logic.get_students()
    return students_data

@app.route("/student/<student_id>")
def student(student_id):
    student_data = logic.get_student(student_id)
    return student_data