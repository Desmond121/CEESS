# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Student(object):
    def setupUi(self, Student):
        if not Student.objectName():
            Student.setObjectName(u"Student")
        Student.resize(400, 200)
        self.centralwidget = QWidget(Student)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnSafetyTest = QPushButton(self.centralwidget)
        self.btnSafetyTest.setObjectName(u"btnSafetyTest")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSafetyTest.sizePolicy().hasHeightForWidth())
        self.btnSafetyTest.setSizePolicy(sizePolicy)
        self.btnSafetyTest.setMinimumSize(QSize(120, 80))
        font = QFont()
        font.setPointSize(12)
        self.btnSafetyTest.setFont(font)

        self.gridLayout.addWidget(self.btnSafetyTest, 0, 0, 1, 1)

        self.btnPreparing = QPushButton(self.centralwidget)
        self.btnPreparing.setObjectName(u"btnPreparing")
        sizePolicy.setHeightForWidth(self.btnPreparing.sizePolicy().hasHeightForWidth())
        self.btnPreparing.setSizePolicy(sizePolicy)
        self.btnPreparing.setMinimumSize(QSize(120, 80))
        self.btnPreparing.setFont(font)

        self.gridLayout.addWidget(self.btnPreparing, 0, 1, 1, 1)

        self.btnSimulator = QPushButton(self.centralwidget)
        self.btnSimulator.setObjectName(u"btnSimulator")
        sizePolicy.setHeightForWidth(self.btnSimulator.sizePolicy().hasHeightForWidth())
        self.btnSimulator.setSizePolicy(sizePolicy)
        self.btnSimulator.setMinimumSize(QSize(120, 80))
        self.btnSimulator.setFont(font)

        self.gridLayout.addWidget(self.btnSimulator, 0, 2, 1, 1)

        self.btnDataProcess = QPushButton(self.centralwidget)
        self.btnDataProcess.setObjectName(u"btnDataProcess")
        sizePolicy.setHeightForWidth(self.btnDataProcess.sizePolicy().hasHeightForWidth())
        self.btnDataProcess.setSizePolicy(sizePolicy)
        self.btnDataProcess.setMinimumSize(QSize(120, 80))
        self.btnDataProcess.setFont(font)

        self.gridLayout.addWidget(self.btnDataProcess, 1, 0, 1, 1)

        self.btnExpTest = QPushButton(self.centralwidget)
        self.btnExpTest.setObjectName(u"btnExpTest")
        sizePolicy.setHeightForWidth(self.btnExpTest.sizePolicy().hasHeightForWidth())
        self.btnExpTest.setSizePolicy(sizePolicy)
        self.btnExpTest.setMinimumSize(QSize(120, 80))
        self.btnExpTest.setFont(font)

        self.gridLayout.addWidget(self.btnExpTest, 1, 1, 1, 1)

        self.btnSetting = QPushButton(self.centralwidget)
        self.btnSetting.setObjectName(u"btnSetting")
        sizePolicy.setHeightForWidth(self.btnSetting.sizePolicy().hasHeightForWidth())
        self.btnSetting.setSizePolicy(sizePolicy)
        self.btnSetting.setMinimumSize(QSize(120, 80))
        self.btnSetting.setFont(font)

        self.gridLayout.addWidget(self.btnSetting, 1, 2, 1, 1)

        Student.setCentralWidget(self.centralwidget)

        self.retranslateUi(Student)

        QMetaObject.connectSlotsByName(Student)
    # setupUi

    def retranslateUi(self, Student):
        Student.setWindowTitle(QCoreApplication.translate("Student", u"CEESS-\u5b66\u751f", None))
        self.btnSafetyTest.setText(QCoreApplication.translate("Student", u"\u5b89\u5168\u6d4b\u8bd5", None))
        self.btnPreparing.setText(QCoreApplication.translate("Student", u"\u5b9e\u9a8c\u9884\u4e60", None))
        self.btnSimulator.setText(QCoreApplication.translate("Student", u"\u5b9e\u9a8c\u6a21\u62df", None))
        self.btnDataProcess.setText(QCoreApplication.translate("Student", u"\u6570\u636e\u5904\u7406", None))
        self.btnExpTest.setText(QCoreApplication.translate("Student", u"\u5b9e\u9a8c\u6d4b\u8bd5", None))
        self.btnSetting.setText(QCoreApplication.translate("Student", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
    # retranslateUi

