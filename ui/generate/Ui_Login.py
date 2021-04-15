# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtSvg import QSvgWidget


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(260, 329)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"AcadEref")
        Login.setFont(font)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.titleSvg = QSvgWidget(self.centralwidget)
        self.titleSvg.setObjectName(u"titleSvg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleSvg.sizePolicy().hasHeightForWidth())
        self.titleSvg.setSizePolicy(sizePolicy1)
        self.titleSvg.setMinimumSize(QSize(240, 60))
        self.titleSvg.setMaximumSize(QSize(240, 60))
        font1 = QFont()
        font1.setFamily(u"Courier New")
        self.titleSvg.setFont(font1)

        self.gridLayout.addWidget(self.titleSvg, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"\u601d\u6e90\u9ed1\u4f53 CN Medium")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lblVersion = QLabel(self.centralwidget)
        self.lblVersion.setObjectName(u"lblVersion")
        font3 = QFont()
        font3.setFamily(u"AcadEref")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.lblVersion.setFont(font3)
        self.lblVersion.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.lblVersion, 3, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.accLineEdit = QLineEdit(self.centralwidget)
        self.accLineEdit.setObjectName(u"accLineEdit")
        sizePolicy.setHeightForWidth(self.accLineEdit.sizePolicy().hasHeightForWidth())
        self.accLineEdit.setSizePolicy(sizePolicy)
        self.accLineEdit.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"\u9ed1\u4f53")
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setWeight(50)
        self.accLineEdit.setFont(font4)

        self.horizontalLayout_2.addWidget(self.accLineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pswLineEdit = QLineEdit(self.centralwidget)
        self.pswLineEdit.setObjectName(u"pswLineEdit")
        sizePolicy.setHeightForWidth(self.pswLineEdit.sizePolicy().hasHeightForWidth())
        self.pswLineEdit.setSizePolicy(sizePolicy)
        self.pswLineEdit.setFont(font4)

        self.horizontalLayout_3.addWidget(self.pswLineEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loginButtom = QPushButton(self.centralwidget)
        self.loginButtom.setObjectName(u"loginButtom")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginButtom.sizePolicy().hasHeightForWidth())
        self.loginButtom.setSizePolicy(sizePolicy2)
        self.loginButtom.setMaximumSize(QSize(80, 30))
        font5 = QFont()
        font5.setFamily(u"\u9ed1\u4f53")
        font5.setPointSize(15)
        self.loginButtom.setFont(font5)

        self.horizontalLayout.addWidget(self.loginButtom)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"CEESS-\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("Login", u"\u5316\u5de5\u5b9e\u9a8c\u4eff\u771f\u6a21\u62df\u7cfb\u7edf", None))
        self.lblVersion.setText(QCoreApplication.translate("Login", u"\u4e91\u7aef\u7248/\u672c\u5730\u7248", None))
        self.accLineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"\u8bf7\u8f93\u5165\u8d26\u6237", None))
        self.pswLineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.loginButtom.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
    # retranslateUi

