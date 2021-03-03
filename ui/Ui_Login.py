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


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(415, 244)
        font = QFont()
        font.setFamily(u"AcadEref")
        Login.setFont(font)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"\u601d\u6e90\u9ed1\u4f53 CN Medium")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.accLabel = QLabel(self.centralwidget)
        self.accLabel.setObjectName(u"accLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accLabel.sizePolicy().hasHeightForWidth())
        self.accLabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setWeight(50)
        self.accLabel.setFont(font2)
        self.accLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.accLabel)

        self.accLineEdit = QLineEdit(self.centralwidget)
        self.accLineEdit.setObjectName(u"accLineEdit")
        self.accLineEdit.setFont(font2)

        self.horizontalLayout_2.addWidget(self.accLineEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pswLabel = QLabel(self.centralwidget)
        self.pswLabel.setObjectName(u"pswLabel")
        sizePolicy.setHeightForWidth(self.pswLabel.sizePolicy().hasHeightForWidth())
        self.pswLabel.setSizePolicy(sizePolicy)
        self.pswLabel.setFont(font2)
        self.pswLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.pswLabel)

        self.pswLineEdit = QLineEdit(self.centralwidget)
        self.pswLineEdit.setObjectName(u"pswLineEdit")
        self.pswLineEdit.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pswLineEdit)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.loginButtom = QPushButton(self.centralwidget)
        self.loginButtom.setObjectName(u"loginButtom")
        font3 = QFont()
        font3.setFamily(u"\u9ed1\u4f53")
        font3.setPointSize(15)
        self.loginButtom.setFont(font3)

        self.horizontalLayout.addWidget(self.loginButtom)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"CEESS-\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("Login", u"CEESS-\u5316\u5de5\u5b9e\u9a8c\u4eff\u771f\u6a21\u62df\u7cfb\u7edf", None))
        self.accLabel.setText(QCoreApplication.translate("Login", u"\u8d26\u6237", None))
        self.pswLabel.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801", None))
        self.loginButtom.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
    # retranslateUi

