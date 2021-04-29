# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GasCylindersOperation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GasCylindersOperation(object):
    def setupUi(self, GasCylindersOperation):
        if not GasCylindersOperation.objectName():
            GasCylindersOperation.setObjectName(u"GasCylindersOperation")
        GasCylindersOperation.resize(716, 532)
        self.horizontalLayout_2 = QHBoxLayout(GasCylindersOperation)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(GasCylindersOperation)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.mistakeList = QListWidget(self.groupBox)
        self.mistakeList.setObjectName(u"mistakeList")
        self.mistakeList.setFont(font1)
        self.mistakeList.setFocusPolicy(Qt.NoFocus)
        self.mistakeList.setFrameShape(QFrame.NoFrame)
        self.mistakeList.setAutoScroll(False)
        self.mistakeList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mistakeList.setAlternatingRowColors(True)
        self.mistakeList.setSelectionMode(QAbstractItemView.MultiSelection)
        self.mistakeList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mistakeList.setProperty("isWrapping", False)
        self.mistakeList.setSpacing(5)
        self.mistakeList.setUniformItemSizes(False)
        self.mistakeList.setWordWrap(True)
        self.mistakeList.setSelectionRectVisible(True)

        self.verticalLayout.addWidget(self.mistakeList)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.btnNext = QPushButton(self.page)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setFont(font1)

        self.verticalLayout_2.addWidget(self.btnNext)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.operationList = QListWidget(self.groupBox_2)
        self.operationList.setObjectName(u"operationList")
        self.operationList.setFont(font1)
        self.operationList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.operationList.setDragEnabled(True)
        self.operationList.setDragDropOverwriteMode(False)
        self.operationList.setDragDropMode(QAbstractItemView.InternalMove)
        self.operationList.setDefaultDropAction(Qt.MoveAction)
        self.operationList.setAlternatingRowColors(True)
        self.operationList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.operationList.setSpacing(5)
        self.operationList.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.operationList)

        self.btnDelete = QPushButton(self.groupBox_2)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setFont(font1)

        self.verticalLayout_4.addWidget(self.btnDelete)

        self.btnRedo = QPushButton(self.groupBox_2)
        self.btnRedo.setObjectName(u"btnRedo")
        self.btnRedo.setFont(font1)

        self.verticalLayout_4.addWidget(self.btnRedo)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.btnFinished = QPushButton(self.page_2)
        self.btnFinished.setObjectName(u"btnFinished")
        self.btnFinished.setFont(font1)

        self.verticalLayout_3.addWidget(self.btnFinished)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.graphicsView = QGraphicsView(GasCylindersOperation)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.textBrowser = QTextBrowser(GasCylindersOperation)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(GasCylindersOperation)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(GasCylindersOperation)
    # setupUi

    def retranslateUi(self, GasCylindersOperation):
        GasCylindersOperation.setWindowTitle(QCoreApplication.translate("GasCylindersOperation", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("GasCylindersOperation", u"\u6c14\u74f6\u8fd0\u8f93", None))
        self.label.setText(QCoreApplication.translate("GasCylindersOperation", u"\u9009\u9879", None))
        self.btnNext.setText(QCoreApplication.translate("GasCylindersOperation", u"\u4e0b\u4e00\u6b65", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("GasCylindersOperation", u"\u6c14\u74f6\u64cd\u4f5c", None))
        self.btnDelete.setText(QCoreApplication.translate("GasCylindersOperation", u"\u5220\u9664", None))
        self.btnRedo.setText(QCoreApplication.translate("GasCylindersOperation", u"\u91cd\u505a", None))
        self.btnFinished.setText(QCoreApplication.translate("GasCylindersOperation", u"\u63d0\u4ea4", None))
    # retranslateUi

