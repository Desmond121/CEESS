# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignRecognizing.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignRecognizing(object):
    def setupUi(self, SignRecognizing):
        if not SignRecognizing.objectName():
            SignRecognizing.setObjectName(u"SignRecognizing")
        SignRecognizing.resize(759, 540)
        self.horizontalLayout_2 = QHBoxLayout(SignRecognizing)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(SignRecognizing)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")
        font1 = QFont()
        font1.setPointSize(16)
        self.listWidget.setFont(font1)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget.setTextElideMode(Qt.ElideMiddle)
        self.listWidget.setSpacing(5)
        self.listWidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.listWidget)

        self.verticalSpacer = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnCheck = QPushButton(self.groupBox)
        self.btnCheck.setObjectName(u"btnCheck")
        self.btnCheck.setEnabled(True)
        self.btnCheck.setFont(font)

        self.verticalLayout.addWidget(self.btnCheck)

        self.btnNext = QPushButton(self.groupBox)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setEnabled(False)
        self.btnNext.setFont(font)

        self.verticalLayout.addWidget(self.btnNext)


        self.horizontalLayout.addWidget(self.groupBox)

        self.graphicsView = QGraphicsView(SignRecognizing)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.textBrowser = QTextBrowser(SignRecognizing)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(SignRecognizing)

        QMetaObject.connectSlotsByName(SignRecognizing)
    # setupUi

    def retranslateUi(self, SignRecognizing):
        SignRecognizing.setWindowTitle(QCoreApplication.translate("SignRecognizing", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("SignRecognizing", u"\u5b89\u5168\u6807\u8bc6\u8fa8\u522b", None))
        self.label.setText(QCoreApplication.translate("SignRecognizing", u"\u6807\u8bc6\u540d\u79f0", None))
        self.btnCheck.setText(QCoreApplication.translate("SignRecognizing", u"\u786e\u8ba4", None))
        self.btnNext.setText(QCoreApplication.translate("SignRecognizing", u"\u4e0b\u4e00\u6b65", None))
    # retranslateUi

