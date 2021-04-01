# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(439, 185)
        self.centralwidget = QWidget(Setting)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.accInfoTab = QWidget()
        self.accInfoTab.setObjectName(u"accInfoTab")
        self.verticalLayout = QVBoxLayout(self.accInfoTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.accInfoTab)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.userAccount = QLineEdit(self.accInfoTab)
        self.userAccount.setObjectName(u"userAccount")
        sizePolicy.setHeightForWidth(self.userAccount.sizePolicy().hasHeightForWidth())
        self.userAccount.setSizePolicy(sizePolicy)
        self.userAccount.setMinimumSize(QSize(180, 0))
        self.userAccount.setReadOnly(True)

        self.horizontalLayout.addWidget(self.userAccount)

        self.horizontalSpacer = QSpacerItem(80, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.accInfoTab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.userName = QLineEdit(self.accInfoTab)
        self.userName.setObjectName(u"userName")
        sizePolicy.setHeightForWidth(self.userName.sizePolicy().hasHeightForWidth())
        self.userName.setSizePolicy(sizePolicy)
        self.userName.setMinimumSize(QSize(180, 0))
        self.userName.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.userName)

        self.rename = QPushButton(self.accInfoTab)
        self.rename.setObjectName(u"rename")
        sizePolicy.setHeightForWidth(self.rename.sizePolicy().hasHeightForWidth())
        self.rename.setSizePolicy(sizePolicy)
        self.rename.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.rename)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnSignOut = QPushButton(self.accInfoTab)
        self.btnSignOut.setObjectName(u"btnSignOut")
        self.btnSignOut.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnSignOut)

        self.btnChangePsw = QPushButton(self.accInfoTab)
        self.btnChangePsw.setObjectName(u"btnChangePsw")
        self.btnChangePsw.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnChangePsw)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.accInfoTab, "")
        self.displayTab = QWidget()
        self.displayTab.setObjectName(u"displayTab")
        self.gridLayout_2 = QGridLayout(self.displayTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.switchDisplayMode = QPushButton(self.displayTab)
        self.switchDisplayMode.setObjectName(u"switchDisplayMode")

        self.gridLayout_2.addWidget(self.switchDisplayMode, 0, 0, 1, 1)

        self.tabWidget.addTab(self.displayTab, "")
        self.aboutTab = QWidget()
        self.aboutTab.setObjectName(u"aboutTab")
        self.horizontalLayout_3 = QHBoxLayout(self.aboutTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textBrowser = QTextBrowser(self.aboutTab)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_3.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.aboutTab, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        Setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(Setting)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Setting", u"\u8d26\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Setting", u"\u59d3\u540d\uff1a", None))
        self.rename.setText(QCoreApplication.translate("Setting", u"\u4fee\u6539", None))
        self.btnSignOut.setText(QCoreApplication.translate("Setting", u"\u9000\u51fa\u8d26\u6237", None))
        self.btnChangePsw.setText(QCoreApplication.translate("Setting", u"\u4fee\u6539\u5bc6\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accInfoTab), QCoreApplication.translate("Setting", u"\u8d26\u53f7", None))
        self.switchDisplayMode.setText(QCoreApplication.translate("Setting", u"\u5e38\u89c4\u6a21\u5f0f/\u591c\u95f4\u6a21\u5f0f\u5207\u6362", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.displayTab), QCoreApplication.translate("Setting", u"\u663e\u793a", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Setting", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Power by Desmond.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All right reserve.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("Setting", u"\u5173\u4e8e", None))
    # retranslateUi

