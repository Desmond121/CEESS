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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.gradeAnalyse = QWidget()
        self.gradeAnalyse.setObjectName(u"gradeAnalyse")
        self.horizontalLayout_3 = QHBoxLayout(self.gradeAnalyse)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gradeTableWidget = QTableWidget(self.gradeAnalyse)
        if (self.gradeTableWidget.columnCount() < 1):
            self.gradeTableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.gradeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.gradeTableWidget.setObjectName(u"gradeTableWidget")

        self.horizontalLayout_2.addWidget(self.gradeTableWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stages = QStackedWidget(self.gradeAnalyse)
        self.stages.setObjectName(u"stages")
        self.completion = QWidget()
        self.completion.setObjectName(u"completion")
        self.stages.addWidget(self.completion)
        self.grade = QWidget()
        self.grade.setObjectName(u"grade")
        self.stages.addWidget(self.grade)

        self.verticalLayout.addWidget(self.stages)

        self.btnCompletion = QPushButton(self.gradeAnalyse)
        self.btnCompletion.setObjectName(u"btnCompletion")

        self.verticalLayout.addWidget(self.btnCompletion)

        self.btnGrade = QPushButton(self.gradeAnalyse)
        self.btnGrade.setObjectName(u"btnGrade")

        self.verticalLayout.addWidget(self.btnGrade)

        self.pushButton = QPushButton(self.gradeAnalyse)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.gradeAnalyse, "")
        self.other = QWidget()
        self.other.setObjectName(u"other")
        self.tabWidget.addTab(self.other, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        Grade.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grade)

        self.tabWidget.setCurrentIndex(0)
        self.stages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Grade)
    # setupUi

    def retranslateUi(self, Grade):
        Grade.setWindowTitle(QCoreApplication.translate("Grade", u"MainWindow", None))
        ___qtablewidgetitem = self.gradeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Grade", u"\u59d3\u540d", None));
        self.btnCompletion.setText(QCoreApplication.translate("Grade", u"\u5b8c\u6210\u5ea6\u5206\u5e03", None))
        self.btnGrade.setText(QCoreApplication.translate("Grade", u"\u6210\u7ee9\u5206\u5e03\u53ef\u89c6\u5316", None))
        self.pushButton.setText(QCoreApplication.translate("Grade", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gradeAnalyse), QCoreApplication.translate("Grade", u"\u5b8c\u6210\u5ea6\u5206\u6790", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other), QCoreApplication.translate("Grade", u"\u5176\u4ed6\u529f\u80fd", None))
    # retranslateUi

