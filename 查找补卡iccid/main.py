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
import findlinebyicicd

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

        self.btn_convert = QPushButton('查找', self)
        self.btn_convert.setGeometry(200, 220, 100, 30)
        self.btn_convert.clicked.connect(self.convert)

        self.txt_path = QLineEdit(self)
        self.txt_path.setGeometry(130, 72, 200, 20)

        self.label2 = QLabel("ICCID：", self)
        self.label2.move(50, 122)

        self.txt_iccid = QLineEdit(self)
        self.txt_iccid.setGeometry(130, 122, 200, 20)

        self.btn_open = QPushButton('<<', self)
        self.btn_open.move(350, 122)
        self.btn_open.clicked.connect(self.showFileDialog)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('补卡工具')
        self.setWindowIcon(QIcon('icons/Limewire.ico'))
        self.show()

    def showDialog(self):
        filename = QFileDialog.getExistingDirectory(self,"选取文件夹","./")
        print(filename)
        self.txt_path.setText(filename)

    def showFileDialog(self):
        filename = QFileDialog.getOpenFileName(self,"选取文件夹","./")
        print(filename)
        self.txt_iccid.setText(filename[0])

    def convert(self):
        flag = True
        try:
            iccid = self.txt_iccid.text()
            path = self.txt_path.text()

            ret = findlinebyicicd.main(path, iccid)
            print(flag)
        except:
            flag =False 
        if flag == True:
            QMessageBox.question(self, 'Message',"查找成功,数量：{}".format(ret), QMessageBox.Yes)
        else:
            QMessageBox.question(self, 'Message', "查找失败！", QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())