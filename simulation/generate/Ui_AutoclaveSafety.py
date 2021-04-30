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
        font2 = QFont()
        font2.setPointSize(15)
        self.nameList.setFont(font2)
        self.nameList.setFocusPolicy(Qt.NoFocus)
        self.nameList.setAlternatingRowColors(True)
        self.nameList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.nameList.setSpacing(8)

        self.verticalLayout_6.addWidget(self.nameList)

        self.btnCheck = QPushButton(self.groupBox_3)
        self.btnCheck.setObjectName(u"btnCheck")
        self.btnCheck.setFont(font1)

        self.verticalLayout_6.addWidget(self.btnCheck)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.btnNext = QPushButton(self.page_3)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setEnabled(False)
        self.btnNext.setFont(font1)

        self.verticalLayout_5.addWidget(self.btnNext)

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
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.groupBox_4)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("intValue", 5)

        self.horizontalLayout_3.addWidget(self.lcdNumber)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.operationList = QListWidget(self.groupBox_4)
        self.operationList.setObjectName(u"operationList")
        self.operationList.setFont(font1)
        self.operationList.setFocusPolicy(Qt.NoFocus)
        self.operationList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.operationList.setDragEnabled(True)
        self.operationList.setDragDropOverwriteMode(False)
        self.operationList.setDragDropMode(QAbstractItemView.InternalMove)
        self.operationList.setDefaultDropAction(Qt.MoveAction)
        self.operationList.setAlternatingRowColors(True)
        self.operationList.setSelectionMode(QAbstractItemView.NoSelection)
        self.operationList.setSpacing(5)
        self.operationList.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.operationList)


        self.verticalLayout_7.addWidget(self.groupBox_4)

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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AutoclaveSafety)
    # setupUi

    def retranslateUi(self, AutoclaveSafety):
        AutoclaveSafety.setWindowTitle(QCoreApplication.translate("AutoclaveSafety", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AutoclaveSafety", u"\u8ba4\u8bc6\u9ad8\u538b\u91dc", None))
        self.label_2.setText(QCoreApplication.translate("AutoclaveSafety", u"\u9ad8\u538b\u91dc\u90e8\u4ef6\u540d\u79f0", None))
        self.btnCheck.setText(QCoreApplication.translate("AutoclaveSafety", u"\u5b8c\u6210", None))
        self.btnNext.setText(QCoreApplication.translate("AutoclaveSafety", u"\u4e0b\u4e00\u6b65", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("AutoclaveSafety", u"\u9ad8\u538b\u91dc\u64cd\u4f5c\u6d41\u7a0b", None))
        self.label.setText(QCoreApplication.translate("AutoclaveSafety", u"\u5269\u4f59\u6b21\u6570", None))
    # retranslateUi

