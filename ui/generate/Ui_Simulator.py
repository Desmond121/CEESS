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


class Ui_Simulator(object):
    def setupUi(self, Simulator):
        if not Simulator.objectName():
            Simulator.setObjectName(u"Simulator")
        Simulator.resize(741, 516)
        self.centralwidget = QWidget(Simulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        Simulator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Simulator)

        QMetaObject.connectSlotsByName(Simulator)
    # setupUi

    def retranslateUi(self, Simulator):
        Simulator.setWindowTitle(QCoreApplication.translate("Simulator", u"CEESS-\u5b89\u5168\u6a21\u62df", None))
    # retranslateUi

