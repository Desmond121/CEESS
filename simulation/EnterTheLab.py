"""
@file       : EnterTheLab.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/04/25 14:39:46
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import QBrush, QColor, QFont, QMovie, QPixmap
from PySide2.QtWidgets import (QGraphicsItem, QGraphicsPixmapItem,
                               QGraphicsScene, QLabel, QWidget)

from simulation.generate.Ui_enterTheLab import Ui_EnterTheLab

_RESOURCE_PATH = "./resources/img/simulation/enterTheLab/"

# item indexes
_TROUSERS = 0
_SHORTS = 1
_GLOVES = 2
_GLASSES = 3
_CLOTHES = 4
_SANDALS = 5
_SHOES = 6

# movie indexes
_FAN = 0
_WINDOW = 1
_SWITCH = 2


class EnterTheLab(QWidget):
    # signal
    finishedSignal = Signal(int)

    simulationIndex = 1
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EnterTheLab()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setupScene()

        # setup text browser
        font = QFont()
        font.setPixelSize(14)
        font.setFamilies("Source Han Sans CN")
        self.ui.textBrowser.setFont(font)
        infoStr = "[提示信息]\n请在左边选择合理的实验室着装后，点击“下一步”。\n"
        self.ui.textBrowser.setText(infoStr)

    def setupScene(self):
        # setup background
        self.ui.graphicsView.setBackgroundBrush(
            QBrush(QColor(0x566280), Qt.SolidPattern))

        # setup scene
        scene = QGraphicsScene(0, 0, 500, 550)
        self.ui.graphicsView.setScene(scene)

        # background
        backgroundItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "background.png"))
        backgroundItem.setScale(0.7)
        backgroundItem.setPos(80, 160)
        scene.addItem(backgroundItem)

        # logo
        logoItem = QGraphicsPixmapItem(QPixmap("./resources/img/icon.svg"))
        logoItem.setPos(450, 490)
        logoItem.setScale(0.3)
        scene.addItem(logoItem)

        # body
        bodyItem = QGraphicsPixmapItem(QPixmap(_RESOURCE_PATH + "body.png"))
        bodyItem.setScale(0.3)
        bodyItem.setPos(185, 100)
        scene.addItem(bodyItem)

        # trousers
        trousersItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "trousers.png"))
        trousersItem.setScale(0.07)
        trousersItem.setPos(220, 250)
        scene.addItem(trousersItem)
        trousersItem.hide()

        # shorts
        shortsItem = QGraphicsPixmapItem(QPixmap(_RESOURCE_PATH +
                                                 "shorts.png"))
        shortsItem.setScale(0.08)
        shortsItem.setPos(217, 263)
        scene.addItem(shortsItem)
        shortsItem.hide()

        # gloves
        glovesItem = QGraphicsPixmapItem(QPixmap(_RESOURCE_PATH +
                                                 "gloves.png"))
        glovesItem.setScale(0.3)
        glovesItem.setPos(183, 240)
        scene.addItem(glovesItem)
        glovesItem.hide()

        # glasses
        glassesItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "glasses.png"))
        glassesItem.setScale(0.05)
        glassesItem.setPos(226, 95)
        scene.addItem(glassesItem)
        glassesItem.hide()

        # clothes
        clothesItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "clothes.png"))
        clothesItem.setScale(0.275)
        clothesItem.setPos(190, 155)
        scene.addItem(clothesItem)
        clothesItem.hide()

        # sandals
        sandalsItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "sandals.png"))
        sandalsItem.setScale(0.3)
        sandalsItem.setPos(210, 411)
        scene.addItem(sandalsItem)
        # sandalsItem.setFlag(QGraphicsItem.ItemIsMovable, True)
        sandalsItem.hide()

        # shoes
        shoesItem = QGraphicsPixmapItem(QPixmap(_RESOURCE_PATH + "shoes.png"))
        shoesItem.setScale(0.3)
        shoesItem.setPos(209, 404)
        scene.addItem(shoesItem)
        shoesItem.setFlag(QGraphicsItem.ItemIsMovable, True)
        shoesItem.hide()

        self.items = (trousersItem, shortsItem, glovesItem, glassesItem,
                      clothesItem, sandalsItem, shoesItem)

        # for item in self.items:
        #     item.setFlag(QGraphicsItem.ItemIsMovable, True)

        # setup the fan gif.
        fanMovie = QMovie(_RESOURCE_PATH + "fan.gif")
        fanMovie.setCacheMode(QMovie.CacheAll)
        fanMovie.setSpeed(500)
        fanLabel = QLabel()
        fanLabel.setAttribute(Qt.WA_NoSystemBackground)
        fanLabel.setMovie(fanMovie)
        fanItem = self.ui.graphicsView.scene().addWidget(fanLabel)
        fanItem.setScale(0.2)
        fanItem.setPos(450, 0)
        fanMovie.jumpToFrame(0)

        # setup window gif
        windowMovie = QMovie(_RESOURCE_PATH + "window.gif")
        windowMovie.setCacheMode(QMovie.CacheAll)
        windowMovie.setSpeed(100)
        windowLabel = QLabel()
        windowLabel.setAttribute(Qt.WA_NoSystemBackground)
        windowLabel.setMovie(windowMovie)
        windowItem = self.ui.graphicsView.scene().addWidget(windowLabel)
        windowItem.setScale(0.3)
        windowItem.setPos(50, 50)
        windowMovie.jumpToFrame(0)

        # setup switch gif
        switchMovie = QMovie(_RESOURCE_PATH + "switch.gif")
        switchMovie.setCacheMode(QMovie.CacheAll)
        switchLabel = QLabel()
        switchLabel.setAttribute(Qt.WA_NoSystemBackground)
        switchLabel.setMovie(switchMovie)
        switchItem = self.ui.graphicsView.scene().addWidget(switchLabel)
        switchItem.setScale(0.2)
        switchItem.setPos(460, 100)
        switchMovie.jumpToFrame(0)

        self.movie = (fanMovie, windowMovie, switchMovie)

    @Slot(bool)
    def on_btnShoes_clicked(self, isChecked):
        self.items[_SHOES].setVisible(isChecked)
        self.items[_SANDALS].setVisible(not isChecked)

    @Slot(bool)
    def on_btnSandals_clicked(self, isChecked):
        self.on_btnShoes_clicked(not isChecked)

    @Slot(bool)
    def on_btnTrousers_clicked(self, isChecked):
        self.items[_TROUSERS].setVisible(isChecked)
        self.items[_SHORTS].setVisible(not isChecked)

    @Slot(bool)
    def on_btnShorts_clicked(self, isChecked):
        self.on_btnTrousers_clicked(not isChecked)

    @Slot()
    def on_btnClothes_clicked(self):
        self.items[_CLOTHES].setVisible(self.ui.btnClothes.isChecked())

    @Slot()
    def on_btnGlasses_clicked(self):
        self.items[_GLASSES].setVisible(self.ui.btnGlasses.isChecked())

    @Slot()
    def on_btnGloves_clicked(self):
        self.items[_GLOVES].setVisible(self.ui.btnGloves.isChecked())

    @Slot()
    def on_btnSwitch_clicked(self):
        if self.ui.btnSwitch.isChecked():
            self.movie[_SWITCH].jumpToFrame(1)
        else:
            self.movie[_SWITCH].jumpToFrame(0)

    @Slot()
    def on_btnFan_clicked(self):
        if self.ui.btnFan.isChecked():
            self.movie[_FAN].start()
        else:
            self.movie[_FAN].stop()

    @Slot()
    def on_btnWindow_clicked(self):
        if self.ui.btnWindow.isChecked():
            self.movie[_WINDOW].start()
        else:
            self.movie[_WINDOW].jumpToFrame(0)

    @Slot()
    def on_btnNext_clicked(self):
        errorCount = 0
        errorStr = "[错误信息]\n"
        if not self.items[_CLOTHES].isVisible():
            errorStr += "-未穿着实验服。\n"
            errorCount += 1
            self.score -= 10
        if not self.items[_GLOVES].isVisible():
            errorStr += "-未穿着防护眼镜.\n"
            errorCount += 1
            self.score -= 10
        if not self.items[_GLOVES].isVisible():
            errorStr += "-未穿着实验手套。\n"
            errorCount += 1
            self.score -= 10
        if not self.items[_TROUSERS].isVisible():
            errorStr += "-未穿着长裤。\n"
            errorCount += 1
            self.score -= 10
        if not self.items[_SHOES].isVisible():
            errorStr += "-实验室内不能光脚或穿着凉鞋。\n"
            errorCount += 1
            self.score -= 10

        if errorCount != 0:
            self.ui.textBrowser.append(errorStr)

        self.ui.stackedWidget.setCurrentIndex(1)

    @Slot()
    def on_btnFinished_clicked(self):
        errorCount = 0
        errorStr = "[错误信息]\n"
        if not self.ui.btnWindow.isChecked():
            errorStr += "-未打开实验室窗户通风。\n"
            errorCount += 1
            self.score -= 10
        if not self.ui.btnFan.isChecked():
            errorStr += "-未打开通风橱。\n"
            errorCount += 1
            self.score -= 10
        if not self.ui.btnSwitch.isChecked():
            errorStr += "-未打开电源总闸。\n"
            errorCount += 1
            self.score -= 10

        if errorCount != 0:
            self.ui.textBrowser.append(errorStr)

        if self.score == 20:
            self.score = 0

        # set finished status
        self.ui.btnFinished.setDisabled(True)
        self.ui.btnFinished.setText("已完成")
        self.finishedSignal.emit(self.score)
        self.ui.textBrowser.append("成绩: " + str(self.score) + "分")
        self.ui.textBrowser.append("模拟完成，关闭窗口即可上传成绩。\n")


# @Slot()
# def on_btnNext_clicked(self):
#     items = self.ui.graphicsView.items()
#     for item in items:
#         if item.isVisible():
#             print(item.pos())

# @Slot()
# def on_pushButton_2_clicked(self):
#     for item in self.items:
#         if item.isVisible():
#             item.hide()
#         else:
#             item.show()
