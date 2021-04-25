# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Simulator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_Simulator(object):
    def setupUi(self, Simulator):
        if not Simulator.objectName():
            Simulator.setObjectName(u"Simulator")
        Simulator.resize(511, 434)
        self.centralwidget = QWidget(Simulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.web = QWebEngineView(self.centralwidget)
        self.web.setObjectName(u"web")

        self.horizontalLayout.addWidget(self.web)

        Simulator.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Simulator)
        self.statusbar.setObjectName(u"statusbar")
        Simulator.setStatusBar(self.statusbar)

        self.retranslateUi(Simulator)

        QMetaObject.connectSlotsByName(Simulator)
    # setupUi

    def retranslateUi(self, Simulator):
        Simulator.setWindowTitle(QCoreApplication.translate("Simulator", u"MainWindow", None))
    # retranslateUi

