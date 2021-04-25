# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Learn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_Learn(object):
    def setupUi(self, Learn):
        if not Learn.objectName():
            Learn.setObjectName(u"Learn")
        Learn.resize(626, 465)
        self.centralwidget = QWidget(Learn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.learningList = QListWidget(self.centralwidget)
        self.learningList.setObjectName(u"learningList")
        self.learningList.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.learningList.setFont(font)

        self.verticalLayout.addWidget(self.learningList)

        self.btnDownload = QPushButton(self.centralwidget)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setFont(font)

        self.verticalLayout.addWidget(self.btnDownload)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.webViewer = QWebEngineView(self.centralwidget)
        self.webViewer.setObjectName(u"webViewer")

        self.horizontalLayout_2.addWidget(self.webViewer)

        self.horizontalLayout_2.setStretch(1, 3)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        Learn.setCentralWidget(self.centralwidget)

        self.retranslateUi(Learn)

        QMetaObject.connectSlotsByName(Learn)
    # setupUi

    def retranslateUi(self, Learn):
        Learn.setWindowTitle(QCoreApplication.translate("Learn", u"MainWindow", None))
        self.btnDownload.setText(QCoreApplication.translate("Learn", u"\u4e0b\u8f7d\u5b8c\u6574\u5b89\u5168\u624b\u518c", None))
    # retranslateUi

