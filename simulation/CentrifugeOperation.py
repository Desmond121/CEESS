"""
@file       : CentrifugeOperation.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/03/23 19:01:54
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

from simulation.generate.Ui_CentrifugeOperation import Ui_CentrifugeOperation

_RESOURCE_PATH = "./resources/img/simulation/centrifugeOperation/"


class CentrifugeOperation(QWidget):
    finishedSignal = Signal(int)
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CentrifugeOperation()
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

        # centrifuge overview
        centrifugeItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "centrifuge.png"))
        centrifugeItem.setPos(90, 75)
        centrifugeItem.setScale(0.5)
        scene.addItem(centrifugeItem)

        # textItem general setting
        font = QFont()
        font.setPixelSize(20)
        defaultText = "(________)"

        nameList = [
            "上盖卡扣",  #
            "离心机上盖",
            "离心室",
            "控制器",
            "转子",
            "离心样品",
            "离心马达"
        ]

        posList = [
            (16, 71),  #
            (330, 79),
            (20, 115),
            (10, 170),
            (337, 181),
            (325, 307),
            (-15, 281)
        ]

        self.textItemList = []
        for i in range(len(nameList)):
            textItem = QGraphicsTextItem(defaultText)
            textItem.setFont(font)
            textItem.setPos(posList[i][0], posList[i][1])
            textItem.setDefaultTextColor(Qt.red)
            scene.addItem(textItem)
            textItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
            textItem.setData(Qt.UserRole, "(" + nameList[i] + ")")
            textItem.setFlag(QGraphicsItem.ItemIsMovable, True)
            self.textItemList.append(textItem)

        random.shuffle(nameList)
        for item in nameList:
            self.ui.nameList.addItem(item)

        self.ui.textBrowser.append("[提示信息]\n单击图中括号，再左侧点击按钮填写组件名称。\n")

    def setupScene2(self):
        items = self.ui.graphicsView.items()
        for i in range(len(items) - 1):
            items[i].hide()

        scene = self.ui.graphicsView.scene()

        self.ui.textBrowser.append("[提示信息]\n请完成正确的操作流程\n")

        # load all movie
        self.movieList = []
        for i in range(10):
            movie = QMovie(_RESOURCE_PATH + "step" + str(i) + ".gif")
            self.movieList.append(movie)

        # setup movieItem
        self.movieLabel = QLabel()
        self.movieLabel.setAttribute(Qt.WA_NoBackground)
        movieItem = scene.addWidget(self.movieLabel)
        movieItem.setScale(1)
        movieItem.setPos(13, 0)

        # before start
        self.movieLabel.setMovie(self.movieList[0])
        btnStart = QPushButton("开始使用离心机")
        startItem = scene.addWidget(btnStart)
        btnStart.setAttribute(Qt.WA_NoSystemBackground)
        startItem.setPos(125, 290)
        startItem.setScale(2)
        btnStart.clicked.connect(self.start)

        startTextItem = QGraphicsTextItem("你需要使用离心机将一管样品进行离心。")
        scene.addItem(startTextItem)
        startTextItem.setPos(10, 245)
        startTextItem.setScale(2)

        self.movieLabel.setMovie(self.movieList[0])
        self.movieLabel.movie().start()

        self.beforeStartItems = [startTextItem, startItem]

        # setup all buttoms
        self.buttomTextList = [
            "装样于离心专用试管,2/3左右",  # 0 step 0
            "装样于离心专用试管,装满",
            "装样于任意试管",
            "标记编号，再放入离心机中",  # 3 step 1
            "将样品直接放入离心机中",
            "另一试管装入等量样品或水",  # 5 step 2
            "关闭离心机上盖",  # 6 step 4
            "在对称位置放入另一试管",  # 7 step 3
            "在相邻位置放入另一试管",
            "在任意位置放入另一试管",
            "设定时间和转速，开始离心",  # 10 step 5
            "等待离心机停止",  # 11 step 6
            "中途打开离心机上盖",
            "打开离心机上盖",  # 13 step 7
            "取出试管，放置于试管架",  # 14 step 8
            "取出试管，随意放置"
        ]
        self.operationList = [
            "装样于离心专用试管,2/3左右",  # 0 step 0
            "标记编号，再放入离心机中",  # 3 step 1
            "另一试管装入等量样品或水",  # 5 step 2
            "在对称位置放入另一试管",  # 7 step 3
            "关闭离心机上盖",  # 6 step 4
            "设定时间和转速，开始离心",  # 10 step 5
            "等待离心机停止",  # 11 step 6
            "打开离心机上盖",  # 13 step 7
            "取出试管，放置于试管架",  # 14 step 8
        ]

        self.itemList = []
        for text in self.buttomTextList:
            # setup buttom
            buttom = QPushButton(text)
            buttom.setAttribute(Qt.WA_NoSystemBackground)
            # get it in to scene
            item = scene.addWidget(buttom)
            self.itemList.append(item)
            item.hide()

        self.stepButtonGroup = [
            (self.itemList[0], self.itemList[1], self.itemList[2]),
            (self.itemList[3], self.itemList[4]),
            (self.itemList[5], ),
            (self.itemList[7], self.itemList[8], self.itemList[9]),
            (self.itemList[6], self.itemList[10]),
            (self.itemList[10], ),
            (self.itemList[11], self.itemList[12]),
            (self.itemList[13], ),
            (self.itemList[14], self.itemList[15]),
        ]

    def start(self):
        for item in self.beforeStartItems:
            item.hide()
        self.setStep(0)

    @Slot()
    def setStep(self, index):
        self.currentStep = index
        self.movieLabel.setMovie(self.movieList[index])
        self.movieLabel.movie().start()

        for item in self.itemList:
            item.hide()

        if self.currentStep < len(self.stepButtonGroup):
            i = 0
            # convert tuple into list so i can use shuffle method.
            bottons = list(self.stepButtonGroup[self.currentStep])
            random.shuffle(bottons)
            for item in bottons:
                item.setPos(20, i * 50 + 320)
                item.show()
                item.setScale(1.8)
                i += 1

            self.setConnect()
        else:
            self.setFinished()

    def nextStep(self):
        self.setStep(self.currentStep + 1)
        if self.currentStep < len(self.stepButtonGroup):
            self.ui.operationList.addItem(self.operationList[self.currentStep -
                                                             1])

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

    @Slot()
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
            item.setPlainText("(" + answer + ")")

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
            self.ui.textBrowser.append("[错误信息]\n正确答案已在图中用绿色改正。共" +
                                       str(errorCount) + "处\n")

        self.score -= errorCount * 7

        self.ui.btnNext.setEnabled(True)
        self.ui.nameList.setEnabled(False)
        self.ui.btnCheck.setEnabled(False)

    @Slot()
    def on_btnNext_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.setupScene2()
