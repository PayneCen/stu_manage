# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from service import service

class Ui_student_manage(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_student_manage,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, student_manage):
        student_manage.setObjectName("student_manage")
        student_manage.resize(1300, 700)
        student_manage.setMinimumSize(QtCore.QSize(1300, 700))
        student_manage.setMaximumSize(QtCore.QSize(1300, 700))
        self.center()
        self.centralwidget = QtWidgets.QWidget(student_manage)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, 0, 1300, 700))
        self.background.setMinimumSize(QtCore.QSize(1300, 700))
        self.background.setMaximumSize(QtCore.QSize(1300, 700))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/pic/img/pix.jpg"))
        self.background.setScaledContents(False)
        self.background.setObjectName("background")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 10, 980, 650))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 230);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_32 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_32.setGeometry(QtCore.QRect(690, 230, 271, 31))
        self.horizontalLayoutWidget_32.setObjectName("horizontalLayoutWidget_32")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_32)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_39 = QtWidgets.QLabel(self.horizontalLayoutWidget_32)
        self.label_39.setMinimumSize(QtCore.QSize(50, 0))
        self.label_39.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_34.addWidget(self.label_39)
        self.s_idEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_32)
        self.s_idEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s_idEdit.setText("")
        self.s_idEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.s_idEdit.setReadOnly(False)
        self.s_idEdit.setPlaceholderText("")
        self.s_idEdit.setObjectName("s_idEdit")
        self.horizontalLayout_34.addWidget(self.s_idEdit)
        self.horizontalLayout_34.setStretch(0, 2)
        self.horizontalLayout_34.setStretch(1, 4)
        self.horizontalLayoutWidget_33 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_33.setGeometry(QtCore.QRect(690, 130, 271, 31))
        self.horizontalLayoutWidget_33.setObjectName("horizontalLayoutWidget_33")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_33)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_41 = QtWidgets.QLabel(self.horizontalLayoutWidget_33)
        self.label_41.setMinimumSize(QtCore.QSize(50, 0))
        self.label_41.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_35.addWidget(self.label_41)
        self.s_nameEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_33)
        self.s_nameEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s_nameEdit.setText("")
        self.s_nameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.s_nameEdit.setReadOnly(False)
        self.s_nameEdit.setPlaceholderText("")
        self.s_nameEdit.setObjectName("s_nameEdit")
        self.horizontalLayout_35.addWidget(self.s_nameEdit)
        self.horizontalLayout_35.setStretch(0, 2)
        self.horizontalLayout_35.setStretch(1, 4)
        self.horizontalLayoutWidget_34 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_34.setGeometry(QtCore.QRect(690, 330, 271, 31))
        self.horizontalLayoutWidget_34.setObjectName("horizontalLayoutWidget_34")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_34)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_43 = QtWidgets.QLabel(self.horizontalLayoutWidget_34)
        self.label_43.setMinimumSize(QtCore.QSize(50, 0))
        self.label_43.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_36.addWidget(self.label_43)
        self.s_mailEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_34)
        self.s_mailEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s_mailEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.s_mailEdit.setObjectName("s_mailEdit")
        self.horizontalLayout_36.addWidget(self.s_mailEdit)
        self.horizontalLayout_36.setStretch(0, 2)
        self.horizontalLayout_36.setStretch(1, 4)
        self.horizontalLayoutWidget_35 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_35.setGeometry(QtCore.QRect(690, 180, 271, 31))
        self.horizontalLayoutWidget_35.setObjectName("horizontalLayoutWidget_35")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_35)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_64 = QtWidgets.QLabel(self.horizontalLayoutWidget_35)
        self.label_64.setMinimumSize(QtCore.QSize(50, 0))
        self.label_64.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_37.addWidget(self.label_64)
        self.s_sexEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_35)
        self.s_sexEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s_sexEdit.setText("")
        self.s_sexEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.s_sexEdit.setReadOnly(False)
        self.s_sexEdit.setPlaceholderText("")
        self.s_sexEdit.setObjectName("s_sexEdit")
        self.horizontalLayout_37.addWidget(self.s_sexEdit)
        self.horizontalLayout_37.setStretch(0, 2)
        self.horizontalLayout_37.setStretch(1, 4)
        self.horizontalLayoutWidget_36 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_36.setGeometry(QtCore.QRect(690, 280, 271, 31))
        self.horizontalLayoutWidget_36.setObjectName("horizontalLayoutWidget_36")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_36)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_66 = QtWidgets.QLabel(self.horizontalLayoutWidget_36)
        self.label_66.setMinimumSize(QtCore.QSize(50, 0))
        self.label_66.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_38.addWidget(self.label_66)
        self.s_telEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_36)
        self.s_telEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s_telEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.s_telEdit.setReadOnly(False)
        self.s_telEdit.setObjectName("s_telEdit")
        self.horizontalLayout_38.addWidget(self.s_telEdit)
        self.horizontalLayout_38.setStretch(0, 2)
        self.horizontalLayout_38.setStretch(1, 4)
        self.horizontalLayoutWidget_37 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_37.setGeometry(QtCore.QRect(690, 380, 271, 31))
        self.horizontalLayoutWidget_37.setObjectName("horizontalLayoutWidget_37")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_37)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_70 = QtWidgets.QLabel(self.horizontalLayoutWidget_37)
        self.label_70.setMinimumSize(QtCore.QSize(50, 0))
        self.label_70.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_70.setObjectName("label_70")
        self.horizontalLayout_39.addWidget(self.label_70)
        self.s_birthEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_37)
        self.s_birthEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s_birthEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.s_birthEdit.setObjectName("s_birthEdit")
        self.horizontalLayout_39.addWidget(self.s_birthEdit)
        self.horizontalLayout_39.setStretch(0, 2)
        self.horizontalLayout_39.setStretch(1, 4)
        self.horizontalLayoutWidget_38 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_38.setGeometry(QtCore.QRect(0, 0, 981, 61))
        self.horizontalLayoutWidget_38.setObjectName("horizontalLayoutWidget_38")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_38)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.title1_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_38)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.title1_4.setFont(font)
        self.title1_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(35, 31, 148);")
        self.title1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.title1_4.setObjectName("title1_4")
        self.horizontalLayout_40.addWidget(self.title1_4)
        self.s_modifyButton = QtWidgets.QPushButton(self.frame)
        self.s_modifyButton.setGeometry(QtCore.QRect(890, 510, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.s_modifyButton.setFont(font)
        self.s_modifyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s_modifyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.s_modifyButton.setObjectName("s_modifyButton")
        self.s_tableWidget = QtWidgets.QTableWidget(self.frame)
        self.s_tableWidget.setGeometry(QtCore.QRect(20, 100, 651, 421))
        self.s_tableWidget.setObjectName("s_tableWidget")
        self.s_tableWidget.setColumnCount(0)
        self.s_tableWidget.setRowCount(0)
        self.s_addButton = QtWidgets.QPushButton(self.frame)
        self.s_addButton.setGeometry(QtCore.QRect(690, 510, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.s_addButton.setFont(font)
        self.s_addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s_addButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.s_addButton.setObjectName("s_addButton")
        self.s_deleteButton = QtWidgets.QPushButton(self.frame)
        self.s_deleteButton.setGeometry(QtCore.QRect(150, 540, 381, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.s_deleteButton.setFont(font)
        self.s_deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s_deleteButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.s_deleteButton.setObjectName("s_deleteButton")
        self.horizontalLayoutWidget_39 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_39.setGeometry(QtCore.QRect(690, 430, 271, 31))
        self.horizontalLayoutWidget_39.setObjectName("horizontalLayoutWidget_39")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_39)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_71 = QtWidgets.QLabel(self.horizontalLayoutWidget_39)
        self.label_71.setMinimumSize(QtCore.QSize(50, 0))
        self.label_71.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_41.addWidget(self.label_71)
        self.s_classEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_39)
        self.s_classEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s_classEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.s_classEdit.setObjectName("s_classEdit")
        self.horizontalLayout_41.addWidget(self.s_classEdit)
        self.horizontalLayout_41.setStretch(0, 2)
        self.horizontalLayout_41.setStretch(1, 4)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(680, 100, 291, 481))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.s_searchButton = QtWidgets.QPushButton(self.frame)
        self.s_searchButton.setGeometry(QtCore.QRect(790, 510, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.s_searchButton.setFont(font)
        self.s_searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s_searchButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.s_searchButton.setObjectName("s_searchButton")
        self.label_5.raise_()
        self.horizontalLayoutWidget_32.raise_()
        self.horizontalLayoutWidget_33.raise_()
        self.horizontalLayoutWidget_34.raise_()
        self.horizontalLayoutWidget_35.raise_()
        self.horizontalLayoutWidget_36.raise_()
        self.horizontalLayoutWidget_37.raise_()
        self.horizontalLayoutWidget_38.raise_()
        self.s_modifyButton.raise_()
        self.s_tableWidget.raise_()
        self.s_addButton.raise_()
        self.s_deleteButton.raise_()
        self.horizontalLayoutWidget_39.raise_()
        self.s_searchButton.raise_()
        student_manage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(student_manage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        student_manage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(student_manage)
        self.statusbar.setObjectName("statusbar")
        student_manage.setStatusBar(self.statusbar)
        self.s_modifyButton.clicked.connect(self.s_modify)
        self.s_deleteButton.clicked.connect(self.s_delete)
        self.s_addButton.clicked.connect(self.s_add)
        self.s_searchButton.clicked.connect(self.s_search)
        self.s_tableWidget.itemClicked.connect(self.s_getItem)
        self.s_show()

        self.retranslateUi(student_manage)
        QtCore.QMetaObject.connectSlotsByName(student_manage)

    def retranslateUi(self, student_manage):
        _translate = QtCore.QCoreApplication.translate
        student_manage.setWindowTitle(_translate("student_manage", "学生管理"))
        self.label_39.setText(_translate("student_manage", "学号："))
        self.label_41.setText(_translate("student_manage", "姓名："))
        self.label_43.setText(_translate("student_manage", "邮箱："))
        self.label_64.setText(_translate("student_manage", "性别："))
        self.label_66.setText(_translate("student_manage", "电话："))
        self.label_70.setText(_translate("student_manage", "生日："))
        self.title1_4.setText(_translate("student_manage", "学生信息管理"))
        self.s_modifyButton.setText(_translate("student_manage", "修改"))
        self.s_addButton.setText(_translate("student_manage", "增加"))
        self.s_searchButton.setText(_translate("student_manage", "查询"))
        self.s_deleteButton.setText(_translate("student_manage", "删         除"))
        self.label_71.setText(_translate("student_manage", "系别："))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def s_getItem(self, item):
        QMessageBox.information(None, '注意', '请认真阅读！\n请在表中单击需要修改或删除的学生学号，修改信息按学号进行，学号不能修改！！！', QMessageBox.Ok)
        if item.column() == 0:
            self.select = item.text()
            self.s_idEdit.setText(self.select)

    def s_show(self):
        self.s_tableWidget.setRowCount(0)
        result = service.query("select * from student")
        row = len(result)
        self.s_tableWidget.setRowCount(row)
        self.s_tableWidget.setColumnCount(7)
        self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
        for i in range(row):
            for j in range(self.s_tableWidget.columnCount()):
                data = QTableWidgetItem(str(result[i][j]))
                self.s_tableWidget.setItem(i, j, data)

    def s_search(self):
        name = self.s_nameEdit.text()
        sex = self.s_sexEdit.text()
        id = self.s_idEdit.text()
        tel = self.s_telEdit.text()
        mail = self.s_mailEdit.text()
        birth = self.s_birthEdit.text()
        department = self.s_classEdit.text()
        a = 0
        if name != "":
            a = a+1
        if sex != "":
            a = a+1
        if id != "":
            a = a+1
        if tel != "":
            a = a+1
        if mail != "":
            a = a+1
        if birth != "":
            a = a+1
        if department != "":
            a = a+1

        if a==0:
            QMessageBox.information(None, '注意', '您未输入查询内容！',QMessageBox.Ok)
        elif a==1:
            if tel != "":
                self.s_tableWidget.setRowCount(0)
                result = service.query("select * from student where tel=%s", tel)
                row = len(result)
                self.s_tableWidget.setRowCount(row)
                self.s_tableWidget.setColumnCount(7)
                self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
                for i in range(row):
                    for j in range(self.s_tableWidget.columnCount()):
                        data = QTableWidgetItem(str(result[i][j]))
                        self.s_tableWidget.setItem(i, j, data)
            if mail != "":
                self.s_tableWidget.setRowCount(0)
                result = service.query("select * from student where mail=%s", mail)
                row = len(result)
                self.s_tableWidget.setRowCount(row)
                self.s_tableWidget.setColumnCount(7)
                self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
                for i in range(row):
                    for j in range(self.s_tableWidget.columnCount()):
                        data = QTableWidgetItem(str(result[i][j]))
                        self.s_tableWidget.setItem(i, j, data)
            if birth != "":
                self.s_tableWidget.setRowCount(0)
                result = service.query("select * from student where birthday=%s", birth)
                row = len(result)
                self.s_tableWidget.setRowCount(row)
                self.s_tableWidget.setColumnCount(7)
                self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
                for i in range(row):
                    for j in range(self.s_tableWidget.columnCount()):
                        data = QTableWidgetItem(str(result[i][j]))
                        self.s_tableWidget.setItem(i, j, data)
            if name != "":
                self.s_tableWidget.setRowCount(0)
                result = service.query("select * from student where sname=%s", name)
                row = len(result)
                self.s_tableWidget.setRowCount(row)
                self.s_tableWidget.setColumnCount(7)
                self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
                for i in range(row):
                    for j in range(self.s_tableWidget.columnCount()):
                        data = QTableWidgetItem(str(result[i][j]))
                        self.s_tableWidget.setItem(i, j, data)
            if sex != "":
                self.s_tableWidget.setRowCount(0)
                result = service.query("select * from student where sex=%s", sex)
                row = len(result)
                self.s_tableWidget.setRowCount(row)
                self.s_tableWidget.setColumnCount(7)
                self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
                for i in range(row):
                    for j in range(self.s_tableWidget.columnCount()):
                        data = QTableWidgetItem(str(result[i][j]))
                        self.s_tableWidget.setItem(i, j, data)
            if department != "":
                self.s_tableWidget.setRowCount(0)
                result = service.query("select * from student where department=%s", department)
                row = len(result)
                self.s_tableWidget.setRowCount(row)
                self.s_tableWidget.setColumnCount(7)
                self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
                for i in range(row):
                    for j in range(self.s_tableWidget.columnCount()):
                        data = QTableWidgetItem(str(result[i][j]))
                        self.s_tableWidget.setItem(i, j, data)
            if id != "":
                self.s_tableWidget.setRowCount(0)
                result = service.query("select * from student where sno=%s", id)
                row = len(result)
                self.s_tableWidget.setRowCount(row)
                self.s_tableWidget.setColumnCount(7)
                self.s_tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '系别', '性别', '电话', '邮箱', '生日'])
                for i in range(row):
                    for j in range(self.s_tableWidget.columnCount()):
                        data = QTableWidgetItem(str(result[i][j]))
                        self.s_tableWidget.setItem(i, j, data)
        else:
            QMessageBox.information(None, '注意', '只能输入一项信息进行筛选查询！', QMessageBox.Ok)


    def s_modify(self):
        name = self.s_nameEdit.text()
        sex = self.s_sexEdit.text()
        id = self.s_idEdit.text()
        tel = self.s_telEdit.text()
        mail = self.s_mailEdit.text()
        birth = self.s_birthEdit.text()
        department = self.s_classEdit.text()
        if id != "":
            if tel != "" or mail != "" or birth != "" or name != "" or sex != "" or department != "":
                if tel != "":
                    service.exec("update student set tel=%s where sno=%s", (tel, id))
                if mail != "":
                    service.exec("update student set mail=%s where sno=%s", (mail, id))
                if birth != "":
                    service.exec("update student set birthday=%s where sno=%s", (birth, id))
                if name != "":
                    service.exec("update student set sname=%s where sno=%s", (name, id))
                if sex != "":
                    service.exec("update student set sex=%s where sno=%s", (sex, id))
                if department != "":
                    service.exec("update student set department=%s where sno=%s", (department, id))
            else:
                QMessageBox.information(None, '注意', '您未输入修改内容！',QMessageBox.Ok)
        else:
            QMessageBox.information(None, '注意', '您未输入学号\n请在表中单击需要修改或删除的学生学号，修改信息按学号进行，学号不能修改！！！',
                                    QMessageBox.Ok)
        self.s_show()

    def s_delete(self):
        id = self.s_idEdit.text()
        if id != "":
            result = service.exec("delete from student where sno=%s", id)
            if result > 0:
                self.s_show()
                QMessageBox.information(None, '提示', '删除成功！', QMessageBox.Ok)
            else:
                QMessageBox.warning(None, '警告', '删除失败，请检查学号是否正确!', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '学号不能为空！', QMessageBox.Ok)

    def s_add(self):
        sname = self.s_nameEdit.text()
        sex = self.s_sexEdit.text()
        sno = self.s_idEdit.text()
        tel = self.s_telEdit.text()
        mail = self.s_mailEdit.text()
        birth = self.s_birthEdit.text()
        department = self.s_classEdit.text()
        result = service.query("select * from student where sno=%s", sno)
        if len(result) > 0:
            QMessageBox.information(None, '警告', '该学号已存在，请核对后输入！', QMessageBox.Ok)
        else:
            result = service.exec("""insert into student(sno,sname,department,sex,tel,mail,birthday)
                            values(%s,%s,%s,%s,%s,%s,%s)""", (sno, sname, department, sex, tel, mail, birth))
            if result > 0:
                self.s_show()
                QMessageBox.information(None, '提示', '添加成功', QMessageBox.Ok)
            else:
                QMessageBox.information(None, '提示', '添加失败，请检查是否完整填入信息！', QMessageBox.Ok)

    import pic