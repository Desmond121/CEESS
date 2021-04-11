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
        UserManage.resize(514, 543)
        self.centralwidget = QWidget(UserManage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnImport = QPushButton(self.centralwidget)
        self.btnImport.setObjectName(u"btnImport")

        self.horizontalLayout.addWidget(self.btnImport)

        self.btnDownload = QPushButton(self.centralwidget)
        self.btnDownload.setObjectName(u"btnDownload")

        self.horizontalLayout.addWidget(self.btnDownload)

        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout.addWidget(self.btnDelete)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.accEdit = QLineEdit(self.groupBox)
        self.accEdit.setObjectName(u"accEdit")

        self.horizontalLayout_3.addWidget(self.accEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.nameEdit = QLineEdit(self.groupBox)
        self.nameEdit.setObjectName(u"nameEdit")

        self.horizontalLayout_2.addWidget(self.nameEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.isAdminButtom = QRadioButton(self.groupBox)
        self.isAdminButtom.setObjectName(u"isAdminButtom")

        self.horizontalLayout_4.addWidget(self.isAdminButtom)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btnNew = QPushButton(self.groupBox)
        self.btnNew.setObjectName(u"btnNew")

        self.horizontalLayout_4.addWidget(self.btnNew)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 2)

        self.userTableWidget = QTableWidget(self.centralwidget)
        if (self.userTableWidget.columnCount() < 3):
            self.userTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.userTableWidget.setObjectName(u"userTableWidget")
        self.userTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.userTableWidget.setSortingEnabled(True)
        self.userTableWidget.horizontalHeader().setCascadingSectionResizes(True)

        self.gridLayout.addWidget(self.userTableWidget, 1, 0, 1, 1)

        UserManage.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserManage)

        QMetaObject.connectSlotsByName(UserManage)
    # setupUi

    def retranslateUi(self, UserManage):
        UserManage.setWindowTitle(QCoreApplication.translate("UserManage", u"CEESS-\u8d26\u53f7\u7ba1\u7406", None))
        self.btnImport.setText(QCoreApplication.translate("UserManage", u"Excel\u5bfc\u5165", None))
        self.btnDownload.setText(QCoreApplication.translate("UserManage", u"\u4e0b\u8f7d\u5bfc\u5165\u6a21\u677f", None))
        self.btnDelete.setText(QCoreApplication.translate("UserManage", u"\u5220\u9664", None))
        self.groupBox.setTitle(QCoreApplication.translate("UserManage", u"\u65b0\u589e\u8d26\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("UserManage", u"\u8d26\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("UserManage", u"\u59d3\u540d", None))
        self.isAdminButtom.setText(QCoreApplication.translate("UserManage", u"\u7ba1\u7406\u5458", None))
        self.btnNew.setText(QCoreApplication.translate("UserManage", u"\u65b0\u589e", None))
        ___qtablewidgetitem = self.userTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UserManage", u"\u8d26\u53f7", None));
        ___qtablewidgetitem1 = self.userTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UserManage", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.userTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UserManage", u"\u7c7b\u578b", None));
    # retranslateUi

