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


class Ui_Teacher(object):
    def setupUi(self, Teacher):
        if not Teacher.objectName():
            Teacher.setObjectName(u"Teacher")
        Teacher.resize(643, 449)
        font = QFont()
        font.setFamily(u"AcadEref")
        Teacher.setFont(font)
        self.centralwidget = QWidget(Teacher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox = QComboBox(self.page_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 1)

        self.timeEdit = QTimeEdit(self.page_2)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout.addWidget(self.timeEdit, 1, 0, 1, 1)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"AcadEref")
        font1.setPointSize(20)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.calendarWidget = QCalendarWidget(self.page_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout.addWidget(self.calendarWidget, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        Teacher.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Teacher)
        self.statusbar.setObjectName(u"statusbar")
        Teacher.setStatusBar(self.statusbar)

        self.retranslateUi(Teacher)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Teacher)
    # setupUi

    def retranslateUi(self, Teacher):
        Teacher.setWindowTitle(QCoreApplication.translate("Teacher", u"CEESS-\u6559\u5e08\u7aef", None))
        self.label.setText(QCoreApplication.translate("Teacher", u"Teacher", None))
    # retranslateUi

