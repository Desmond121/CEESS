# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fireExtinguisherUsing.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_fireExtinguisherUsing(object):
    def setupUi(self, fireExtinguisherUsing):
        if not fireExtinguisherUsing.objectName():
            fireExtinguisherUsing.setObjectName(u"fireExtinguisherUsing")
        fireExtinguisherUsing.resize(736, 461)
        self.horizontalLayout_2 = QHBoxLayout(fireExtinguisherUsing)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(fireExtinguisherUsing)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setProperty("intValue", 5)

        self.horizontalLayout_3.addWidget(self.lcdNumber)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.listWidget.setFont(font1)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.groupBox)

        self.graphicsView = QGraphicsView(fireExtinguisherUsing)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.textBrowser = QTextBrowser(fireExtinguisherUsing)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(fireExtinguisherUsing)

        QMetaObject.connectSlotsByName(fireExtinguisherUsing)
    # setupUi

    def retranslateUi(self, fireExtinguisherUsing):
        fireExtinguisherUsing.setWindowTitle(QCoreApplication.translate("fireExtinguisherUsing", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("fireExtinguisherUsing", u"\u706d\u706b\u5668\u4f7f\u7528", None))
        self.label.setText(QCoreApplication.translate("fireExtinguisherUsing", u"\u5269\u4f59\u6b21\u6570", None))
    # retranslateUi
