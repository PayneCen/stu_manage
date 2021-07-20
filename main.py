# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from student import *
from course import *
from selection import *
from score import *
from service import service
import pic


class Ui_Login_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Login_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(1300, 700)
        Login_Dialog.setMinimumSize(QtCore.QSize(1300, 700))
        Login_Dialog.setMaximumSize(QtCore.QSize(1300, 700))
        self.label = QtWidgets.QLabel(Login_Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/img/background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Button1 = QtWidgets.QPushButton(Login_Dialog)
        self.Button1.setGeometry(QtCore.QRect(930, 500, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button1.setFont(font)
        self.Button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(72, 21, 93);")
        self.Button1.setObjectName("Button1")
        self.Button3 = QtWidgets.QPushButton(Login_Dialog)
        self.Button3.setGeometry(QtCore.QRect(930, 580, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button3.setFont(font)
        self.Button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(72, 21, 93);")
        self.Button3.setObjectName("Button3")
        self.Button4 = QtWidgets.QPushButton(Login_Dialog)
        self.Button4.setGeometry(QtCore.QRect(1110, 580, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button4.setFont(font)
        self.Button4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(72, 21, 93);")
        self.Button4.setObjectName("Button4")
        self.Button2 = QtWidgets.QPushButton(Login_Dialog)
        self.Button2.setGeometry(QtCore.QRect(1110, 500, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button2.setFont(font)
        self.Button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(72, 21, 93);")
        self.Button2.setObjectName("Button2")
        self.Button1.clicked.connect(self.student)
        self.Button2.clicked.connect(self.course)
        self.Button3.clicked.connect(self.selection)
        self.Button4.clicked.connect(self.score)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "教务管理系统"))
        self.Button1.setText(_translate("Login_Dialog", "学生管理"))
        self.Button3.setText(_translate("Login_Dialog", "学生选课"))
        self.Button4.setText(_translate("Login_Dialog", "成绩评定"))
        self.Button2.setText(_translate("Login_Dialog", "课程管理"))

    def student(self):
        ui_student.show()
        MainWindow.close()

    def course(self):
        ui_course.show()
        MainWindow.close()

    def selection(self):
        ui_selection.show()
        MainWindow.close()

    def score(self):
        ui_score.show()
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui_student = Ui_student_manage()
    ui_course = Ui_course_manage()
    ui_selection = Ui_selection()
    ui_score = Ui_score()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())