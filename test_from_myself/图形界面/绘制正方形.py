import turtle
import time

turtle.title("绘制矩形")
turtle.color("purple")
turtle.pensize(5)
turtle.speed(1)
turtle.goto(0,0)

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.up()
turtle.goto(-150,-100)
turtle.color("red")
turtle.pensize(10)
turtle.write("Done")

