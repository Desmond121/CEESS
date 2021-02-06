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


class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        if not LoginMainWindow.objectName():
            LoginMainWindow.setObjectName(u"LoginMainWindow")
        LoginMainWindow.resize(800, 600)
        self.centralwidget = QWidget(LoginMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font)
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
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setWeight(50)
        self.accLabel.setFont(font1)
        self.accLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.accLabel)

        self.accLineEdit = QLineEdit(self.centralwidget)
        self.accLineEdit.setObjectName(u"accLineEdit")
        self.accLineEdit.setFont(font1)

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
        self.pswLabel.setFont(font1)
        self.pswLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.pswLabel)

        self.pswLineEdit = QLineEdit(self.centralwidget)
        self.pswLineEdit.setObjectName(u"pswLineEdit")
        self.pswLineEdit.setFont(font1)

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
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(15)
        self.loginButtom.setFont(font2)

        self.horizontalLayout.addWidget(self.loginButtom)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        LoginMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginMainWindow)

        QMetaObject.connectSlotsByName(LoginMainWindow)
    # setupUi

    def retranslateUi(self, LoginMainWindow):
        LoginMainWindow.setWindowTitle(QCoreApplication.translate("LoginMainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginMainWindow", u"CEESS-\u5316\u5de5\u5b9e\u9a8c\u4eff\u771f\u6a21\u62df\u7cfb\u7edf", None))
        self.accLabel.setText(QCoreApplication.translate("LoginMainWindow", u"\u8d26\u6237", None))
        self.pswLabel.setText(QCoreApplication.translate("LoginMainWindow", u"\u5bc6\u7801", None))
        self.loginButtom.setText(QCoreApplication.translate("LoginMainWindow", u"\u767b\u5f55", None))
    # retranslateUi

