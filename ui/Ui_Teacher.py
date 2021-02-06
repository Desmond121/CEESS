# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teacher.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TeacherMainWindow(object):
    def setupUi(self, TeacherMainWindow):
        if not TeacherMainWindow.objectName():
            TeacherMainWindow.setObjectName(u"TeacherMainWindow")
        TeacherMainWindow.resize(427, 292)
        self.centralwidget = QWidget(TeacherMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 100, 161, 111))
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        TeacherMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TeacherMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        TeacherMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TeacherMainWindow)

        QMetaObject.connectSlotsByName(TeacherMainWindow)
    # setupUi

    def retranslateUi(self, TeacherMainWindow):
        TeacherMainWindow.setWindowTitle(QCoreApplication.translate("TeacherMainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("TeacherMainWindow", u"\u8001\u5e08", None))
    # retranslateUi

