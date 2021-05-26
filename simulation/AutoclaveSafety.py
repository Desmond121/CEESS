"""
@file       : AutoclaveSafety.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/02/29 10:01:54
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

import random
from PySide2.QtCore import QObject, Qt, Signal, Slot
from PySide2.QtGui import QBrush, QColor, QFont, QMovie, QPixmap
from PySide2.QtWidgets import (QGraphicsItem, QGraphicsPixmapItem,
                               QGraphicsScene, QGraphicsTextItem, QLabel,
                               QMessageBox, QPushButton, QWidget)

from simulation.generate.Ui_AutoclaveSafety import Ui_AutoclaveSafety

_RESOURCE_PATH = "./resources/img/simulation/autoclaveSafety/"


class AutoclaveSafety(QWidget):
    finishedSignal = Signal(int)
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AutoclaveSafety()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setupScene()

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

        # autoclave overview
        autoclaveItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "autoclave.png"))
        autoclaveItem.setPos(80, 75)
        autoclaveItem.setScale(0.4)
        scene.addItem(autoclaveItem)
        # autoclaveItem.setFlags(QGraphicsItem.ItemIsSelectable
        #                        | QGraphicsItem.ItemIsMovable)

        # pressure gauge text
        defaultText = "(________)"
        pressureGaugeTextItem = QGraphicsTextItem()
        font = QFont()
        font.setPixelSize(20)
        pressureGaugeTextItem.setFont(font)
        pressureGaugeTextItem.setPos(261, 83)
        pressureGaugeTextItem.setPlainText(defaultText)
        pressureGaugeTextItem.setDefaultTextColor(Qt.red)
        scene.addItem(pressureGaugeTextItem)
        pressureGaugeTextItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
        pressureGaugeTextItem.setData(Qt.UserRole, "( 压力表 )")
        # pressureGaugeTextItem.setFlag(QGraphicsItem.ItemIsMovable, True)

        # safety valve text
        safetyValveTextItem = QGraphicsTextItem()
        safetyValveTextItem.setFont(font)
        safetyValveTextItem.setPos(289, 144)
        safetyValveTextItem.setPlainText(defaultText)
        safetyValveTextItem.setDefaultTextColor(Qt.red)
        scene.addItem(safetyValveTextItem)
        safetyValveTextItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
        safetyValveTextItem.setData(Qt.UserRole, "( 安全阀 )")

        # thermometer measurement hole text
        thermometerTextItem = QGraphicsTextItem()
        thermometerTextItem.setFont(font)
        thermometerTextItem.setPos(293, 191)
        thermometerTextItem.setPlainText(defaultText)
        thermometerTextItem.setDefaultTextColor(Qt.red)
        scene.addItem(thermometerTextItem)
        thermometerTextItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
        thermometerTextItem.setData(Qt.UserRole, "( 热电偶插孔 )")

        # kettle cover text
        kettleCoverTextItem = QGraphicsTextItem()
        kettleCoverTextItem.setFont(font)
        kettleCoverTextItem.setPos(-4, 184)
        kettleCoverTextItem.setPlainText(defaultText)
        kettleCoverTextItem.setDefaultTextColor(Qt.red)
        scene.addItem(kettleCoverTextItem)
        kettleCoverTextItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
        kettleCoverTextItem.setData(Qt.UserRole, "( 釜盖 )")

        # needleValve text
        needleValveTextItem = QGraphicsTextItem()
        needleValveTextItem.setFont(font)
        needleValveTextItem.setPos(-1, 210)
        needleValveTextItem.setPlainText(defaultText)
        needleValveTextItem.setDefaultTextColor(Qt.red)
        scene.addItem(needleValveTextItem)
        needleValveTextItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
        needleValveTextItem.setData(Qt.UserRole, "( 针形阀 )")

        # kettle body text
        kettleBodyTextItem = QGraphicsTextItem()
        kettleBodyTextItem.setFont(font)
        kettleBodyTextItem.setPos(-8, 341)
        kettleBodyTextItem.setPlainText(defaultText)
        kettleBodyTextItem.setDefaultTextColor(Qt.red)
        scene.addItem(kettleBodyTextItem)
        kettleBodyTextItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
        kettleBodyTextItem.setData(Qt.UserRole, "( 釜体 )")

        self.textItemList = [
            pressureGaugeTextItem, kettleBodyTextItem, kettleCoverTextItem,
            needleValveTextItem, safetyValveTextItem, thermometerTextItem
        ]

        # setup List
        names = ["压力表", "安全阀", "热电偶插孔", "针形阀", "釜体", "釜盖"]
        self.ui.nameList.addItems(names)
        # hint info
        self.ui.textBrowser.append("[提示信息]\n单击图中括号，再左侧点击按钮填写组件名称。\n")

    def setupScene2(self):
        items = self.ui.graphicsView.items()
        for i in range(len(items) - 1):
            items[i].hide()

        scene = self.ui.graphicsView.scene()

        # 1
        btnOpenAutoclave = QPushButton()
        btnOpenAutoclave.setText("打开反应釜盖")
        btnOpenAutoclave.setAttribute(Qt.WA_NoSystemBackground)
        openAutoclaveItem = scene.addWidget(btnOpenAutoclave)

        btnFeeding = QPushButton()
        btnFeeding.setText("加入物料")
        btnFeeding.setAttribute(Qt.WA_NoSystemBackground)
        feedingItem = scene.addWidget(btnFeeding)

        btnCloseAutoclave = QPushButton()
        btnCloseAutoclave.setText("关上反应釜盖")
        btnCloseAutoclave.setAttribute(Qt.WA_NoSystemBackground)
        closeAutoclaveItem = scene.addWidget(btnCloseAutoclave)

        btnRightScrew = QPushButton()
        btnRightScrew.setText("按对角顺序均匀拧紧螺栓")
        btnRightScrew.setAttribute(Qt.WA_NoSystemBackground)
        rightScrewItem = scene.addWidget(btnRightScrew)

        btnWrongScrew = QPushButton()
        btnWrongScrew.setText("按顺时针顺序拧紧螺栓")
        btnWrongScrew.setAttribute(Qt.WA_NoSystemBackground)
        wrongScrewItem = scene.addWidget(btnWrongScrew)

        # 6
        btnInTube = QPushButton()
        btnInTube.setText("确保2个阀门是关闭后，接入充气管")
        btnInTube.setAttribute(Qt.WA_NoSystemBackground)
        inTubeItem = scene.addWidget(btnInTube)

        # Prv = pressure reducing valve
        btnOpenPrv = QPushButton()
        btnOpenPrv.setText("打开减压阀")
        btnOpenPrv.setAttribute(Qt.WA_NoSystemBackground)
        openPrvItem = scene.addWidget(btnOpenPrv)

        btnOpenInput = QPushButton()
        btnOpenInput.setText("打开进气阀，向釜内通入气体")
        btnOpenInput.setAttribute(Qt.WA_NoSystemBackground)
        openInputItem = scene.addWidget(btnOpenInput)

        btnClosePrv = QPushButton()
        btnClosePrv.setText("关闭减压阀，等待加压至目标压力")
        btnClosePrv.setAttribute(Qt.WA_NoSystemBackground)
        closePrvItem = scene.addWidget(btnClosePrv)

        btnCloseInput = QPushButton()
        btnCloseInput.setText("关闭进气阀")
        btnCloseInput.setAttribute(Qt.WA_NoSystemBackground)
        closeInputItem = scene.addWidget(btnCloseInput)

        # 11
        btnHeat = QPushButton()
        btnHeat.setText("放入加热套中，接上热电偶，打开搅拌器")
        btnHeat.setAttribute(Qt.WA_NoSystemBackground)
        heatItem = scene.addWidget(btnHeat)

        btnWaitTemp = QPushButton()
        btnWaitTemp.setText("等待温度降至常温")
        btnWaitTemp.setAttribute(Qt.WA_NoSystemBackground)
        waitTempItem = scene.addWidget(btnWaitTemp)

        # 13
        btnReducePressure = QPushButton()
        btnReducePressure.setText("打开减压阀泄压至常压")
        btnReducePressure.setAttribute(Qt.WA_NoSystemBackground)
        reducePressureItem = scene.addWidget(btnReducePressure)

        self.allButton = [
            openAutoclaveItem, feedingItem, closeAutoclaveItem, inTubeItem,
            rightScrewItem, wrongScrewItem, openInputItem, openPrvItem,
            heatItem, waitTempItem, reducePressureItem, closePrvItem,
            closeInputItem
        ]
        # first one in tuple is correct answer
        self.stepButtonGroup = [
            (openAutoclaveItem, ),  # step 0
            (feedingItem, closeAutoclaveItem),  # step 1
            (closeAutoclaveItem, ),  # step 2
            (rightScrewItem, inTubeItem, wrongScrewItem),  # step 3
            (inTubeItem, openInputItem),  # step 4
            (openPrvItem, openInputItem),  # step 5
            (openInputItem, ),  # step 6
            (closePrvItem, ),  # step 7
            (closeInputItem, heatItem),  # step 8
            (heatItem, ),  # step 9
            (waitTempItem, openPrvItem, openAutoclaveItem),  # step 10
            (reducePressureItem, openAutoclaveItem),  # step 11
            (openAutoclaveItem, )  # step 12
        ]

        # gif movies
        # setup the fan gif.
        self.moviesGroup = []
        for i in range(14):
            movie = QMovie(_RESOURCE_PATH + "step" + str(i) + ".gif")
            self.moviesGroup.append(movie)

        self.movieLabel = QLabel()
        self.movieLabel.setAttribute(Qt.WA_NoSystemBackground)
        movieItem = scene.addWidget(self.movieLabel)
        movieItem.setScale(1)
        movieItem.setPos(35, 0)

        self.infoList = [
            "等待开始",
            "打开反应釜盖",
            "加入反应物料",
            "关闭反应釜盖",
            "按对角线均匀的上紧螺栓",
            "确认进气阀的减压阀都关闭后，接入充气管",
            "打开减压阀",
            "打开进气阀，向内充气置换府内气体",
            "关闭减压阀，等待压力升至目标压力",
            "压力已升至目标值，关闭进气阀",
            "放入加热套中，调节各项设置，开始反应",
            "反应完成，等待温度降至常温。",
            "打开减压阀，将压力降至常压",
            "打开阀盖，结束",
        ]

        self.currentStep = 0

    def nextStep(self):
        for item in self.allButton:
            item.hide()

        # setup button of each step.
        if self.currentStep < len(self.stepButtonGroup):
            i = 0
            bottons = list(self.stepButtonGroup[self.currentStep])
            random.shuffle(bottons)
            for item in bottons:
                item.setPos(20, i * 50 + 230)
                item.show()
                item.setScale(1.8)
                i += 1

            self.setConnect()
        else:
            self.setFinished()

        movie = self.moviesGroup[self.currentStep]
        self.movieLabel.setMovie(movie)
        movie.start()

        self.ui.operationList.addItem(self.infoList[self.currentStep])
        self.currentStep += 1

    def setConnect(self):
        # remove last connection
        if self.currentStep != 0:
            lastBottonItems = self.stepButtonGroup[self.currentStep - 1]
            for item in lastBottonItems:
                QObject.disconnect(item.widget(), None, None, None)

        bottonItems = self.stepButtonGroup[self.currentStep]
        # right answer
        bottonItems[0].widget().clicked.connect(self.nextStep)
        # other answers
        for i in range(1, len(bottonItems)):
            bottonItems[i].widget().clicked.connect(self.wrongAnswer)

    def wrongAnswer(self):
        if self.ui.lcdNumber.intValue() == 1:
            self.ui.lcdNumber.display(self.ui.lcdNumber.intValue() - 1)
            QMessageBox.warning(self, "CEESS-警告", "错误过程！无剩余次数！")
            self.setFinished()
        else:
            QMessageBox.warning(self, "CEESS-警告", "错误过程")
            self.ui.lcdNumber.display(self.ui.lcdNumber.intValue() - 1)

    def setFinished(self):
        self.ui.graphicsView.setEnabled(False)
        count = self.ui.lcdNumber.intValue()
        self.ui.textBrowser.append("[完成信息]\n剩余机会：" + str(count) + "次，得分：" +
                                   str(count * 10) + "分\n")
        self.score = self.score - 50 + count * 10
        self.ui.textBrowser.append("[成绩信息]\n最终得分：" + str(self.score))
        self.ui.textBrowser.append("\n练习已完成。退出当前窗口以上传成绩。")
        self.finishedSignal.emit(self.score)

    @Slot()
    def on_nameList_itemClicked(self):
        items = self.ui.graphicsView.scene().selectedItems()
        if len(items) != 0:
            item = items[0]
            answer = self.ui.nameList.selectedItems()[0].text()
            item.setPlainText("( " + answer + " )")

    @Slot()
    def on_btnCheck_clicked(self):
        errorCount = 0
        errorList = list()
        for item in self.textItemList:
            if item.data(Qt.UserRole) != item.toPlainText():
                errorCount += 1
                errorList.append(item)

        for item in errorList:
            item.setPlainText(item.data(Qt.UserRole))
            item.setDefaultTextColor(Qt.green)

        if errorCount == 0:
            self.ui.textBrowser.append("[完成信息]\n全部正确。\n")
        else:
            self.ui.textBrowser.append("[错误信息]\n正确答案已在图中用绿色改正。\n")

        if errorCount > 5:
            errorCount = 5
        self.score -= errorCount * 10

        self.ui.btnNext.setEnabled(True)
        self.ui.nameList.setEnabled(False)
        self.ui.btnCheck.setEnabled(False)

    @Slot()
    def on_btnNext_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.setupScene2()
        self.nextStep()

    # @Slot()
    # def on_btnNext_clicked(self):
    #     items = self.ui.graphicsView.items()
    #     for item in items:
    #         if item.isSelected():
    #             print(item.pos())