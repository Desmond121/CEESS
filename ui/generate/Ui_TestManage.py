# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestManage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TestManage(object):
    def setupUi(self, TestManage):
        if not TestManage.objectName():
            TestManage.setObjectName(u"TestManage")
        TestManage.resize(509, 474)
        self.centralwidget = QWidget(TestManage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        TestManage.setCentralWidget(self.centralwidget)

        self.retranslateUi(TestManage)

        QMetaObject.connectSlotsByName(TestManage)
    # setupUi

    def retranslateUi(self, TestManage):
        TestManage.setWindowTitle(QCoreApplication.translate("TestManage", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("TestManage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cascadia Code','Consolas','Courier New','monospace'; font-size:14px; font-weight:296; color:#000000;\">\u8fd9\u662f\u7b2c\u4e00\u9898\uff0c\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u8bd5\u6d4b\u8bd5</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-family:'Cascadia Code','Consolas','Courier New','monospace'; font-size:14px; font-weight:296; color:#000000;\">A.\u9009\u9879\u9009\u9879</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cascadia Code','Consolas','Courier New','monospace'; font-size:14px; color:#000000;\">B.</span><span style=\" font-family:'Cascadia Code','Consolas','Courier New','monospace'; font-size:14px; font-weight:296; color:#000000;\">\u9009\u9879\u9009\u9879</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cascadia Code','Consolas','Courier New','monospace'; font-size:14px; font-weight:296; color:#000000;\">C.\u9009\u9879\u9009\u9879</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-family:'Cascadia Code','Consolas','Courier New','monospace'; font-size:14px; font-weight:296; color:#000000;\">D.\u9009\u9879\u9009\u9879</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("TestManage", u"\u5220\u9664", None))
        self.pushButton_2.setText(QCoreApplication.translate("TestManage", u"\u6279\u91cf\u5bfc\u5165", None))
        self.radioButton.setText(QCoreApplication.translate("TestManage", u"\u5bfc\u5165\u65f6\u8986\u76d6", None))
    # retranslateUi

