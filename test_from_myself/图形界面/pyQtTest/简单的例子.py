import sys
from PyQt5.QtWidgets import QApplication,QWidget

app=QApplication(sys.argv)#创建应用程序
win=QWidget()#创建用户界面
win.resize(500,300)#调整大小，像素
win.move(350,200)#移动位置
win.setWindowTitle("simple")#设置标题
win.show()#显示

sys.exit(app.exec_())#退出程序