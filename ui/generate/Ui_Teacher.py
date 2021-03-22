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

from PySide2.QtSvg import QSvgWidget


class Ui_Teacher(object):
    def setupUi(self, Teacher):
        if not Teacher.objectName():
            Teacher.setObjectName(u"Teacher")
        Teacher.resize(400, 200)
        font = QFont()
        font.setFamily(u"AcadEref")
        Teacher.setFont(font)
        self.centralwidget = QWidget(Teacher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnUserManage = QPushButton(self.centralwidget)
        self.btnUserManage.setObjectName(u"btnUserManage")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUserManage.sizePolicy().hasHeightForWidth())
        self.btnUserManage.setSizePolicy(sizePolicy)
        self.btnUserManage.setMinimumSize(QSize(120, 80))
        font1 = QFont()
        font1.setFamily(u"AcadEref")
        font1.setPointSize(12)
        self.btnUserManage.setFont(font1)

        self.verticalLayout.addWidget(self.btnUserManage)

        self.btnScoreAnalyse = QPushButton(self.centralwidget)
        self.btnScoreAnalyse.setObjectName(u"btnScoreAnalyse")
        sizePolicy.setHeightForWidth(self.btnScoreAnalyse.sizePolicy().hasHeightForWidth())
        self.btnScoreAnalyse.setSizePolicy(sizePolicy)
        self.btnScoreAnalyse.setMinimumSize(QSize(120, 80))
        self.btnScoreAnalyse.setFont(font1)

        self.verticalLayout.addWidget(self.btnScoreAnalyse)


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
        self.btnTestManage = QPushButton(self.centralwidget)
        self.btnTestManage.setObjectName(u"btnTestManage")
        sizePolicy.setHeightForWidth(self.btnTestManage.sizePolicy().hasHeightForWidth())
        self.btnTestManage.setSizePolicy(sizePolicy)
        self.btnTestManage.setMinimumSize(QSize(120, 80))
        self.btnTestManage.setFont(font1)

        self.verticalLayout_2.addWidget(self.btnTestManage)

        self.btnSetting = QPushButton(self.centralwidget)
        self.btnSetting.setObjectName(u"btnSetting")
        sizePolicy.setHeightForWidth(self.btnSetting.sizePolicy().hasHeightForWidth())
        self.btnSetting.setSizePolicy(sizePolicy)
        self.btnSetting.setMinimumSize(QSize(120, 80))
        self.btnSetting.setFont(font1)

        self.verticalLayout_2.addWidget(self.btnSetting)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        Teacher.setCentralWidget(self.centralwidget)

        self.retranslateUi(Teacher)

        QMetaObject.connectSlotsByName(Teacher)
    # setupUi

    def retranslateUi(self, Teacher):
        Teacher.setWindowTitle(QCoreApplication.translate("Teacher", u"CEESS-\u6559\u5e08\u7aef", None))
        self.btnUserManage.setText(QCoreApplication.translate("Teacher", u"\u8d26\u53f7\u7ba1\u7406", None))
        self.btnScoreAnalyse.setText(QCoreApplication.translate("Teacher", u"\u6210\u7ee9\u5206\u6790", None))
        self.btnTestManage.setText(QCoreApplication.translate("Teacher", u"\u9898\u5e93\u7ba1\u7406", None))
        self.btnSetting.setText(QCoreApplication.translate("Teacher", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
    # retranslateUi

