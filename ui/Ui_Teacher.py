# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dev\Repo\CEESS\ui\Teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teacher(object):
    def setupUi(self, Teacher):
        Teacher.setObjectName("Teacher")
        Teacher.resize(427, 292)
        self.centralwidget = QtWidgets.QWidget(Teacher)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 100, 161, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Teacher.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Teacher)
        self.statusbar.setObjectName("statusbar")
        Teacher.setStatusBar(self.statusbar)

        self.retranslateUi(Teacher)
        QtCore.QMetaObject.connectSlotsByName(Teacher)

    def retranslateUi(self, Teacher):
        _translate = QtCore.QCoreApplication.translate
        Teacher.setWindowTitle(_translate("Teacher", "MainWindow"))
        self.label.setText(_translate("Teacher", "老师"))