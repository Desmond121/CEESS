# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Test(object):
    def setupUi(self, Test):
        if not Test.objectName():
            Test.setObjectName(u"Test")
        Test.resize(580, 373)
        self.centralwidget = QWidget(Test)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_12 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.horizontalLayout_8 = QHBoxLayout(self.startPage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnStart = QPushButton(self.startPage)
        self.btnStart.setObjectName(u"btnStart")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)

        self.gridLayout.addWidget(self.btnStart, 2, 1, 1, 1)

        self.lblNameStart = QLabel(self.startPage)
        self.lblNameStart.setObjectName(u"lblNameStart")
        self.lblNameStart.setFont(font)

        self.gridLayout.addWidget(self.lblNameStart, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 2, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout)

        self.pages.addWidget(self.startPage)
        self.testPage = QWidget()
        self.testPage.setObjectName(u"testPage")
        self.horizontalLayout_9 = QHBoxLayout(self.testPage)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTime = QLabel(self.testPage)
        self.lblTime.setObjectName(u"lblTime")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.lblTime.setFont(font1)
        self.lblTime.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblTime)

        self.questionTable = QTableWidget(self.testPage)
        if (self.questionTable.columnCount() < 1):
            self.questionTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.questionTable.setObjectName(u"questionTable")
        self.questionTable.setMinimumSize(QSize(140, 0))
        self.questionTable.setMaximumSize(QSize(140, 16777215))
        self.questionTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.questionTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.questionTable.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.questionTable)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.questionBrowser = QTextBrowser(self.testPage)
        self.questionBrowser.setObjectName(u"questionBrowser")

        self.verticalLayout_4.addWidget(self.questionBrowser)

        self.answerPages = QStackedWidget(self.testPage)
        self.answerPages.setObjectName(u"answerPages")
        self.answerPages.setFrameShadow(QFrame.Plain)
        self.answerPages.setLineWidth(0)
        self.choicePage = QWidget()
        self.choicePage.setObjectName(u"choicePage")
        self.horizontalLayout_2 = QHBoxLayout(self.choicePage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btnA = QPushButton(self.choicePage)
        self.btnA.setObjectName(u"btnA")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnA.setFont(font2)
        self.btnA.setCheckable(False)
        self.btnA.setChecked(False)

        self.horizontalLayout.addWidget(self.btnA)

        self.btnB = QPushButton(self.choicePage)
        self.btnB.setObjectName(u"btnB")
        self.btnB.setFont(font2)
        self.btnB.setCheckable(False)

        self.horizontalLayout.addWidget(self.btnB)

        self.btnC = QPushButton(self.choicePage)
        self.btnC.setObjectName(u"btnC")
        self.btnC.setFont(font2)
        self.btnC.setCheckable(False)

        self.horizontalLayout.addWidget(self.btnC)

        self.btnD = QPushButton(self.choicePage)
        self.btnD.setObjectName(u"btnD")
        self.btnD.setFont(font2)
        self.btnD.setCheckable(False)

        self.horizontalLayout.addWidget(self.btnD)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.answerPages.addWidget(self.choicePage)
        self.trueFalsePage = QWidget()
        self.trueFalsePage.setObjectName(u"trueFalsePage")
        self.horizontalLayout_3 = QHBoxLayout(self.trueFalsePage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btnTrue = QPushButton(self.trueFalsePage)
        self.btnTrue.setObjectName(u"btnTrue")
        self.btnTrue.setFont(font2)
        self.btnTrue.setCheckable(False)
        self.btnTrue.setChecked(False)

        self.horizontalLayout_6.addWidget(self.btnTrue)

        self.btnFalse = QPushButton(self.trueFalsePage)
        self.btnFalse.setObjectName(u"btnFalse")
        self.btnFalse.setFont(font2)
        self.btnFalse.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.btnFalse)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)

        self.answerPages.addWidget(self.trueFalsePage)

        self.verticalLayout_4.addWidget(self.answerPages)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnPrev = QPushButton(self.testPage)
        self.btnPrev.setObjectName(u"btnPrev")
        font3 = QFont()
        font3.setPointSize(12)
        self.btnPrev.setFont(font3)

        self.horizontalLayout_4.addWidget(self.btnPrev)

        self.btnNext = QPushButton(self.testPage)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setFont(font3)

        self.horizontalLayout_4.addWidget(self.btnNext)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.btnSubmit = QPushButton(self.testPage)
        self.btnSubmit.setObjectName(u"btnSubmit")

        self.horizontalLayout_7.addWidget(self.btnSubmit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.pages.addWidget(self.testPage)
        self.overPage = QWidget()
        self.overPage.setObjectName(u"overPage")
        self.horizontalLayout_10 = QHBoxLayout(self.overPage)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.overPage)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_11.addWidget(self.label)

        self.lblGrade = QLabel(self.overPage)
        self.lblGrade.setObjectName(u"lblGrade")
        self.lblGrade.setFont(font)

        self.horizontalLayout_11.addWidget(self.lblGrade)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 2, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.overPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lblNameFinished = QLabel(self.overPage)
        self.lblNameFinished.setObjectName(u"lblNameFinished")
        self.lblNameFinished.setFont(font)

        self.horizontalLayout_5.addWidget(self.lblNameFinished)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_2)

        self.pages.addWidget(self.overPage)

        self.horizontalLayout_12.addWidget(self.pages)

        Test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Test)

        self.pages.setCurrentIndex(1)
        self.answerPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Test)
    # setupUi

    def retranslateUi(self, Test):
        Test.setWindowTitle(QCoreApplication.translate("Test", u"MainWindow", None))
        self.btnStart.setText(QCoreApplication.translate("Test", u"\u5f00\u59cb\u8003\u8bd5", None))
        self.lblNameStart.setText("")
        self.lblTime.setText(QCoreApplication.translate("Test", u"00:00", None))
        ___qtablewidgetitem = self.questionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Test", u"\u9009\u9879", None));
        self.questionBrowser.setHtml(QCoreApplication.translate("Test", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btnA.setText(QCoreApplication.translate("Test", u"A", None))
        self.btnB.setText(QCoreApplication.translate("Test", u"B", None))
        self.btnC.setText(QCoreApplication.translate("Test", u"C", None))
        self.btnD.setText(QCoreApplication.translate("Test", u"D", None))
        self.btnTrue.setText("")
        self.btnFalse.setText("")
        self.btnPrev.setText(QCoreApplication.translate("Test", u"\u4e0a\u4e00\u9898", None))
        self.btnNext.setText(QCoreApplication.translate("Test", u"\u4e0b\u4e00\u9898", None))
        self.btnSubmit.setText(QCoreApplication.translate("Test", u"\u63d0\u4ea4", None))
        self.label.setText(QCoreApplication.translate("Test", u"\u6210\u7ee9\uff1a", None))
        self.lblGrade.setText("")
        self.label_2.setText(QCoreApplication.translate("Test", u"\u59d3\u540d\uff1a", None))
        self.lblNameFinished.setText("")
    # retranslateUi

