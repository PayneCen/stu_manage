# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from service import service

class Ui_selection(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_selection,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, selection):
        selection.setObjectName("selection")
        selection.resize(1300, 700)
        selection.setMinimumSize(QtCore.QSize(1300, 700))
        selection.setMaximumSize(QtCore.QSize(1300, 700))
        self.center()
        self.centralwidget = QtWidgets.QWidget(selection)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1300, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/img/pix.jpg"))
        self.label.setObjectName("label")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(160, 10, 980, 650))
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 230);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayoutWidget_20 = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidget_20.setGeometry(QtCore.QRect(0, 0, 981, 61))
        self.horizontalLayoutWidget_20.setObjectName("horizontalLayoutWidget_20")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.title4 = QtWidgets.QLabel(self.horizontalLayoutWidget_20)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.title4.setFont(font)
        self.title4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(159, 25, 32);")
        self.title4.setAlignment(QtCore.Qt.AlignCenter)
        self.title4.setObjectName("title4")
        self.horizontalLayout_22.addWidget(self.title4)
        self.selectButton = QtWidgets.QPushButton(self.frame_5)
        self.selectButton.setGeometry(QtCore.QRect(160, 550, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.selectButton.setFont(font)
        self.selectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.selectButton.setObjectName("selectButton")
        self.returnButton = QtWidgets.QPushButton(self.frame_5)
        self.returnButton.setGeometry(QtCore.QRect(580, 550, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.returnButton.setFont(font)
        self.returnButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.returnButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.returnButton.setObjectName("returnButton")
        self.tableWidget1 = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget1.setGeometry(QtCore.QRect(100, 80, 521, 341))
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)
        self.tableWidget1.horizontalHeader().setDefaultSectionSize(130)
        self.snoEdit = QtWidgets.QLineEdit(self.frame_5)
        self.snoEdit.setGeometry(QtCore.QRect(370, 450, 480, 40))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.snoEdit.setFont(font)
        self.snoEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.snoEdit.setObjectName("snoEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(140, 450, 60, 41))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.cnoSelect = QtWidgets.QLabel(self.frame_5)
        self.cnoSelect.setGeometry(QtCore.QRect(220, 450, 121, 41))
        self.cnoSelect.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.cnoSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.cnoSelect.setObjectName("cnoSelect")
        self.snoShow = QtWidgets.QLabel(self.frame_5)
        self.snoShow.setGeometry(QtCore.QRect(750, 90, 121, 41))
        self.snoShow.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.snoShow.setAlignment(QtCore.Qt.AlignCenter)
        self.snoShow.setObjectName("snoShow")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(649, 90, 81, 41))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.creditShow = QtWidgets.QLabel(self.frame_5)
        self.creditShow.setGeometry(QtCore.QRect(750, 160, 121, 41))
        self.creditShow.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.creditShow.setAlignment(QtCore.Qt.AlignCenter)
        self.creditShow.setObjectName("creditShow")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(649, 160, 81, 41))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.cnoSelect_4 = QtWidgets.QLabel(self.frame_5)
        self.cnoSelect_4.setGeometry(QtCore.QRect(750, 230, 121, 41))
        self.cnoSelect_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.cnoSelect_4.setAlignment(QtCore.Qt.AlignCenter)
        self.cnoSelect_4.setObjectName("cnoSelect_4")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(649, 230, 81, 41))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        selection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(selection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        selection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(selection)
        self.statusbar.setObjectName("statusbar")
        selection.setStatusBar(self.statusbar)
        self.select_show()
        self.tableWidget1.itemClicked.connect(self.getItem)
        self.selectButton.clicked.connect(self.choose)
        self.returnButton.clicked.connect(self.drop)

        self.retranslateUi(selection)
        QtCore.QMetaObject.connectSlotsByName(selection)

    def retranslateUi(self, selection):
        _translate = QtCore.QCoreApplication.translate
        selection.setWindowTitle(_translate("selection", "学生选课"))
        self.title4.setText(_translate("selection", "选课"))
        self.selectButton.setText(_translate("selection", "选课"))
        self.returnButton.setText(_translate("selection", "退课"))
        self.snoEdit.setPlaceholderText(_translate("selection", "请选择选、退课程，并在此处输入您的学号"))
        self.label_2.setText(_translate("selection", "课程号："))
        self.cnoSelect.setText(_translate("selection", "--"))
        self.snoShow.setText(_translate("selection", "--"))
        self.label_3.setText(_translate("selection", "学       号："))
        self.creditShow.setText(_translate("selection", "--"))
        self.label_4.setText(_translate("selection", "当前学分："))
        self.cnoSelect_4.setText(_translate("selection", "30"))
        self.label_5.setText(_translate("selection", "要求学分："))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def getItem(self, item):
        if item.column() == 0:
            self.select = item.text()
            self.cnoSelect.setText(self.select)

    def select_show(self):
        self.tableWidget1.setRowCount(0)
        result = service.query("select * from course")
        row = len(result)
        self.tableWidget1.setRowCount(row)
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setHorizontalHeaderLabels(['课程号', '课程名', '学分'])
        for i in range(row):
            for j in range(self.tableWidget1.columnCount()):
                data = QTableWidgetItem(str(result[i][j]))
                self.tableWidget1.setItem(i, j, data)

    def choose(self):
        sno = self.snoEdit.text()
        cno = self.cnoSelect.text()
        self.snoShow.setText(sno)
        result = service.query("select cno from course where cno=%s", cno)
        if sno != "" and cno != "" and len(result) > 0:
            result = service.query("""
                            select * 
                            from selection
                            where sno=%s
                            and cno=%s
                            """, sno, cno)
            if len(result) > 0:
                QMessageBox.warning(None, '提示', '你已选择该课程', QMessageBox.Ok)
                credit_sum = service.query("""
                                                                        select sum(credit) 
                                                                        from selection,course
                                                                        where selection.sno=%s
                                                                        and selection.cno=course.cno
                                                                        """, sno)
                credit_sum = str(credit_sum)
                credit_sum = credit_sum.strip("DecimalNon（）()',")
                credit = int(credit_sum)
                if credit <= 30:
                    QMessageBox.warning(None, '提示', '您所选课程的学分未够30，请注意！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '提示', '您所选课程的学分已达标！', QMessageBox.Ok)
            else:
                a = service.exec("insert into selection(sno, cno) values(%s,%s)", (sno, cno))
                if a > 0:
                    credit_sum = service.query("""
                                                        select sum(credit) 
                                                        from selection,course
                                                        where selection.sno=%s
                                                        and selection.cno=course.cno
                                                        """, sno)
                    credit_sum = str(credit_sum)
                    credit_sum = credit_sum.strip("DecimalNon（）()',")
                    credit = int(credit_sum)
                    QMessageBox.information(None, '提示', '选课成功！', QMessageBox.Ok)
                    if credit <= 30:
                        QMessageBox.warning(None, '提示', '您所选课程的学分未够30，请注意！', QMessageBox.Ok)
                    else:
                        QMessageBox.warning(None, '提示', '您所选课程的学分已达标！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请检查课程号选择、学号填写是否正确！', QMessageBox.Ok)
            credit_sum = "--"
        self.creditShow.setText(credit_sum)

    def drop(self):
        sno = self.snoEdit.text()
        cno = self.cnoSelect.text()
        self.snoShow.setText(sno)
        result = service.query("select cno from course where cno=%s", cno)
        if sno != "" and cno != "" and len(result) > 0:
            result = service.query("""
                                    select * 
                                    from selection
                                    where sno=%s
                                    and cno=%s
                                    """, sno, cno)
            if len(result) > 0:
                a = service.exec("delete from selection where sno=%s and cno=%s", (sno, cno))
                if a > 0:
                    QMessageBox.information(None, '提示', '退课成功！', QMessageBox.Ok)
                    credit_sum = service.query("""
                                                                                            select sum(credit) 
                                                                                            from selection,course
                                                                                            where selection.sno=%s
                                                                                            and selection.cno=course.cno
                                                                                            """, sno)
                    credit_sum = str(credit_sum)
                    credit_sum = credit_sum.strip("DecimalNon（）()',")
                    credit = int(credit_sum)
                    if credit <= 30:
                        QMessageBox.warning(None, '提示', '您所选课程的学分未够30，请注意！', QMessageBox.Ok)
                    else:
                        QMessageBox.warning(None, '提示', '您所选课程的学分已达标！', QMessageBox.Ok)
            else:
                QMessageBox.warning(None, '提示', '未选择该课程，无法退课！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请检查课程号选择、学号填写是否正确！', QMessageBox.Ok)
            credit_sum = "--"
        self.creditShow.setText(credit_sum)
    import pic
