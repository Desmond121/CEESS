# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserManage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UserManage(object):
    def setupUi(self, UserManage):
        if not UserManage.objectName():
            UserManage.setObjectName(u"UserManage")
        UserManage.resize(581, 468)
        self.centralwidget = QWidget(UserManage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_4.addWidget(self.radioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        UserManage.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserManage)

        QMetaObject.connectSlotsByName(UserManage)
    # setupUi

    def retranslateUi(self, UserManage):
        UserManage.setWindowTitle(QCoreApplication.translate("UserManage", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("UserManage", u"\u65b0\u589e\u8d26\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("UserManage", u"\u8d26\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("UserManage", u"\u59d3\u540d", None))
        self.radioButton.setText(QCoreApplication.translate("UserManage", u"\u7ba1\u7406\u5458", None))
        self.pushButton_2.setText(QCoreApplication.translate("UserManage", u"\u65b0\u589e", None))
        self.pushButton_3.setText(QCoreApplication.translate("UserManage", u"Excel\u5bfc\u5165", None))
        self.pushButton.setText(QCoreApplication.translate("UserManage", u"\u5220\u9664", None))
    # retranslateUi

