# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

In this example, we determine the event sender
object.

author: py40.com
last edited: 2017年3月
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,QLabel,
                             QInputDialog, QApplication,QFileDialog,QMessageBox)
from PyQt5.QtGui import QIcon
import combinetxt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.label1 = QLabel("选择文件夹：", self)
        self.label1.move(50, 75)

        self.label2 = QLabel("开发：彭世瑜  pengshiyuyx@gmail.com", self)
        self.label2.move(230, 280)

        self.btn_open = QPushButton('<<', self)
        self.btn_open.move(350, 70)
        self.btn_open.clicked.connect(self.showDialog)

        self.btn_convert = QPushButton('合并', self)
        self.btn_convert.setGeometry(200, 220, 100, 30)
        self.btn_convert.clicked.connect(self.convert)

        self.txt_path = QLineEdit(self)
        self.txt_path.setGeometry(130, 72, 200, 20)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('合并数据txt文本')
        self.setWindowIcon(QIcon('icons/Limewire.ico'))
        self.show()

    def showDialog(self):
        filename = QFileDialog.getExistingDirectory(self,"选取文件夹","./")
        print(filename)
        self.txt_path.setText(filename)

    def convert(self):
        flag = True
        try:
            path = self.txt_path.text()
            ret = combinetxt.combineTxt(path)
        except:
            flag =False
        if flag == True:
            QMessageBox.question(self, 'Message',"合并成功，文件数：%s"%(ret,), QMessageBox.Yes)
        else:
            QMessageBox.question(self, 'Message', "合并失败！", QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())