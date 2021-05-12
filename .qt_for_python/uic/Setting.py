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
        Setting.resize(563, 203)
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
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.accInfoTab)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.userAccount = QLineEdit(self.accInfoTab)
        self.userAccount.setObjectName(u"userAccount")

        self.horizontalLayout.addWidget(self.userAccount)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.accInfoTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.userName = QLineEdit(self.accInfoTab)
        self.userName.setObjectName(u"userName")

        self.horizontalLayout_2.addWidget(self.userName)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnSignOut = QPushButton(self.accInfoTab)
        self.btnSignOut.setObjectName(u"btnSignOut")
        font1 = QFont()
        font1.setPointSize(12)
        self.btnSignOut.setFont(font1)

        self.horizontalLayout_4.addWidget(self.btnSignOut)

        self.btnChangePsw = QPushButton(self.accInfoTab)
        self.btnChangePsw.setObjectName(u"btnChangePsw")
        self.btnChangePsw.setFont(font1)

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
        self.gradeTab = QWidget()
        self.gradeTab.setObjectName(u"gradeTab")
        self.horizontalLayout_6 = QHBoxLayout(self.gradeTab)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gradeTabStack = QStackedWidget(self.gradeTab)
        self.gradeTabStack.setObjectName(u"gradeTabStack")
        self.teacherPage = QWidget()
        self.teacherPage.setObjectName(u"teacherPage")
        self.verticalLayout_3 = QVBoxLayout(self.teacherPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser_2 = QTextBrowser(self.teacherPage)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_3.addWidget(self.textBrowser_2)

        self.btnImport = QPushButton(self.teacherPage)
        self.btnImport.setObjectName(u"btnImport")

        self.verticalLayout_3.addWidget(self.btnImport)

        self.gradeTabStack.addWidget(self.teacherPage)
        self.studentPage = QWidget()
        self.studentPage.setObjectName(u"studentPage")
        self.verticalLayout_2 = QVBoxLayout(self.studentPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gradeInfoText = QTextBrowser(self.studentPage)
        self.gradeInfoText.setObjectName(u"gradeInfoText")

        self.verticalLayout_2.addWidget(self.gradeInfoText)

        self.btnExport = QPushButton(self.studentPage)
        self.btnExport.setObjectName(u"btnExport")

        self.verticalLayout_2.addWidget(self.btnExport)

        self.gradeTabStack.addWidget(self.studentPage)

        self.horizontalLayout_6.addWidget(self.gradeTabStack)

        self.tabWidget.addTab(self.gradeTab, "")
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
        self.gradeTabStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"CEESS-\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Setting", u"\u8d26\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Setting", u"\u5bc6\u7801\uff1a", None))
        self.btnSignOut.setText(QCoreApplication.translate("Setting", u"\u9000\u51fa\u8d26\u6237", None))
        self.btnChangePsw.setText(QCoreApplication.translate("Setting", u"\u4fee\u6539\u5bc6\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accInfoTab), QCoreApplication.translate("Setting", u"\u4e2a\u4eba\u8d26\u53f7", None))
        self.switchDisplayMode.setText(QCoreApplication.translate("Setting", u"\u5e38\u89c4\u6a21\u5f0f/\u591c\u95f4\u6a21\u5f0f\u5207\u6362", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.displayTab), QCoreApplication.translate("Setting", u"\u663e\u793a\u8bbe\u7f6e", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Setting", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u5c06\u5b66\u751f\u5bfc\u51fa\u7684\u6210\u7ee9\u653e\u5165\u540c\u4e00\u4e2a\u6587\u4ef6\u5939\u4e2d\uff0c\u70b9\u51fb\u4e0b\u65b9\u6309\u94ae\u9009\u62e9\u6587\u4ef6\u5939\u5373\u53ef\u3002</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#aa0000;\">\u8be5\u884c\u4e3a\u4f1a\u6e05\u7a7a\u6570\u636e\u5e93\u4e2d\u73b0\u5b58\u7684\u6210\u7ee9\u3002</span></p></body></html>", None))
        self.btnImport.setText(QCoreApplication.translate("Setting", u"\u5bfc\u5165\u6210\u7ee9", None))
        self.btnExport.setText(QCoreApplication.translate("Setting", u"\u5bfc\u51fa\u6210\u7ee9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gradeTab), "")
        self.textBrowser.setHtml(QCoreApplication.translate("Setting", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-"
                        "size:12pt; font-weight:600;\">Powered by Desmond.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">All right reserved.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("Setting", u"\u5173\u4e8e", None))
    # retranslateUi

