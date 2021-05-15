# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Grade.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Grade(object):
    def setupUi(self, Grade):
        if not Grade.objectName():
            Grade.setObjectName(u"Grade")
        Grade.setEnabled(True)
        Grade.resize(736, 559)
        self.centralwidget = QWidget(Grade)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gradeTableWidget = QTableWidget(self.centralwidget)
        if (self.gradeTableWidget.columnCount() < 1):
            self.gradeTableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.gradeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.gradeTableWidget.setObjectName(u"gradeTableWidget")

        self.horizontalLayout_2.addWidget(self.gradeTableWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stages = QStackedWidget(self.centralwidget)
        self.stages.setObjectName(u"stages")
        self.completion = QWidget()
        self.completion.setObjectName(u"completion")
        self.stages.addWidget(self.completion)
        self.grade = QWidget()
        self.grade.setObjectName(u"grade")
        self.stages.addWidget(self.grade)

        self.verticalLayout.addWidget(self.stages)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnCompletion = QPushButton(self.centralwidget)
        self.btnCompletion.setObjectName(u"btnCompletion")
        font = QFont()
        font.setPointSize(13)
        self.btnCompletion.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnCompletion)

        self.btnGrade = QPushButton(self.centralwidget)
        self.btnGrade.setObjectName(u"btnGrade")
        self.btnGrade.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnGrade)

        self.btnHelp = QPushButton(self.centralwidget)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnHelp)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        Grade.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grade)

        self.stages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Grade)
    # setupUi

    def retranslateUi(self, Grade):
        Grade.setWindowTitle(QCoreApplication.translate("Grade", u"CEESS-\u6210\u7ee9\u5206\u6790", None))
        ___qtablewidgetitem = self.gradeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Grade", u"\u59d3\u540d", None));
        self.btnCompletion.setText(QCoreApplication.translate("Grade", u"\u5b8c\u6210\u5ea6\u5206\u5e03", None))
        self.btnGrade.setText(QCoreApplication.translate("Grade", u"\u6210\u7ee9\u5206\u5e03\u53ef\u89c6\u5316", None))
        self.btnHelp.setText(QCoreApplication.translate("Grade", u"\u4f7f\u7528\u8bf4\u660e", None))
    # retranslateUi

