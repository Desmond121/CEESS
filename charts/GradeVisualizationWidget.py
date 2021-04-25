"""
@file       : GradeVisualization.py
@description: this is a Q3DBar class to show student grade distribution
@date       : 2021/04/15 15:50:37
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

import sys

from PySide2.QtCore import QMargins, Qt
from PySide2.QtDataVisualization import QtDataVisualization
from PySide2.QtGui import QColor
from PySide2.QtWidgets import (QApplication, QMainWindow, QSizePolicy,
                               QVBoxLayout, QWidget)


class GradeVisualizationWidget(QWidget):
    def __init__(self, data: dict, testTypeDict: dict, parent=None):
        """
        {data}-- dict
        data = {tid: [amount(0~10),amount(10~20),..., amount(90~100)], ...}
        """
        super().__init__(parent)
        self.setupBars(data, testTypeDict)
        self.setupBarsFormat()

        self.container = QWidget.createWindowContainer(self.bars)

        if not self.bars.hasContext():
            print("Couldn't initialize the OpenGL context.")
            sys.exit(-1)

        camera = self.bars.scene().activeCamera()
        camera.setYRotation(45)

        self.container.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Expanding)
        self.container.setFocusPolicy(Qt.StrongFocus)

        self.vboxLayout = QVBoxLayout(self)
        self.vboxLayout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.vboxLayout.addWidget(self.container)

    def setupBars(self, data: dict, testTypeDict: dict):

        # setup dict
        # this dict help to find row number by tid
        # RowToTidDict = {row: tid, ...}
        rowToTidDict = dict()

        # create bars
        self.bars = QtDataVisualization.Q3DBars()

        # setup column
        self.columnAxis = QtDataVisualization.QCategory3DAxis()
        self.columnAxis.setTitle("成绩区间(分)")
        self.columnAxis.setTitleVisible(True)
        colLabels = list()
        for i in range(0, 100, 10):
            colLabels.append(str(i) + "-" + str(i + 10))
        self.columnAxis.setLabels(colLabels)
        self.columnAxis.setLabelAutoRotation(30)

        # setup row
        self.rowAxis = QtDataVisualization.QCategory3DAxis()
        self.rowAxis.setTitle("测试名称")
        self.rowAxis.setTitleVisible(True)
        rowIndex = 0
        rowLabels = list()
        for tid, typeName in testTypeDict.items():
            rowToTidDict.setdefault(rowIndex, tid)
            rowLabels.append(typeName)
            rowIndex += 1
        self.rowAxis.setLabels(rowLabels)
        self.rowAxis.setLabelAutoRotation(30)

        # setup value axis
        self.valueAxis = QtDataVisualization.QValue3DAxis()
        self.valueAxis.setTitle("人数(个)")
        self.valueAxis.setTitleVisible(True)
        self.valueAxis.setLabelFormat("%d")

        # set all axis
        self.bars.setRowAxis(self.rowAxis)
        self.bars.setColumnAxis(self.columnAxis)
        self.bars.setValueAxis(self.valueAxis)

        # setup series of bars (import data to series)
        self.series = QtDataVisualization.QBar3DSeries()
        """
        {arrayData}:
        row = [amount(0~10),amount(10~20),..., amount(90~100)]
        arrayData = [row_1, row_2, ..., row_n]
        """
        arrayData = list()
        for i in range(len(data)):
            tid = rowToTidDict.get(i)
            arrayData.append(data.get(tid))
        self.series.dataProxy().addRows(self.dataToBarDataArray(arrayData))
        self.bars.setPrimarySeries(self.series)

    def setupBarsFormat(self):
        # behavior
        self.bars.setSelectionMode(
            QtDataVisualization.QAbstract3DGraph.SelectionItemAndRow)
        # appearance
        theme = self.bars.activeTheme()
        theme.setType(QtDataVisualization.Q3DTheme.ThemeQt)
        theme.setLabelBackgroundEnabled(False)
        theme.setLabelTextColor(QColor(0x4B84CA))
        theme.setWindowColor(QColor(0x1F2430))
        theme.setGridLineColor(QColor(0xFD7300))
        theme.setBackgroundEnabled(False)
        theme.setColorStyle(
            QtDataVisualization.Q3DTheme.ColorStyle.ColorStyleObjectGradient)
        # theme.setBaseColors([
        #     QColor(0x3b789a),
        #     QColor(0x70afce),
        #     QColor(0xa5def1),
        #     QColor(0xffffff)
        # ])
        # theme.setAmbientLightStrength(0.3)
        # theme.setBackgroundColor(QColor(0x8EDAF3))
        # theme.setBackgroundEnabled(True)
        # theme.setColorStyle(
        #     QtDataVisualization.Q3DTheme.ColorStyle.ColorStyleObjectGradient)
        # theme.setFont(QFont("Source Han Sans CN", 35))
        # theme.setGridEnabled(True)
        # theme.setGridLineColor(QColor(0x6bc3e1))
        # theme.setHighlightLightStrength(3.0)
        # theme.setLabelBackgroundColor(QColor(0x9EB5EC))
        # theme.setLabelBackgroundEnabled(True)
        # theme.setLabelBorderEnabled(True)
        # theme.setLabelTextColor(QColor(0x404044))
        # theme.setLightColor(Qt.white)
        # theme.setLightStrength(6.0)
        # theme.setMultiHighlightColor(QColor(0xFFFFFF))
        # theme.setSingleHighlightColor(QColor(0xFFFFFF))
        # theme.setWindowColor(QColor(0x34458B))

    def dataToBarDataRow(self, data):
        return list(QtDataVisualization.QBarDataItem(d) for d in data)

    def dataToBarDataArray(self, data):
        return list(self.dataToBarDataRow(row) for row in data)


# ! for testing
if __name__ == '__main__':
    testTypeDict = {1: "安全测试", 2: "气瓶管理"}
    data = {
        1: [0, 0, 0, 10, 20, 30, 40, 23, 22, 5],
        2: [4, 4, 4, 8, 10, 30, 30, 33, 20, 7]
    }
    app = QApplication(sys.argv)

    mainWin = QMainWindow()
    widget = GradeVisualizationWidget(data, testTypeDict)
    mainWin.setCentralWidget(widget)
    mainWin.showMaximized()
    mainWin.show()
    sys.exit(app.exec_())
