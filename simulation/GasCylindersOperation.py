"""
@file       : GasCylindersOperation.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/02/26 15:19:11
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
import random

from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import QBrush, QColor, QFont, QPen, QPixmap
from PySide2.QtWidgets import (QGraphicsEllipseItem, QGraphicsItem,
                               QGraphicsPixmapItem, QGraphicsRectItem,
                               QGraphicsScene, QGraphicsTextItem,
                               QListWidgetItem, QWidget)

from simulation.generate.Ui_GasCylindersOperation import \
    Ui_GasCylindersOperation

_RESOURCE_PATH = "./resources/img/simulation/gasCylinderOperation/"


class GasCylindersOperation(QWidget):
    finishedSignal = Signal(int)
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GasCylindersOperation()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setupScene()
        self.setupMistakeList()

        # setup text browser
        font = QFont()
        font.setPixelSize(14)
        font.setFamilies("Source Han Sans CN")
        self.ui.textBrowser.setFont(font)
        infoStr = "[提示信息]\n左图中是运输乙炔和氧气瓶的操作，请在左边选择操作中存在的错误。\n"
        self.ui.textBrowser.setText(infoStr)

    def setupScene(self):
        # setup background
        self.ui.graphicsView.setBackgroundBrush(
            QBrush(QColor(0x566280), Qt.SolidPattern))

        # setup scene
        scene = QGraphicsScene(0, 0, 450, 500)
        self.ui.graphicsView.setScene(scene)

        # logo
        logoItem = QGraphicsPixmapItem(QPixmap("./resources/img/icon.svg"))
        logoItem.setPos(380, 450)
        logoItem.setScale(0.3)
        scene.addItem(logoItem)
        logoItem.setFlag(QGraphicsItem.ItemIsSelectable, True)

        # gas cylinder Transport
        transportItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "transport.png"))
        transportItem.setScale(0.6)
        transportItem.setPos(130, 45)
        scene.addItem(transportItem)

    def setupScene2(self):
        # hide item of scene1
        self.ui.graphicsView.items()[0].hide()

        # get scene
        scene = self.ui.graphicsView.scene()

        # pressure reducers
        pressureReducerItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "barometer.png"))
        pressureReducerItem.setScale(0.08)
        pressureReducerItem.setPos(340, 50)
        scene.addItem(pressureReducerItem)
        # barometerItem.setFlag(QGraphicsItem.ItemIsMovable, True)

        # cylinder
        cylinderItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "cylinder.png"))
        cylinderItem.setScale(0.6)
        cylinderItem.setPos(290, 100)
        scene.addItem(cylinderItem)
        # cylinderItem.setFlag(QGraphicsItem.ItemIsMovable, True)

        # window
        windowItem = QGraphicsPixmapItem(QPixmap(_RESOURCE_PATH +
                                                 "window.png"))
        windowItem.setScale(0.3)
        windowItem.setPos(0, 30)
        scene.addItem(windowItem)
        # windowItem.setFlag(QGraphicsItem.ItemIsMovable, True)

        # wrong place
        wrongPlaceItem = QGraphicsRectItem(0, 0, 125, 125)
        wrongPlaceItem.setPos(0, 150)
        pen = QPen()
        pen.setStyle(Qt.PenStyle.DashLine)
        wrongPlaceItem.setPen(pen)
        scene.addItem(wrongPlaceItem)
        # wrongItem.setFlag(QGraphicsItem.ItemIsMovable, True)

        # right place
        rightPlaceItem = QGraphicsRectItem(0, 0, 125, 125)
        rightPlaceItem.setPos(130, 150)
        rightPlaceItem.setPen(pen)
        scene.addItem(rightPlaceItem)
        # rightItem.setFlag(QGraphicsItem.ItemIsMovable, True)

        # place hint
        placeHintItem = QGraphicsTextItem("气瓶应该摆放在不会被太阳暴晒\n的地方，更应远离高温热源。")
        placeHintItem.setPos(10, 260)
        scene.addItem(placeHintItem)
        placeHintItem.hide()

        # right hint
        rightHintItem = QGraphicsPixmapItem(
            QPixmap("./resources/img/btnTrue.svg"))
        rightHintItem.setPos(150, 160)
        rightHintItem.setScale(0.5)
        rightHintItem.hide()
        scene.addItem(rightHintItem)

        # wrong hint
        wrongHintItem = QGraphicsPixmapItem(
            QPixmap("./resources/img/btnFalse.svg"))
        wrongHintItem.setPos(20, 160)
        wrongHintItem.setScale(0.5)
        wrongHintItem.hide()
        scene.addItem(wrongHintItem)

        # pressure reducer hint
        pressureReducerHintItem = QGraphicsEllipseItem(0, 0, 120, 120)
        pressureReducerHintItem.setPos(330, 40)
        pen = QPen()
        pen.setColor(Qt.red)
        pen.setWidth(2)
        pressureReducerHintItem.setPen(pen)
        scene.addItem(pressureReducerHintItem)
        pressureReducerHintItem.hide()

        # pressure reducer Valve hint
        pressureReducerValveHintItem = QGraphicsEllipseItem(0, 0, 65, 45)
        pressureReducerValveHintItem.setPos(355, 110)
        pen = QPen()
        pen.setColor(Qt.red)
        pen.setWidth(2)
        pressureReducerValveHintItem.setPen(pen)
        scene.addItem(pressureReducerValveHintItem)
        pressureReducerValveHintItem.hide()

        # cylinder valve hint
        cylinderValveHintItem = QGraphicsEllipseItem(0, 0, 45, 65)
        cylinderValveHintItem.setPos(305, 90)
        pen = QPen()
        pen.setColor(Qt.red)
        pen.setWidth(2)
        cylinderValveHintItem.setPen(pen)
        scene.addItem(cylinderValveHintItem)
        cylinderValveHintItem.hide()

        # barometer hint
        barometerHintItem = QGraphicsRectItem(0, 0, 45, 45)
        barometerHintItem.setPos(395, 50)
        pen = QPen()
        pen.setColor(Qt.red)
        pen.setWidth(2)
        barometerHintItem.setPen(pen)
        scene.addItem(barometerHintItem)
        barometerHintItem.hide()

        self.interactiveItems = [
            rightHintItem, wrongHintItem, placeHintItem, barometerHintItem,
            cylinderValveHintItem, pressureReducerHintItem,
            pressureReducerValveHintItem
        ]

        self.interactiveItemsDict = {
            0: (rightHintItem, wrongHintItem, placeHintItem),
            2: (pressureReducerHintItem, ),
            -2: (pressureReducerHintItem, ),
            3: (cylinderValveHintItem, ),
            -3: (cylinderValveHintItem, ),
            4: (pressureReducerValveHintItem, barometerHintItem),
            -4: (cylinderValveHintItem, barometerHintItem),
            5: (cylinderValveHintItem, ),
            6: (pressureReducerHintItem, ),
            7: (cylinderValveHintItem, barometerHintItem),
            -7: (cylinderValveHintItem, )
        }

        self.setupOperationList()

    def setupMistakeList(self):
        transportMistakes = [
            "气瓶没有采用横置运输。", "气瓶运输时没有固定在运输推车上。", "气瓶运输时没有将阀门卸下。",
            "气瓶运输时没有将安全盖盖上。", "氧气和乙炔瓶可以同时运输，但是需要用橡胶圈固定。", "氧气和乙炔瓶不能同时运输。",
            "每辆推车次只能运输一个气瓶。", "氧气瓶和乙炔瓶同时运输时需要涂抹沥青保护瓶身。", "运输时不应该单手推动推车。",
            "乙炔瓶上没有防震胶圈。"
        ]

        self.transportAnswers = [
            False, True, False, True, False, True, False, False, True, True
        ]  # correct selections

        for mistake in transportMistakes:
            self.ui.mistakeList.addItem(mistake)

    def setupOperationList(self):
        # symbol + - means right or wrong, value define the right sequence.
        self.operations = [("对气瓶和周围环境进行安全检查，将气瓶放置与合适位置。", 0),
                           ("将气瓶、减压器和实验装置用气管连接好。", 1), ("站立在正对减压器的位置。", -2),
                           ("远离减压器正对的位置。", 2), ("缓慢旋开气瓶阀门。", 3),
                           ("迅速旋开气瓶阀门", -3), ("调节减压阀，将压力调整到实验要求值。", 4),
                           ("调节气瓶阀，将压力调整到实验要求值", -4), ("使用完毕后，先关闭气瓶阀门。", 5),
                           ("待减压器中气体逸尽后，再关闭减压阀。", 6),
                           ("最后检查气瓶阀门是否关闭完全（观察阀门是否拧紧）。", -7),
                           ("最后检查气瓶阀门是否关闭完全（观察减压表上压力是否归零）。", 7)]

        random.shuffle(self.operations)

        for operation in self.operations:
            item = QListWidgetItem()
            item.setText(operation[0])
            item.setData(Qt.UserRole, operation[1])
            self.ui.operationList.addItem(item)

    @Slot()
    def on_btnNext_clicked(self):
        indexes = self.ui.mistakeList.selectedIndexes()
        selected = set()
        for index in indexes:
            selected.add(index.row())

        errorCount = 0
        errorStr = "[错误信息]\n"
        errorStrList = [
            "-气瓶不能横向放置", "-气瓶需要用半圆支架或者绳圈固定在运输推车上", "-气瓶运输时需要盖上安全帽，而不是卸下阀门",
            "-气瓶运输时需要盖上安全帽", "-氧气和乙炔瓶严禁放在一起", "-氧气和乙炔瓶严禁放在一起",
            "-合适规格的推车可以一次运输多个气瓶", "-氧气瓶不能沾染油脂和沥青,因为可能造成起火事故。",
            "-运输时单手推车可能有失控风险", "-为了避免碰撞、跌到而引起爆炸，因此乙炔瓶必须配防震圈。"
        ]

        missCount = 0  # amount of correct answers which are not selected.
        errorCount = 0  # amount of wrong answers which are selected.
        for i in range(self.ui.mistakeList.count()):
            if self.transportAnswers[i] is True:
                if i not in selected:
                    errorStr += errorStrList[i] + "\n"
                    missCount += 1
            else:
                if i in selected:
                    errorStr += errorStrList[i] + "\n"
                    missCount += 1
        if missCount + errorCount > 5:
            errorCount = 5
        else:
            errorCount = missCount + errorCount

        if errorCount != 0:
            self.score -= errorCount * 10
            self.ui.textBrowser.append(errorStr)

        self.ui.stackedWidget.setCurrentIndex(1)

        # hint messages
        hintStr = "[提示信息]\n请在左边的操作中去除错误的操作，并拖拽各操作进行排序。\n"
        self.ui.textBrowser.append(hintStr)

        self.setupScene2()

    @Slot()
    def on_btnFinished_clicked(self):
        items = self.ui.graphicsView.items()
        for item in items:
            if item.isVisible():
                print(item.pos())

        for i in range(self.ui.operationList.count()):
            item = self.ui.operationList.item(i)

    @Slot(QListWidgetItem)
    def on_operationList_itemClicked(self, item: QListWidgetItem):
        itemId = item.data(Qt.UserRole)
        for item in self.interactiveItems:
            item.hide()
        itemList = self.interactiveItemsDict.get(itemId)
        if itemList is not None:
            for item in itemList:
                item.show()

    @Slot()
    def on_btnRedo_clicked(self):
        for item in self.interactiveItems:
            item.hide()

        self.ui.operationList.clear()
        for operation in self.operations:
            item = QListWidgetItem()
            item.setText(operation[0])
            item.setData(Qt.UserRole, operation[1])
            self.ui.operationList.addItem(item)

    @Slot()
    def on_btnDelete_clicked(self):
        Items = self.ui.operationList.selectedIndexes()
        for item in Items:
            row = item.row()
            self.ui.operationList.takeItem(row)

    @Slot()
    def on_btnFinished_clicked(self):
        errorCount = 0
        errorStr = "[错误信息]\n"
        errorInfo = {
            -2: "-站立在正对减压器的位置十分危险。",
            -3: "-必须缓慢旋开气瓶阀门。",
            -4: "-应当通过减压阀调节到所需的压力值。",
            -7: "-需要观察减压器上的压力表数值确定是否完全关闭（减压表压力归零）。"
        }
        result = list()
        for row in range(self.ui.operationList.count()):
            item = self.ui.operationList.item(row)
            result.append(item.data(Qt.UserRole))

        for num in result:
            error = errorInfo.get(num)
            if error is not None:
                errorCount += 1
                errorStr += error + "\n"

        if result != [0, 1, 2, 3, 4, 5, 6, 7]:
            errorCount += 1
            if errorCount != 1:
                errorStr += "\n"
            errorStr += "正确的顺序为：\n\
1.对气瓶和周围环境进行安全检查，将气瓶放置与合适位置。\n\
2.将气瓶、减压器和实验装置用气管连接好。\n\
3.缓慢旋开气瓶阀门。\n\
4.调节减压阀，将压力调整到实验要求值。\n\
5.使用完毕后，先关闭气瓶阀门。\n\
6.待减压器中气体逸尽后，再关闭减压阀。\n\
7.最后检查气瓶阀门是否关闭完全（观察减压表上压力是否归零）。\n"

        self.score -= errorCount * 10
        if errorCount != 0:
            self.ui.textBrowser.append(errorStr)

        # set finish status
        self.ui.btnDelete.setDisabled(True)
        self.ui.btnFinished.setDisabled(True)
        self.ui.btnRedo.setDisabled(True)
        self.finishedSignal.emit(self.score)
        self.ui.textBrowser.append("成绩: " + str(self.score) + "分")
        self.ui.textBrowser.append("模拟完成，关闭窗口即可上传成绩。\n")


1
