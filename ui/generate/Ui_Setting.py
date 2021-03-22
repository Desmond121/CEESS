# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(463, 312)
        self.centralwidget = QWidget(Setting)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.accInfoTab = QWidget()
        self.accInfoTab.setObjectName(u"accInfoTab")
        self.verticalLayout = QVBoxLayout(self.accInfoTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.accInfoTab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_5 = QLabel(self.accInfoTab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.accInfoTab)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.accInfoTab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.accInfoTab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_6 = QLabel(self.accInfoTab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(self.accInfoTab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.verticalLayout.addWidget(self.pushButton)

        self.tabWidget.addTab(self.accInfoTab, "")
        self.themeSettingTab = QWidget()
        self.themeSettingTab.setObjectName(u"themeSettingTab")
        self.gridLayout_2 = QGridLayout(self.themeSettingTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton = QRadioButton(self.themeSettingTab)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.tabWidget.addTab(self.themeSettingTab, "")
        self.aboutTab = QWidget()
        self.aboutTab.setObjectName(u"aboutTab")
        self.tabWidget.addTab(self.aboutTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        Setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(Setting)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("Setting", u"\u59d3\u540d\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Setting", u"\u9093\u94ed\u54f2", None))
        self.label.setText(QCoreApplication.translate("Setting", u"\u8d26\u53f7\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Setting", u"201764362216", None))
        self.label_3.setText(QCoreApplication.translate("Setting", u"\u6743\u9650\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Setting", u"\u5b66\u751f", None))
        self.pushButton.setText(QCoreApplication.translate("Setting", u"\u9000\u51fa\u8d26\u6237", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accInfoTab), QCoreApplication.translate("Setting", u"\u8d26\u53f7", None))
        self.radioButton.setText(QCoreApplication.translate("Setting", u"\u591c\u95f4\u6a21\u5f0f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.themeSettingTab), QCoreApplication.translate("Setting", u"\u663e\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("Setting", u"\u5173\u4e8e", None))
    # retranslateUi

