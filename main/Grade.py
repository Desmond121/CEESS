"""
@file       : Grade.py
@description: This module help teacher analyze
              the completion status and grade status of students.
@date       : 2021/04/12 15:23:14
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from charts.CompletionPieChart import CompletionPieChart
from charts.GradeVisualizationWidget import GradeVisualizationWidget
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QMargins, Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import (QLayout, QMainWindow, QTableWidgetItem,
                               QVBoxLayout)
from ui.generate.Ui_Grade import Ui_Grade
from utility.DataManager import DataManager


class Grade(QMainWindow):
    # testTypeDict { tid: type_name, ...}
    testTypeDict = None
    # studentNameDict { uid: name, ...}
    studentNameDict = None
    # studentNameDict { uid: {tid: grade}, ...} dict in dict
    studentGradeDict = None
    # tableColumnDict { tid: column, ...}
    tableColumnDict = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Grade()
        self.ui.setupUi(self)
        self.ui.stages.setCurrentIndex(0)
        self.showMaximized()

        # get data from database
        db = DataManager()
        grades = db.getAllGrade()
        names = db.getStudentNames()
        self.testTypeDict = db.getTestTypeDict()
        db.closeConnect()
        # setup name dict
        self.studentNameDict = dict()
        for id, name in names:
            self.studentNameDict.setdefault(id, name)

        # setup grade dict { UID: (QID, grade), ... }
        self.studentGradeDict = dict()
        for uid, tid, grade in grades:
            if self.studentGradeDict.get(uid) is None:
                self.studentGradeDict[uid] = {tid: grade}
            else:
                self.studentGradeDict[uid].setdefault(tid, grade)

        # setup QChartView
        self.ui.completion.setStyleSheet("background-color:#1F2430;")
        self.chartView = QtCharts.QChartView(self.ui.completion)
        completionLayout = QVBoxLayout()
        completionLayout.setContentsMargins(QMargins(0, 0, 0, 0))
        completionLayout.addWidget(self.chartView)
        self.ui.completion.setLayout(completionLayout)

        self.setupCompletionPie()
        self.chartView.setChart(self.chart)

        # setup GradeVisualizationWidget (Q3DBar)
        self.setupGradeVisualization()
        gradeLayout = QVBoxLayout()
        gradeLayout.setContentsMargins(QMargins(0, 0, 0, 0))
        gradeLayout.addWidget(self.gradeVisualization)
        self.ui.grade.setLayout(gradeLayout)

        # import data into table
        self.setupGradeTable()

    def setupGradeTable(self):
        # setup rows and columns
        tableColumn = len(self.testTypeDict) + 1
        tableRow = len(self.studentNameDict)
        self.ui.gradeTableWidget.setColumnCount(tableColumn)
        self.ui.gradeTableWidget.setRowCount(tableRow)
        for row in range(tableRow):
            for col in range(tableColumn):
                item = QTableWidgetItem("未完成")
                item.setBackgroundColor(QColor(0xFF8D6F))
                self.ui.gradeTableWidget.setItem(row, col, item)

        # setup table label
        self.tableColumnDict = dict()
        labels = ["姓名"]
        index = 1
        for id, name in self.testTypeDict.items():
            labels.append(name)
            self.tableColumnDict.setdefault(id, index)
            index += 1
        self.ui.gradeTableWidget.setHorizontalHeaderLabels(labels)

        # load student grade
        row = 0
        for id, name in self.studentNameDict.items():
            self.ui.gradeTableWidget.setItem(row, 0,
                                             QTableWidgetItem(str(name)))
            grades = self.studentGradeDict.get(id)
            if grades is not None:
                for tid, grade in grades.items():
                    item = self.ui.gradeTableWidget.item(
                        row, self.tableColumnDict.get(tid))
                    item.setBackgroundColor(QColor(0x84BC46))
                    item.setText(str(round(grade, 2)))
            row += 1

    def setupCompletionPie(self):
        sliceCount = len(self.testTypeDict) + 1
        # for example: there are 4 types, so the sliceCount will be 5 which
        # represent 5 completion status: finished all, 3, 2, 1, 0 test(s)
        slices = [0] * sliceCount
        # {0, 1, 2, 3, ..., all} each element contain the amount of students in
        # this completion status.
        for uid in self.studentNameDict.keys():
            grades = self.studentGradeDict.get(uid)
            if grades is None:
                slices[0] += 1
            else:
                slices[len(grades)] += 1
        self.chart = CompletionPieChart(slices)

    def setupGradeVisualization(self):
        data = dict()
        for tid in self.testTypeDict.keys():
            distribution = [0] * 10
            data.setdefault(tid, distribution)

        for grade in self.studentGradeDict.values():
            for tid, grade in grade.items():
                distribution = data.get(tid)
                index = int(grade) // 10
                if index == 10:
                    index = 9
                distribution[index] += 1

        self.gradeVisualization = GradeVisualizationWidget(
            data, self.testTypeDict, self)

    @Slot()
    def on_btnCompletion_clicked(self):
        self.ui.stages.setCurrentIndex(0)

    @Slot()
    def on_btnGrade_clicked(self):
        self.ui.stages.setCurrentIndex(1)
