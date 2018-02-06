#温度计算程序改进版.py
from graphics import *

def convert(entry):
	#输入转换
	c=eval(entry.getText())
	f=9.0/5.0*c+32
	return f

def colorChange(win,entry):
	# 修改窗体背景颜色
	c=eval(entry.getText())
	weight=c/100.0
	newColor=color_rgb(255*weight,66+150*(1-weight),255*(1-weight))
	win.setBackground(newColor)

def main():
	win=GraphWin("温度转换",400,300)
	win.setCoords(0.0,0.0,4.0,3.0)
	#绘制输入接口
	Text(Point(1,2.8),"摄氏温度：").draw(win)	
	Text(Point(1.5,2.5),"请输入温度（0-100）:").draw(win)
	Text(Point(1,1),"华氏温度：").draw(win)
	#绘制输入框
	entry=Entry(Point(2.7,2.5),5)
	entry.setText("0.0")
	entry.draw(win)
	#绘制输出显示文本
	output=Text(Point(2,1),"")
	output.draw(win)
	#绘制按钮
	button=Text(Point(1.7,1.8),"转换")
	button.draw(win)
	rect=Rectangle(Point(1.2,1.3),Point(2.2,2.3))
	rect.draw(win)
	#等待鼠标点击	
	win.getMouse()
	#转换输入
	result=convert(entry)
	#显示输出
	output.setText(result)
	#改变颜色
	colorChange(win,entry)
	#改变按钮文字
	button.setText("退出")
	#等待点击事件，退出程序
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()