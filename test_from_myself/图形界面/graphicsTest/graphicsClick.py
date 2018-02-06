#graphicsClick.py
from graphics import *
def main():
	win=GraphWin("click me!")
	for i in range(10):
		p=win.getMouse()
		print("click at :",p.getX(),p.getY())


main()