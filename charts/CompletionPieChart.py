"""
@file       : CompletionPie.py
@description: the pie chart illustrating test completion situation.
@date       : 2021/04/12 21:33:07
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QFont


class CompletionPieChart(QtCharts.QChart):
    def __init__(self, slicesValue):
        super().__init__()
        # setup series
        series = QtCharts.QPieSeries(self)
        count = len(slicesValue)
        series.append("全部未完成", slicesValue[0])
        for i in range(1, count - 1):
            label = "完成" + str(i) + "项"
            series.append(label, slicesValue[i])
        series.append("全部完成", slicesValue[count - 1])
        self.addSeries(series)

        # setup title
        self.setTitle("学生完成情况饼图")
        font = QFont()
        font.setFamily("Source Han Sans CN")
        font.setBold(True)
        font.setPixelSize(20)
        self.setTitleFont(font)
        # setup legend
        font.setPixelSize(14)
        font.setBold(False)
        self.legend().setFont(font)
        self.legend().markers()[0].setLabel("全部未完成")
        for i in range(1, count - 1):
            self.legend().markers()[1].setLabel("完成" + str(i) + "项")
        self.legend().markers()[count - 1].setLabel("全部未完成")
        self.legend().setAlignment(Qt.AlignBottom)

        # setup slice labels
        series.setLabelsPosition(QtCharts.QPieSlice.LabelPosition.LabelOutside)
        slices = series.slices()
        for slice in slices:
            value = slice.value()
            total = sum(slicesValue)
            labelText = str(int(slice.value())) + "人(" + str(
                round(value / total * 100, 1)) + "%)"
            slice.setLabel(labelText)
            slice.setLabelFont(font)

        # signal
        series.hovered.connect(self.changeSliceExplored)
        series.released.connect(self.changeSliceExplored)

    @Slot(QtCharts.QPieSlice, bool)
    def changeSliceExplored(self, slice: QtCharts.QPieSlice, isHovered: bool):
        if isHovered:
            slice.setExploded(True)
            slice.setLabelVisible(True)
        else:
            slice.setExploded(False)
            slice.setLabelVisible(False)
