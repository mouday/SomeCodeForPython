import sys
from PyQt5.QtWidgets import (QApplication,QWidget,
    QToolTip,QPushButton,QMessageBox,QDesktopWidget)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

# QtGui,QDesktopWidget类提供了用户的桌面信息,包括屏幕大小。

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #界面绘制
    def initUI(self):
        #设置字体
        QToolTip.setFont(QFont("微软雅黑",10))
        
        #创建提示
        self.setToolTip("this is a <b>QWidget</b> widget")
        
         #创建一个button
        btn=QPushButton("Quit",self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip("this is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        #创建一个退出button
        btn=QPushButton("Quit",self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip("this is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(200,50)

        #设置窗体
        self.setGeometry(300,300,300,220)#设置窗口大小和位置
        self.resize(500,300)
        self.center()
        self.setWindowTitle("PyQt5Test")#设置窗口标题
        self.setWindowIcon(QIcon("Internet Explorer 10.png"))#设置图标
        self.show()#显示窗口

    #重写closeEvent()事件处理
    def closeEvent(self,event):
        reply=QMessageBox.question(self,"Message",
            "are you sure to quit?",QMessageBox.Yes|
            QMessageBox.No,QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #控制窗口显示在屏幕中心的方法 
    def center(self):
        frame=self.frameGeometry()#获得窗口
        centerPoint=QDesktopWidget().availableGeometry().center()#获得屏幕中心点
        #显示到屏幕中心
        frame.moveCenter(centerPoint) 
        self.move(frame.topLeft())

def main():
    #创建应用程序和对象
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

# 参考网址：http://code.py40.com/pyqt5/16.html