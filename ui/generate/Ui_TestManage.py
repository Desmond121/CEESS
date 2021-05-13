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
        TestManage.resize(612, 390)
        self.centralwidget = QWidget(TestManage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.trueFalseLCD = QLCDNumber(self.centralwidget)
        self.trueFalseLCD.setObjectName(u"trueFalseLCD")
        font1 = QFont()
        font1.setPointSize(9)
        self.trueFalseLCD.setFont(font1)
        self.trueFalseLCD.setDigitCount(4)
        self.trueFalseLCD.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_4.addWidget(self.trueFalseLCD)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.trueFalseList = QListWidget(self.centralwidget)
        self.trueFalseList.setObjectName(u"trueFalseList")
        self.trueFalseList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayout.addWidget(self.trueFalseList, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.choiceLCD = QLCDNumber(self.centralwidget)
        self.choiceLCD.setObjectName(u"choiceLCD")
        self.choiceLCD.setDigitCount(4)
        self.choiceLCD.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_3.addWidget(self.choiceLCD)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.choiceList = QListWidget(self.centralwidget)
        self.choiceList.setObjectName(u"choiceList")
        self.choiceList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.choiceList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.choiceList, 1, 0, 1, 1)

        self.btnDeleteChoice = QPushButton(self.centralwidget)
        self.btnDeleteChoice.setObjectName(u"btnDeleteChoice")

        self.gridLayout.addWidget(self.btnDeleteChoice, 2, 0, 1, 1)

        self.btnDeletetrueFalse = QPushButton(self.centralwidget)
        self.btnDeletetrueFalse.setObjectName(u"btnDeletetrueFalse")

        self.gridLayout.addWidget(self.btnDeletetrueFalse, 2, 1, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_5.addWidget(self.textBrowser)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnDownload = QPushButton(self.centralwidget)
        self.btnDownload.setObjectName(u"btnDownload")

        self.horizontalLayout_2.addWidget(self.btnDownload)

        self.btnImport = QPushButton(self.centralwidget)
        self.btnImport.setObjectName(u"btnImport")

        self.horizontalLayout_2.addWidget(self.btnImport)

        self.btnIsOverride = QRadioButton(self.centralwidget)
        self.btnIsOverride.setObjectName(u"btnIsOverride")

        self.horizontalLayout_2.addWidget(self.btnIsOverride)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        TestManage.setCentralWidget(self.centralwidget)

        self.retranslateUi(TestManage)

        QMetaObject.connectSlotsByName(TestManage)
    # setupUi

    def retranslateUi(self, TestManage):
        TestManage.setWindowTitle(QCoreApplication.translate("TestManage", u"CEESS-\u9898\u5e93\u7ba1\u7406", None))
        self.label_2.setText(QCoreApplication.translate("TestManage", u"\u5224\u65ad\u9898", None))
        self.label.setText(QCoreApplication.translate("TestManage", u"\u9009\u62e9\u9898", None))
        self.btnDeleteChoice.setText(QCoreApplication.translate("TestManage", u"\u5220\u9664", None))
        self.btnDeletetrueFalse.setText(QCoreApplication.translate("TestManage", u"\u5220\u9664", None))
        self.textBrowser.setHtml(QCoreApplication.translate("TestManage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btnDownload.setText(QCoreApplication.translate("TestManage", u"\u4e0b\u8f7d\u6a21\u677f", None))
        self.btnImport.setText(QCoreApplication.translate("TestManage", u"\u6279\u91cf\u5bfc\u5165", None))
        self.btnIsOverride.setText(QCoreApplication.translate("TestManage", u"\u5bfc\u5165\u65f6\u8986\u76d6", None))
    # retranslateUi

