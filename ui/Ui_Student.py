# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StudentMainWindow(object):
    def setupUi(self, StudentMainWindow):
        if not StudentMainWindow.objectName():
            StudentMainWindow.setObjectName(u"StudentMainWindow")
        StudentMainWindow.resize(695, 434)
        self.centralwidget = QWidget(StudentMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 6, 1, 1)

        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout.addWidget(self.treeWidget, 0, 1, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout.addWidget(self.toolButton, 2, 4, 1, 1)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 0, 0, 3, 1)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 3, 1, 1)

        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout.addWidget(self.timeEdit, 0, 3, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 4, 1, 1)

        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalSlider, 0, 6, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 4, 1, 1)

        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalScrollBar, 0, 7, 1, 1)

        StudentMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StudentMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        StudentMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StudentMainWindow)

        QMetaObject.connectSlotsByName(StudentMainWindow)
    # setupUi

    def retranslateUi(self, StudentMainWindow):
        StudentMainWindow.setWindowTitle(QCoreApplication.translate("StudentMainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("StudentMainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("StudentMainWindow", u"\u5b66\u751f", None))
        self.toolButton.setText(QCoreApplication.translate("StudentMainWindow", u"...", None))
        self.radioButton.setText(QCoreApplication.translate("StudentMainWindow", u"RadioButton", None))
    # retranslateUi

