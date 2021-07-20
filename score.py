# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from service import service
import pymysql


class Ui_score(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_score,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, score):
        score.setObjectName("score")
        score.resize(1300, 700)
        score.setMinimumSize(QtCore.QSize(1300, 700))
        score.setMaximumSize(QtCore.QSize(1300, 700))
        self.centralwidget = QtWidgets.QWidget(score)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1300, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/img/pix.jpg"))
        self.label.setObjectName("label")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(160, 10, 980, 650))
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 230);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayoutWidget_19 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_19.setGeometry(QtCore.QRect(0, 0, 981, 61))
        self.horizontalLayoutWidget_19.setObjectName("horizontalLayoutWidget_19")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.title3 = QtWidgets.QLabel(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title3.setFont(font)
        self.title3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(94, 0, 100);")
        self.title3.setAlignment(QtCore.Qt.AlignCenter)
        self.title3.setObjectName("title3")
        self.horizontalLayout_21.addWidget(self.title3)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 421, 231))
        self.tableWidget.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setGeometry(QtCore.QRect(10, 371, 350, 241))
        self.frame_6.setStyleSheet("background-color: rgba(255, 255, 255, 179);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.add_idEdit = QtWidgets.QLineEdit(self.frame_6)
        self.add_idEdit.setGeometry(QtCore.QRect(80, 70, 231, 31))
        self.add_idEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.add_idEdit.setObjectName("add_idEdit")
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 61, 31))
        self.label_21.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.label_20.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.add_scoreEdit = QtWidgets.QLineEdit(self.frame_6)
        self.add_scoreEdit.setGeometry(QtCore.QRect(80, 120, 231, 31))
        self.add_scoreEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.add_scoreEdit.setObjectName("add_scoreEdit")
        self.label_37 = QtWidgets.QLabel(self.frame_6)
        self.label_37.setGeometry(QtCore.QRect(10, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(94, 0, 100);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.addButton = QtWidgets.QPushButton(self.frame_6)
        self.addButton.setGeometry(QtCore.QRect(35, 180, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.addButton.setObjectName("addButton")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setGeometry(QtCore.QRect(460, 370, 350, 241))
        self.frame_7.setStyleSheet("background-color: rgba(255, 255, 255, 179);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.modi_idEdit = QtWidgets.QLineEdit(self.frame_7)
        self.modi_idEdit.setGeometry(QtCore.QRect(80, 70, 231, 31))
        self.modi_idEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modi_idEdit.setObjectName("modi_idEdit")
        self.label_33 = QtWidgets.QLabel(self.frame_7)
        self.label_33.setGeometry(QtCore.QRect(10, 120, 61, 31))
        self.label_33.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_7)
        self.label_34.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.label_34.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.modi_scoreEdit = QtWidgets.QLineEdit(self.frame_7)
        self.modi_scoreEdit.setGeometry(QtCore.QRect(80, 120, 231, 31))
        self.modi_scoreEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modi_scoreEdit.setObjectName("modi_scoreEdit")
        self.label_38 = QtWidgets.QLabel(self.frame_7)
        self.label_38.setGeometry(QtCore.QRect(10, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(94, 0, 100);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.modifyButton = QtWidgets.QPushButton(self.frame_7)
        self.modifyButton.setGeometry(QtCore.QRect(35, 180, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.modifyButton.setFont(font)
        self.modifyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modifyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.modifyButton.setObjectName("modifyButton")
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(170, 320, 261, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgba(255, 255, 255, 110);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_36 = QtWidgets.QLabel(self.frame_4)
        self.label_36.setGeometry(QtCore.QRect(10, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(94, 0, 100);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setGeometry(QtCore.QRect(460, 80, 351, 231))
        self.frame_8.setStyleSheet("background-color: rgba(255, 255, 255, 179);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.snoEdit = QtWidgets.QLineEdit(self.frame_8)
        self.snoEdit.setGeometry(QtCore.QRect(80, 70, 231, 31))
        self.snoEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.snoEdit.setObjectName("snoEdit")
        self.label_35 = QtWidgets.QLabel(self.frame_8)
        self.label_35.setGeometry(QtCore.QRect(10, 120, 61, 31))
        self.label_35.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.label_39 = QtWidgets.QLabel(self.frame_8)
        self.label_39.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.label_39.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_8)
        self.label_40.setGeometry(QtCore.QRect(10, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(94, 0, 100);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.searchButton = QtWidgets.QPushButton(self.frame_8)
        self.searchButton.setGeometry(QtCore.QRect(35, 180, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.searchButton.setFont(font)
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.searchButton.setObjectName("searchButton")
        self.scoreShow = QtWidgets.QLabel(self.frame_8)
        self.scoreShow.setGeometry(QtCore.QRect(80, 120, 261, 31))
        self.scoreShow.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.scoreShow.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreShow.setObjectName("scoreShow")
        self.export_1 = QtWidgets.QPushButton(self.frame_4)
        self.export_1.setGeometry(QtCore.QRect(820, 80, 31, 531))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.export_1.setFont(font)
        self.export_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);")
        self.export_1.setObjectName("export_1")

        self.export_2 = QtWidgets.QPushButton(self.frame_4)
        self.export_2.setGeometry(QtCore.QRect(860, 80, 31, 531))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.export_2.setFont(font)
        self.export_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);")
        self.export_2.setObjectName("export_2")
        self.export_3 = QtWidgets.QPushButton(self.frame_4)
        self.export_3.setGeometry(QtCore.QRect(900, 80, 31, 531))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.export_3.setFont(font)
        self.export_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);")
        self.export_3.setObjectName("export_3")
        self.export_4 = QtWidgets.QPushButton(self.frame_4)
        self.export_4.setGeometry(QtCore.QRect(940, 80, 31, 531))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.export_4.setFont(font)
        self.export_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);")
        self.export_4.setObjectName("export_4")
        score.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(score)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        score.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(score)
        self.statusbar.setObjectName("statusbar")
        score.setStatusBar(self.statusbar)
        self.combo()
        self.addButton.clicked.connect(self.add)
        self.modifyButton.clicked.connect(self.modify)
        self.searchButton.clicked.connect(self.search)
        self.export_1.clicked.connect(self.export_a)
        self.export_2.clicked.connect(self.export_b)
        self.export_3.clicked.connect(self.export_c)
        self.export_4.clicked.connect(self.export_d)

        self.retranslateUi(score)
        QtCore.QMetaObject.connectSlotsByName(score)

    def retranslateUi(self, score):
        _translate = QtCore.QCoreApplication.translate
        score.setWindowTitle(_translate("score", "成绩评定"))
        self.title3.setText(_translate("score", "成绩评定"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("score", "请在下方选择课程！！！"))
        self.label_21.setText(_translate("score", "成   绩："))
        self.label_20.setText(_translate("score", "学   号："))
        self.label_37.setText(_translate("score", "成绩录入"))
        self.addButton.setText(_translate("score", "录      入"))
        self.label_33.setText(_translate("score", "成   绩："))
        self.label_34.setText(_translate("score", "学   号："))
        self.label_38.setText(_translate("score", "成绩修改"))
        self.modifyButton.setText(_translate("score", "修      改"))
        self.comboBox.setItemText(0, _translate("score", "-"))
        self.label_36.setText(_translate("score", "请在此选择课程名："))
        self.label_35.setText(_translate("score", "绩   点："))
        self.label_39.setText(_translate("score", "学   号："))
        self.label_40.setText(_translate("score", "成绩评定"))
        self.searchButton.setText(_translate("score", "绩点查询"))
        self.scoreShow.setText(_translate("score", "- -"))
        self.export_1.setText(_translate("score", "点\n"
"击\n"
"此\n"
"处\n"
"导\n"
"出\n"
"所\n"
"有\n"
"学\n"
"生\n"
"选\n"
"课\n"
"情\n"
"况"))
        self.export_2.setText(_translate("score", "点\n"
"击\n"
"此\n"
"处\n"
"导\n"
"出\n"
"所\n"
"有\n"
"学\n"
"生\n"
"所\n"
"有\n"
"成\n"
"绩"))
        self.export_3.setText(_translate("score", "点\n"
"击\n"
"此\n"
"处\n"
"导\n"
"出\n"
"已\n"
"选\n"
"课\n"
"程\n"
"选\n"
"课\n"
"信\n"
"息"))
        self.export_4.setText(_translate("score", "点\n"
"击\n"
"此\n"
"处\n"
"导\n"
"出\n"
"学\n"
"分\n"
"不\n"
"足\n"
"学\n"
"生\n"
"名\n"
"单"))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def grade(self, text):
        cname = text
        self.tableWidget.setRowCount(0)
        result = service.query("""
            select course.cno, course.cname, student.sno, student.sname, selection.score
            from course, selection, student
            where selection.cno= course.cno
            and student.sno= selection.sno
            and course.cname= %s
            """, cname)
        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['课程号', '课程名', '学号', '姓名', '成绩'])
        for i in range(row):
            for j in range(self.tableWidget.columnCount()):
                data = QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)

    def combo(self):
        self.comboBox.clear()
        result = service.query("select course.cname from course")
        row = len(result)
        for i in range(row):
            data = str(result[i])
            data = data.strip("()',")
            self.comboBox.addItem(data)
        self.comboBox.activated[str].connect(self.grade)

    def add(self):
        cname = self.comboBox.currentText()
        id = self.add_idEdit.text()
        score = self.add_scoreEdit.text()
        result = service.query("""
            select selection.score from selection, course
            where course.cname= %s
            and selection.sno= %s
            and course.cno= selection.cno
            """, cname, id)
        a = str(result)
        a = a.strip("()',")
        if len(result) > 0 and a != 'None':
            QMessageBox.warning(None, '警告', '该学生已有成绩!', QMessageBox.Ok)
        else:
            cno = service.query("select cno from course where cname=%s", cname)
            cno = str(cno)
            cno = cno.strip("()',")
            result = service.exec("""
                    update selection set score=%s
                    where cno=%s
                    and sno=%s
                    """, (score, cno, id))
            if result > 0:
                self.grade(cname)
                QMessageBox.information(None, "提示", "添加成功！", QMessageBox.Ok)
            else:
                QMessageBox.warning(None, "警告", "添加失败，请检查输入！", QMessageBox.Ok)

    def modify(self):
        cname = self.comboBox.currentText()
        id = self.modi_idEdit.text()
        score = self.modi_scoreEdit.text()
        result = service.query("""
                        select selection.score from selection, course
                        where course.cname= %s
                        and selection.sno= %s
                        and course.cno= selection.cno
                        """, cname, id)
        a = str(result)
        a = a.strip("()',")
        if len(result) > 0 and a != 'None':
            cno = service.query("select cno from course where cname=%s", cname)
            cno = str(cno)
            cno = cno.strip("()',")
            result = service.exec("""
                                                    update selection set score=%s
                                                    where cno=%s
                                                    and sno=%s
                                                    """, (score, cno, id))
            if result > 0:
                self.grade(cname)
                QMessageBox.information(None, "提示", "修改成功！", QMessageBox.Ok)
            else:
                QMessageBox.warning(None, "警告", "修改失败，请检查输入！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '该学生没有成绩，修改失败!', QMessageBox.Ok)

    def search(self):
        sno = self.snoEdit.text()
        a = service.query("""select sum(credit) 
        from course,selection 
        where sno=%s 
        and course.cno=selection.cno
        and selection.score is not null """, sno)
        a = str(a)
        a = a.strip("Decimal('()',")
        a = int(a)
        b = service.query("""
        select sum((course.credit * ((selection.score/10)-5))) 
        from course,selection 
        where course.cno = selection.cno
        and selection.sno=%s
        """, sno)
        b = str(b)
        b = b.strip("Decimal('(),")
        b = float(b)
        c = b / a
        c = float(c)
        c = format(c, '.2f')
        self.scoreShow.setText(c)

    def export_a(self):
        service.export_a("""
        select selection.sno,selection.cno,sname,cname,credit,score
        from selection,student,course
        where student.sno = selection.sno
        and course.cno = selection.cno
        """)
        result = service.query("""
                select selection.sno,selection.cno,sname,cname,credit,score
                from selection,student,course
                where student.sno = selection.sno
                and course.cno = selection.cno
                """)
        if len(result) > 0:
            QMessageBox.information(None, "提示", "信息已导出，请查看！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '信息失败，请检查!', QMessageBox.Ok)

    def export_b(self):
        service.export_b("""
        select selection.sno,sname,ifnull(avg(score),0)
        from selection,student,course
        where student.sno = selection.sno
        group by sno;""")
        result = service.query("""
        select selection.sno,sname,ifnull(avg(score),0)
        from selection,student,course
        where student.sno = selection.sno
        group by sno;""")
        if len(result) > 0:
            QMessageBox.information(None, "提示", "信息已导出，请查看！", QMessageBox.Ok)

    def export_c(self):
        cname = self.comboBox.currentText()
        service.course_name = cname
        if cname == "-":
            QMessageBox.information(None, "提示", "请在左侧选择课程！", QMessageBox.Ok)
        else:
            service.export_c("""
                                    select student.sno, student.sname
                                    from course, selection, student
                                    where selection.cno= course.cno
                                    and student.sno= selection.sno
                                    and course.cname= %s
                                    """, cname)
            result = service.query("""
                        select student.sno, student.sname
                        from course, selection, student
                        where selection.cno= course.cno
                        and student.sno= selection.sno
                        and course.cname= %s
                        """, cname)
            if len(result) > 0:
                QMessageBox.information(None, "提示", "信息已导出，请查看！", QMessageBox.Ok)

    def export_d(self):
        service.export_d("""
        select student.sname,student.sno
        from student , course , selection
        where student.sno = selection.sno and selection.cno = course.cno
        group by student.sno
        having sum(course.credit) < 30
                """)
        QMessageBox.information(None, "提示", "信息已导出，请查看！", QMessageBox.Ok)

# service.export_d("""
# select student.sname from student
# left join selection on student.sno = selection.cno
# left join course on selection.cno = course.cno
# group by student.sname
# having sum(ifnull(course.credit,0)) < 30
#                 """)

import pic

