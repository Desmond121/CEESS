# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dev\Repo\CEESS\ui\Student.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Student(object):
    def setupUi(self, Student):
        Student.setObjectName("Student")
        Student.resize(560, 275)
        self.centralwidget = QtWidgets.QWidget(Student)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 110, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Student.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Student)
        self.statusbar.setObjectName("statusbar")
        Student.setStatusBar(self.statusbar)

        self.retranslateUi(Student)
        QtCore.QMetaObject.connectSlotsByName(Student)

    def retranslateUi(self, Student):
        _translate = QtCore.QCoreApplication.translate
        Student.setWindowTitle(_translate("Student", "MainWindow"))
        self.label.setText(_translate("Student", "学生"))
