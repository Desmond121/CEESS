# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'centrifugeOperation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_centrifugeOperation(object):
    def setupUi(self, centrifugeOperation):
        if not centrifugeOperation.objectName():
            centrifugeOperation.setObjectName(u"centrifugeOperation")
        centrifugeOperation.resize(701, 444)
        self.horizontalLayout_2 = QHBoxLayout(centrifugeOperation)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(centrifugeOperation)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_9 = QVBoxLayout(self.page_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_5 = QGroupBox(self.page_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        font = QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_3)

        self.nameList = QListWidget(self.groupBox_5)
        self.nameList.setObjectName(u"nameList")
        font2 = QFont()
        font2.setPointSize(15)
        self.nameList.setFont(font2)
        self.nameList.setFocusPolicy(Qt.NoFocus)
        self.nameList.setAlternatingRowColors(True)
        self.nameList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.nameList.setSpacing(8)

        self.verticalLayout_10.addWidget(self.nameList)

        self.btnCheck = QPushButton(self.groupBox_5)
        self.btnCheck.setObjectName(u"btnCheck")
        self.btnCheck.setFont(font1)

        self.verticalLayout_10.addWidget(self.btnCheck)

        self.verticalSpacer_2 = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.verticalLayout_9.addWidget(self.groupBox_5)

        self.btnNext = QPushButton(self.page_5)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setEnabled(False)
        self.btnNext.setFont(font1)

        self.verticalLayout_9.addWidget(self.btnNext)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_11 = QVBoxLayout(self.page_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_6 = QGroupBox(self.page_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lcdNumber = QLCDNumber(self.groupBox_6)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("intValue", 5)

        self.horizontalLayout_4.addWidget(self.lcdNumber)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.operationList = QListWidget(self.groupBox_6)
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

        self.verticalLayout_12.addWidget(self.operationList)


        self.verticalLayout_11.addWidget(self.groupBox_6)

        self.stackedWidget.addWidget(self.page_6)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.graphicsView = QGraphicsView(centrifugeOperation)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.textBrowser = QTextBrowser(centrifugeOperation)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(centrifugeOperation)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(centrifugeOperation)
    # setupUi

    def retranslateUi(self, centrifugeOperation):
        centrifugeOperation.setWindowTitle(QCoreApplication.translate("centrifugeOperation", u"Form", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("centrifugeOperation", u"\u8ba4\u8bc6\u79bb\u5fc3\u673a", None))
        self.label_3.setText(QCoreApplication.translate("centrifugeOperation", u"\u79bb\u5fc3\u673a\u90e8\u4ef6\u540d\u79f0", None))
        self.btnCheck.setText(QCoreApplication.translate("centrifugeOperation", u"\u5b8c\u6210", None))
        self.btnNext.setText(QCoreApplication.translate("centrifugeOperation", u"\u4e0b\u4e00\u6b65", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("centrifugeOperation", u"\u79bb\u5fc3\u673a\u64cd\u4f5c\u6d41\u7a0b", None))
        self.label_4.setText(QCoreApplication.translate("centrifugeOperation", u"\u5269\u4f59\u6b21\u6570", None))
    # retranslateUi

