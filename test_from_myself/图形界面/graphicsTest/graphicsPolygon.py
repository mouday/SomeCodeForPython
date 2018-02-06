#graphicsPolygon.py
from graphics import *
win=GraphWin("click me",300,300)
win.setCoords(0.0,0.0,300.0,300.0)
message=Text(Point(150,20),"click me five point")
message.draw(win)
win.getMouse()