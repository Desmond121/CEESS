# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoclaveSafety.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AutoclaveSafety(object):
    def setupUi(self, AutoclaveSafety):
        if not AutoclaveSafety.objectName():
            AutoclaveSafety.setObjectName(u"AutoclaveSafety")
        AutoclaveSafety.resize(776, 513)
        self.horizontalLayout_2 = QHBoxLayout(AutoclaveSafety)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(AutoclaveSafety)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.page_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font = QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_2)

        self.nameList = QListWidget(self.groupBox_3)
        self.nameList.setObjectName(u"nameList")
        self.nameList.setFont(font1)
        self.nameList.setFocusPolicy(Qt.NoFocus)
        self.nameList.setFrameShape(QFrame.NoFrame)
        self.nameList.setAutoScroll(False)
        self.nameList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.nameList.setAlternatingRowColors(True)
        self.nameList.setSelectionMode(QAbstractItemView.NoSelection)
        self.nameList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.nameList.setProperty("isWrapping", False)
        self.nameList.setSpacing(5)
        self.nameList.setUniformItemSizes(False)
        self.nameList.setWordWrap(True)
        self.nameList.setSelectionRectVisible(True)

        self.verticalLayout_6.addWidget(self.nameList)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.btnNext_2 = QPushButton(self.page_3)
        self.btnNext_2.setObjectName(u"btnNext_2")
        self.btnNext_2.setFont(font1)

        self.verticalLayout_5.addWidget(self.btnNext_2)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_4 = QGroupBox(self.page_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.operationList_2 = QListWidget(self.groupBox_4)
        self.operationList_2.setObjectName(u"operationList_2")
        self.operationList_2.setFont(font1)
        self.operationList_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.operationList_2.setDragEnabled(True)
        self.operationList_2.setDragDropOverwriteMode(False)
        self.operationList_2.setDragDropMode(QAbstractItemView.InternalMove)
        self.operationList_2.setDefaultDropAction(Qt.MoveAction)
        self.operationList_2.setAlternatingRowColors(True)
        self.operationList_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.operationList_2.setSpacing(5)
        self.operationList_2.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.operationList_2)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.pushButton = QPushButton(self.page_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.verticalLayout_7.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.graphicsView = QGraphicsView(AutoclaveSafety)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.textBrowser = QTextBrowser(AutoclaveSafety)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(AutoclaveSafety)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AutoclaveSafety)
    # setupUi

    def retranslateUi(self, AutoclaveSafety):
        AutoclaveSafety.setWindowTitle(QCoreApplication.translate("AutoclaveSafety", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AutoclaveSafety", u"\u8ba4\u8bc6\u9ad8\u538b\u91dc", None))
        self.label_2.setText(QCoreApplication.translate("AutoclaveSafety", u"\u9009\u9879", None))
        self.btnNext_2.setText(QCoreApplication.translate("AutoclaveSafety", u"\u4e0b\u4e00\u6b65", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("AutoclaveSafety", u"\u8ba4\u8bc6\u9ad8\u538b\u91dc", None))
        self.pushButton.setText(QCoreApplication.translate("AutoclaveSafety", u"\u63d0\u4ea4", None))
    # retranslateUi

