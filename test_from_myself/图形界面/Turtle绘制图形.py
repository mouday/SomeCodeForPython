#Turtle绘制图形.py
import turtle
import time

t=turtle.Turtle()


t.pensize(3)
t.penup()
t.goto(-200,-50)
t.pendown()
t.circle(40,steps=3)#绘制三角形

t.penup()
t.goto(-100,-50)
t.pendown()
t.circle(40,steps=4)#绘制菱形

t.penup()
t.goto(0,-50)
t.pendown()
t.circle(40,steps=5)#绘制五边形

t.penup()
t.goto(100,-50)
t.pendown()
t.circle(40,steps=6)#绘制六边形

t.penup()
t.goto(200,-50)
t.pendown()
t.circle(40)  # 绘制圆
t.down()

while True:
    time.sleep(1000)