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

from PySide2.QtSvg import QSvgWidget


class Ui_Student(object):
    def setupUi(self, Student):
        if not Student.objectName():
            Student.setObjectName(u"Student")
        Student.resize(400, 200)
        self.centralwidget = QWidget(Student)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnLearn = QPushButton(self.centralwidget)
        self.btnLearn.setObjectName(u"btnLearn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLearn.sizePolicy().hasHeightForWidth())
        self.btnLearn.setSizePolicy(sizePolicy)
        self.btnLearn.setMinimumSize(QSize(120, 80))
        font = QFont()
        font.setPointSize(12)
        self.btnLearn.setFont(font)

        self.verticalLayout.addWidget(self.btnLearn)

        self.btnSafetyTest = QPushButton(self.centralwidget)
        self.btnSafetyTest.setObjectName(u"btnSafetyTest")
        sizePolicy.setHeightForWidth(self.btnSafetyTest.sizePolicy().hasHeightForWidth())
        self.btnSafetyTest.setSizePolicy(sizePolicy)
        self.btnSafetyTest.setMinimumSize(QSize(120, 80))
        self.btnSafetyTest.setFont(font)

        self.verticalLayout.addWidget(self.btnSafetyTest)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.svgBanner = QSvgWidget(self.centralwidget)
        self.svgBanner.setObjectName(u"svgBanner")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.svgBanner.sizePolicy().hasHeightForWidth())
        self.svgBanner.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.svgBanner)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnSimulator = QPushButton(self.centralwidget)
        self.btnSimulator.setObjectName(u"btnSimulator")
        sizePolicy.setHeightForWidth(self.btnSimulator.sizePolicy().hasHeightForWidth())
        self.btnSimulator.setSizePolicy(sizePolicy)
        self.btnSimulator.setMinimumSize(QSize(120, 80))
        self.btnSimulator.setFont(font)

        self.verticalLayout_2.addWidget(self.btnSimulator)

        self.btnSetting = QPushButton(self.centralwidget)
        self.btnSetting.setObjectName(u"btnSetting")
        sizePolicy.setHeightForWidth(self.btnSetting.sizePolicy().hasHeightForWidth())
        self.btnSetting.setSizePolicy(sizePolicy)
        self.btnSetting.setMinimumSize(QSize(120, 80))
        self.btnSetting.setFont(font)

        self.verticalLayout_2.addWidget(self.btnSetting)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        Student.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btnLearn, self.btnSimulator)
        QWidget.setTabOrder(self.btnSimulator, self.btnSafetyTest)
        QWidget.setTabOrder(self.btnSafetyTest, self.btnSetting)

        self.retranslateUi(Student)

        QMetaObject.connectSlotsByName(Student)
    # setupUi

    def retranslateUi(self, Student):
        Student.setWindowTitle(QCoreApplication.translate("Student", u"CEESS-\u5b66\u751f", None))
        self.btnLearn.setText(QCoreApplication.translate("Student", u"\u5b89\u5168\u5b66\u4e60", None))
        self.btnSafetyTest.setText(QCoreApplication.translate("Student", u"\u5b89\u5168\u6d4b\u8bd5", None))
        self.btnSimulator.setText(QCoreApplication.translate("Student", u"\u5b89\u5168\u6a21\u62df", None))
        self.btnSetting.setText(QCoreApplication.translate("Student", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
    # retranslateUi

