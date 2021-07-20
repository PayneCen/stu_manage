# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from service import service

class Ui_course_manage(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_course_manage,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, course_manage):
        course_manage.setObjectName("course_manage")
        course_manage.resize(1300, 700)
        course_manage.setMinimumSize(QtCore.QSize(1300, 700))
        course_manage.setMaximumSize(QtCore.QSize(1300, 700))
        self.center()
        self.centralwidget = QtWidgets.QWidget(course_manage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1300, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/img/pix.jpg"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(160, 10, 980, 650))
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 230);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.title3_2 = QtWidgets.QLabel(self.frame_5)
        self.title3_2.setGeometry(QtCore.QRect(1, 1, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title3_2.setFont(font)
        self.title3_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(35, 31, 148);")
        self.title3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title3_2.setObjectName("title3_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setGeometry(QtCore.QRect(10, 340, 471, 260))
        self.frame_8.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.cnoAdd = QtWidgets.QLineEdit(self.frame_8)
        self.cnoAdd.setGeometry(QtCore.QRect(141, 60, 211, 31))
        self.cnoAdd.setObjectName("cnoAdd")
        self.label_54 = QtWidgets.QLabel(self.frame_8)
        self.label_54.setGeometry(QtCore.QRect(61, 60, 71, 31))
        self.label_54.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_54.setObjectName("label_54")
        self.cnameAdd = QtWidgets.QLineEdit(self.frame_8)
        self.cnameAdd.setGeometry(QtCore.QRect(141, 110, 211, 31))
        self.cnameAdd.setObjectName("cnameAdd")
        self.label_55 = QtWidgets.QLabel(self.frame_8)
        self.label_55.setGeometry(QtCore.QRect(61, 110, 71, 31))
        self.label_55.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_55.setObjectName("label_55")
        self.c_addButton = QtWidgets.QPushButton(self.frame_8)
        self.c_addButton.setGeometry(QtCore.QRect(140, 210, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.c_addButton.setFont(font)
        self.c_addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_addButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.c_addButton.setObjectName("c_addButton")
        self.label_56 = QtWidgets.QLabel(self.frame_8)
        self.label_56.setGeometry(QtCore.QRect(0, 0, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"color: rgb(255, 255, 255);")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.label_62 = QtWidgets.QLabel(self.frame_8)
        self.label_62.setGeometry(QtCore.QRect(60, 160, 71, 31))
        self.label_62.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_62.setObjectName("label_62")
        self.creditAdd = QtWidgets.QSpinBox(self.frame_8)
        self.creditAdd.setGeometry(QtCore.QRect(141, 160, 211, 31))
        self.creditAdd.setObjectName("creditAdd")
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setGeometry(QtCore.QRect(9, 42, 961, 281))
        self.frame_9.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_60 = QtWidgets.QLabel(self.frame_9)
        self.label_60.setGeometry(QtCore.QRect(0, 0, 41, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"color: rgb(255, 255, 255);")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.c_modifyButton = QtWidgets.QPushButton(self.frame_9)
        self.c_modifyButton.setGeometry(QtCore.QRect(700, 230, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.c_modifyButton.setFont(font)
        self.c_modifyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_modifyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.c_modifyButton.setObjectName("c_modifyButton")
        self.label_57 = QtWidgets.QLabel(self.frame_9)
        self.label_57.setGeometry(QtCore.QRect(620, 100, 71, 31))
        self.label_57.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.frame_9)
        self.label_58.setGeometry(QtCore.QRect(620, 30, 71, 31))
        self.label_58.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_58.setObjectName("label_58")
        self.cnameModify = QtWidgets.QLineEdit(self.frame_9)
        self.cnameModify.setGeometry(QtCore.QRect(700, 100, 211, 31))
        self.cnameModify.setObjectName("cnameModify")
        self.label_59 = QtWidgets.QLabel(self.frame_9)
        self.label_59.setGeometry(QtCore.QRect(620, 170, 71, 31))
        self.label_59.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_59.setObjectName("label_59")
        self.c_tableWidget = QtWidgets.QTableWidget(self.frame_9)
        self.c_tableWidget.setGeometry(QtCore.QRect(50, 10, 521, 261))
        self.c_tableWidget.setObjectName("c_tableWidget")
        self.c_tableWidget.setColumnCount(0)
        self.c_tableWidget.setRowCount(0)
        self.cnoModify = QtWidgets.QLineEdit(self.frame_9)
        self.cnoModify.setGeometry(QtCore.QRect(700, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cnoModify.setFont(font)
        self.cnoModify.setAlignment(QtCore.Qt.AlignCenter)
        self.cnoModify.setObjectName("cnoModify")
        self.creditModify = QtWidgets.QSpinBox(self.frame_9)
        self.creditModify.setGeometry(QtCore.QRect(700, 170, 211, 31))
        self.creditModify.setObjectName("creditModify")
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setGeometry(QtCore.QRect(510, 340, 461, 260))
        self.frame_10.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_61 = QtWidgets.QLabel(self.frame_10)
        self.label_61.setGeometry(QtCore.QRect(0, 0, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"color: rgb(255, 255, 255);")
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.c_deleteButton = QtWidgets.QPushButton(self.frame_10)
        self.c_deleteButton.setGeometry(QtCore.QRect(130, 210, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.c_deleteButton.setFont(font)
        self.c_deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_deleteButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.c_deleteButton.setObjectName("c_deleteButton")
        self.course_comboBox = QtWidgets.QComboBox(self.frame_10)
        self.course_comboBox.setGeometry(QtCore.QRect(40, 100, 391, 32))
        self.course_comboBox.setObjectName("course_comboBox")
        course_manage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(course_manage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        course_manage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(course_manage)
        self.statusbar.setObjectName("statusbar")
        course_manage.setStatusBar(self.statusbar)
        self.c_modifyButton.clicked.connect(self.c_modify)
        self.c_deleteButton.clicked.connect(self.c_delete)
        self.c_addButton.clicked.connect(self.c_add)
        self.c_tableWidget.itemClicked.connect(self.c_getItem)
        self.course_combo()
        self.c_show()

        self.retranslateUi(course_manage)
        QtCore.QMetaObject.connectSlotsByName(course_manage)

    def retranslateUi(self, course_manage):
            _translate = QtCore.QCoreApplication.translate
            course_manage.setWindowTitle(_translate("course_manage", "课程管理"))
            self.title3_2.setText(_translate("course_manage", "课程信息管理"))
            self.label_54.setText(_translate("course_manage", "课程号："))
            self.label_55.setText(_translate("course_manage", "课程名："))
            self.c_addButton.setText(_translate("course_manage", "添      加"))
            self.label_56.setText(_translate("course_manage", "课程添加"))
            self.label_62.setText(_translate("course_manage", "学   分："))
            self.label_60.setText(_translate("course_manage", "课\n"
                                                              "程\n"
                                                              "信\n"
                                                              "息\n"
                                                              "修\n"
                                                              "改"))
            self.c_modifyButton.setText(_translate("course_manage", "修  改"))
            self.label_57.setText(_translate("course_manage", "课程名："))
            self.label_58.setText(_translate("course_manage", "课程号："))
            self.label_59.setText(_translate("course_manage", "学   分："))
            self.cnoModify.setPlaceholderText(_translate("course_manage", "请在列表中点击课程号选择"))
            self.label_61.setText(_translate("course_manage", "删除课程"))
            self.c_deleteButton.setText(_translate("course_manage", "删      除"))

    def center(self):
            screen = QDesktopWidget().screenGeometry()
            size = self.geometry()
            self.move((screen.width() - size.width()) / 2,
                      (screen.height() - size.height()) / 2)

    def c_getItem(self, item):
            if item.column() == 0:
                    self.select = item.text()
                    self.cnoModify.setText(self.select)

    def course_combo(self):
            self.course_comboBox.clear()
            result = service.query("select cname from course")
            row = len(result)
            for i in range(row):
                    data = str(result[i])
                    data = data.strip("()',")
                    self.course_comboBox.addItem(data)

    def c_show(self):
            self.c_tableWidget.setRowCount(0)
            result = service.query("select * from course")
            row = len(result)
            self.c_tableWidget.setRowCount(row)
            self.c_tableWidget.setColumnCount(3)
            self.c_tableWidget.setHorizontalHeaderLabels(['课程号', '课程名', '学分'])
            for i in range(row):
                    for j in range(self.c_tableWidget.columnCount()):
                            data = QTableWidgetItem(str(result[i][j]))
                            self.c_tableWidget.setItem(i, j, data)

    def c_modify(self):
            cno = self.cnoModify.text()
            cname = self.cnameModify.text()
            credit = self.creditModify.value()
            if cno != "":
                    if cname != "" or credit != 0:
                            if cname != "":
                                    service.exec("update course set cname=%s where cno=%s", (cname, cno))
                            if credit != "":
                                    service.exec("update course set credit=%s where cno=%s", (credit, cno))
                    else:
                            QMessageBox.information(None, '注意', '您未输入修改内容！', QMessageBox.Ok)
            else:
                    QMessageBox.information(None, '注意', '您未选择课程号\n请在表中单击需要修改的课程号！',
                                            QMessageBox.Ok)
            self.c_show()
            self.course_combo()

    def c_add(self):
            cno = self.cnoAdd.text()
            cname = self.cnameAdd.text()
            credit = self.creditAdd.value()
            result = service.query("select * from course where cno=%s", cno)
            if len(result) > 0:
                    QMessageBox.information(None, '警告', '该课程号已存在，请核对后输入！', QMessageBox.Ok)
            else:
                    if credit > 0:
                            result = service.exec("""insert into course(cno,cname,credit)
                                                                            values(%s,%s,%s)""",
                                                  (cno, cname, credit))
                            if result > 0:
                                    self.c_show()
                                    QMessageBox.information(None, '提示', '添加成功', QMessageBox.Ok)
                            else:
                                    QMessageBox.information(None, '提示', '添加失败，请检查是否完整填入信息！', QMessageBox.Ok)
                    else:
                            QMessageBox.information(None, '提示', '课程学分不能为 0 ！', QMessageBox.Ok)
            self.course_combo()


    def c_delete(self):
            cname = self.course_comboBox.currentText()
            cno = service.query("select cno from course where cname=%s", cname)
            cno = str(cno)
            cno = cno.strip("()',")
            result = service.exec("delete from course where cno=%s", (cno))
            if result > 0:
                    QMessageBox.information(None, '提示', '课程已删除！', QMessageBox.Ok)
            else:
                    QMessageBox.information(None, '提示', '课程删除失败！', QMessageBox.Ok)
            self.c_show()
            self.course_combo()

    import pic
