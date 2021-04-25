# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EnterTheLab.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EnterTheLab(object):
    def setupUi(self, EnterTheLab):
        if not EnterTheLab.objectName():
            EnterTheLab.setObjectName(u"EnterTheLab")
        EnterTheLab.resize(843, 553)
        self.horizontalLayout_2 = QHBoxLayout(EnterTheLab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(EnterTheLab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.btnClothes = QPushButton(self.groupBox)
        self.btnClothes.setObjectName(u"btnClothes")
        self.btnClothes.setFont(font1)
        self.btnClothes.setCheckable(True)

        self.verticalLayout.addWidget(self.btnClothes)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.btnShorts = QPushButton(self.groupBox)
        self.pantsGroup = QButtonGroup(EnterTheLab)
        self.pantsGroup.setObjectName(u"pantsGroup")
        self.pantsGroup.addButton(self.btnShorts)
        self.btnShorts.setObjectName(u"btnShorts")
        self.btnShorts.setFont(font1)
        self.btnShorts.setCheckable(True)

        self.verticalLayout.addWidget(self.btnShorts)

        self.btnTrousers = QPushButton(self.groupBox)
        self.pantsGroup.addButton(self.btnTrousers)
        self.btnTrousers.setObjectName(u"btnTrousers")
        self.btnTrousers.setFont(font1)
        self.btnTrousers.setCheckable(True)

        self.verticalLayout.addWidget(self.btnTrousers)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.btnSandals = QPushButton(self.groupBox)
        self.shoesGroup = QButtonGroup(EnterTheLab)
        self.shoesGroup.setObjectName(u"shoesGroup")
        self.shoesGroup.addButton(self.btnSandals)
        self.btnSandals.setObjectName(u"btnSandals")
        self.btnSandals.setFont(font1)
        self.btnSandals.setCheckable(True)

        self.verticalLayout.addWidget(self.btnSandals)

        self.btnShoes = QPushButton(self.groupBox)
        self.shoesGroup.addButton(self.btnShoes)
        self.btnShoes.setObjectName(u"btnShoes")
        self.btnShoes.setFont(font1)
        self.btnShoes.setCheckable(True)

        self.verticalLayout.addWidget(self.btnShoes)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.btnGlasses = QPushButton(self.groupBox)
        self.btnGlasses.setObjectName(u"btnGlasses")
        self.btnGlasses.setFont(font1)
        self.btnGlasses.setCheckable(True)

        self.verticalLayout.addWidget(self.btnGlasses)

        self.btnGloves = QPushButton(self.groupBox)
        self.btnGloves.setObjectName(u"btnGloves")
        self.btnGloves.setFont(font1)
        self.btnGloves.setCheckable(True)

        self.verticalLayout.addWidget(self.btnGloves)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnNext = QPushButton(self.page_1)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setFont(font1)

        self.verticalLayout_2.addWidget(self.btnNext)

        self.stackedWidget.addWidget(self.page_1)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_3 = QVBoxLayout(self.page_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.page_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnSwitch = QPushButton(self.groupBox_2)
        self.btnSwitch.setObjectName(u"btnSwitch")
        self.btnSwitch.setFont(font1)
        self.btnSwitch.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btnSwitch)

        self.btnWindow = QPushButton(self.groupBox_2)
        self.btnWindow.setObjectName(u"btnWindow")
        self.btnWindow.setFont(font1)
        self.btnWindow.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btnWindow)

        self.btnFan = QPushButton(self.groupBox_2)
        self.btnFan.setObjectName(u"btnFan")
        self.btnFan.setFont(font1)
        self.btnFan.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btnFan)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btnFinished = QPushButton(self.page_5)
        self.btnFinished.setObjectName(u"btnFinished")
        self.btnFinished.setFont(font1)

        self.verticalLayout_3.addWidget(self.btnFinished)

        self.stackedWidget.addWidget(self.page_5)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.graphicsView = QGraphicsView(EnterTheLab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.textBrowser = QTextBrowser(EnterTheLab)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(EnterTheLab)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(EnterTheLab)
    # setupUi

    def retranslateUi(self, EnterTheLab):
        EnterTheLab.setWindowTitle(QCoreApplication.translate("EnterTheLab", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("EnterTheLab", u"\u5b9e\u9a8c\u5ba4\u7a7f\u6234\u89c4\u8303", None))
        self.label.setText(QCoreApplication.translate("EnterTheLab", u"\u4e0a\u88c5", None))
        self.btnClothes.setText(QCoreApplication.translate("EnterTheLab", u"\u5b9e\u9a8c\u670d", None))
        self.label_2.setText(QCoreApplication.translate("EnterTheLab", u"\u4e0b\u88c5", None))
        self.btnShorts.setText(QCoreApplication.translate("EnterTheLab", u"\u77ed\u88e4", None))
        self.btnTrousers.setText(QCoreApplication.translate("EnterTheLab", u"\u957f\u88e4", None))
        self.label_3.setText(QCoreApplication.translate("EnterTheLab", u"\u978b\u5b50", None))
        self.btnSandals.setText(QCoreApplication.translate("EnterTheLab", u"\u51c9\u978b", None))
        self.btnShoes.setText(QCoreApplication.translate("EnterTheLab", u"\u8fd0\u52a8\u978b", None))
        self.label_4.setText(QCoreApplication.translate("EnterTheLab", u"\u4e2a\u4eba\u9632\u62a4", None))
        self.btnGlasses.setText(QCoreApplication.translate("EnterTheLab", u"\u62a4\u76ee\u955c", None))
        self.btnGloves.setText(QCoreApplication.translate("EnterTheLab", u"\u624b\u5957", None))
        self.btnNext.setText(QCoreApplication.translate("EnterTheLab", u"\u4e0b\u4e00\u6b65", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("EnterTheLab", u"\u8fdb\u5165\u5b9e\u9a8c\u5ba4", None))
        self.btnSwitch.setText(QCoreApplication.translate("EnterTheLab", u"\u6253\u5f00\u7535\u95f8", None))
        self.btnWindow.setText(QCoreApplication.translate("EnterTheLab", u"\u6253\u5f00\u7a97\u6237", None))
        self.btnFan.setText(QCoreApplication.translate("EnterTheLab", u"\u6253\u5f00\u901a\u98ce\u6a71", None))
        self.btnFinished.setText(QCoreApplication.translate("EnterTheLab", u"\u5b8c\u6210", None))
    # retranslateUi

