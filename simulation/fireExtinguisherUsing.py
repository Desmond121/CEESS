"""
@file       : fireExtinguisherUsing.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/05/25 22:01:59
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

import random

from PySide2.QtCore import QObject, Qt, Signal, Slot
from PySide2.QtGui import QBrush, QColor, QMovie, QPixmap
from PySide2.QtWidgets import (QGraphicsPixmapItem, QGraphicsScene,
                               QGraphicsTextItem, QLabel, QMessageBox,
                               QPushButton, QWidget)

from simulation.generate.Ui_fireExtinguisherUsing import \
    Ui_fireExtinguisherUsing

_RESOURCE_PATH = "./resources/img/simulation/fireExtinguisherUsing/"


class fireExtingusherUsing(QWidget):
    finishedSignal = Signal(int)
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fireExtinguisherUsing()
        self.ui.setupUi(self)
        self.setupScene()

    def setupScene(self):
        # setup background
        self.ui.graphicsView.setBackgroundBrush(
            QBrush(QColor(0x566280), Qt.SolidPattern))

        # setup scene
        scene = QGraphicsScene(0, 0, 450, 500)
        self.ui.graphicsView.setScene(scene)

        # origin items
        # fire gif
        fireMovie = QMovie(_RESOURCE_PATH + "fire.gif")
        fireMovieLabel = QLabel()
        fireMovieLabel.setAttribute(Qt.WA_NoSystemBackground)
        fireMovieLabel.setMovie(fireMovie)
        fireMovieItem = scene.addWidget(fireMovieLabel)
        fireMovieItem.setScale(1)
        fireMovieItem.setPos(70, 0)
        fireMovie.start()

        # start text
        startTextItem = QGraphicsTextItem("实验中意外起火，请开始灭火！")
        scene.addItem(startTextItem)
        startTextItem.setPos(50, 230)
        startTextItem.setScale(2)
        # startTextItem.setFlags(QGraphicsItem.ItemIsSelectable
        #                        | QGraphicsItem.ItemIsMovable)

        # start btn
        btnStart = QPushButton()
        btnStart.setText("前往灭火器处")
        btnStart.setAttribute(Qt.WA_NoSystemBackground)
        startItem = scene.addWidget(btnStart)
        startItem.setScale(2)
        startItem.setPos(135, 270)
        btnStart.clicked.connect(self.start)

        self.startItemGroup = [startItem, startTextItem, fireMovieItem]

        # pic item
        self.picItem = QGraphicsPixmapItem()
        scene.addItem(self.picItem)
        self.picItem.setPos(75, 0)
        self.picItem.setScale(0.5)

        # 1
        btnTakeItCarefully = QPushButton()
        btnTakeItCarefully.setText("左手握着压把，右手托着瓶身，轻取灭火器")
        btnTakeItCarefully.setAttribute(Qt.WA_NoSystemBackground)
        takeItCarefullyItem = scene.addWidget(btnTakeItCarefully)

        # 2
        btnTakeItCarelessly = QPushButton()
        btnTakeItCarelessly.setText("事态紧急，用力拔下灭火器")
        btnTakeItCarelessly.setAttribute(Qt.WA_NoSystemBackground)
        takeItCarelesslyItem = scene.addWidget(btnTakeItCarelessly)

        # 3
        btnPickItToFire = QPushButton()
        btnPickItToFire.setText("右手提着灭火器前往现场")
        btnPickItToFire.setAttribute(Qt.WA_NoSystemBackground)
        pickItToFireItem = scene.addWidget(btnPickItToFire)

        # 4
        btnMistakenlytakeIt = QPushButton()
        btnMistakenlytakeIt.setText("横抱着灭火器前往现场")
        btnMistakenlytakeIt.setAttribute(Qt.WA_NoSystemBackground)
        mistakenlyPickItItem = scene.addWidget(btnMistakenlytakeIt)

        # 5
        btnRemoveSeal = QPushButton()
        btnRemoveSeal.setText("除去铅封")
        btnRemoveSeal.setAttribute(Qt.WA_NoSystemBackground)
        removeSealItem = scene.addWidget(btnRemoveSeal)

        # 6
        btnRemoveBolt = QPushButton()
        btnRemoveBolt.setText("拔掉插销")
        btnRemoveBolt.setAttribute(Qt.WA_NoSystemBackground)
        removeBoltItem = scene.addWidget(btnRemoveBolt)

        # 7
        btnForceOpen = QPushButton()
        btnForceOpen.setText("用力按压压把切断插销")
        btnForceOpen.setAttribute(Qt.WA_NoSystemBackground)
        forceOpenItem = scene.addWidget(btnForceOpen)

        # 8
        btnCorrectPosture = QPushButton()
        btnCorrectPosture.setText("左手握着喷口，右手提着压把")
        btnCorrectPosture.setAttribute(Qt.WA_NoSystemBackground)
        correctPostureItem = scene.addWidget(btnCorrectPosture)

        # 9
        btnWrongPosture = QPushButton()
        btnWrongPosture.setText("左手托住瓶身，右手托着压把")
        btnWrongPosture.setAttribute(Qt.WA_NoSystemBackground)
        wrongPostureItem = scene.addWidget(btnWrongPosture)

        # 10
        btnPutOutFire = QPushButton()
        btnPutOutFire.setText("2米外，喷口对准火源摇摆，按压压把")
        btnPutOutFire.setAttribute(Qt.WA_NoSystemBackground)
        putOutFireItem = scene.addWidget(btnPutOutFire)

        btnTooFar = QPushButton()
        btnTooFar.setText("10米外，喷口对准火源摇摆，按压压把")
        btnTooFar.setAttribute(Qt.WA_NoSystemBackground)
        tooFarItem = scene.addWidget(btnTooFar)

        btnNotHold = QPushButton()
        btnNotHold.setText("距离2米，右手按压压把喷出")
        btnNotHold.setAttribute(Qt.WA_NoSystemBackground)
        notHoldItem = scene.addWidget(btnNotHold)

        btnSuccess = QPushButton()
        btnSuccess.setText("完成灭火")
        btnSuccess.setAttribute(Qt.WA_NoSystemBackground)
        successItem = scene.addWidget(btnSuccess)

        # first one in tuple is correct answer
        self.stepButtonGroup = [
            (takeItCarefullyItem, takeItCarelesslyItem),  # step 0
            (pickItToFireItem, mistakenlyPickItItem),
            (removeSealItem, removeBoltItem, forceOpenItem),
            (removeBoltItem, forceOpenItem),
            (correctPostureItem, wrongPostureItem),
            (putOutFireItem, tooFarItem, notHoldItem),  # 5
            (successItem, )
        ]

        self.allButtom = [
            takeItCarefullyItem, takeItCarelesslyItem, pickItToFireItem,
            mistakenlyPickItItem, removeBoltItem, removeSealItem,
            forceOpenItem, correctPostureItem, wrongPostureItem,
            putOutFireItem, tooFarItem, notHoldItem, successItem
        ]

        for item in self.allButtom:
            item.hide()

        self.infoList = [
            "尽快前往灭火器处", "左手握着压把，右手托着瓶身，轻取下灭火器", "右手提着灭火器前往现场", "将铅封去除", "拔去插销",
            "左手握着喷管，右手提着压把", "2米外，喷口对准火源摇摆，按压压把,喷射到所有起火区域"
        ]

    def setStep(self, step):
        self.currentStep = step
        self.picItem.setPixmap(
            QPixmap(_RESOURCE_PATH + "step" + str(step) + ".png"))

        for item in self.allButtom:
            item.hide()
        # setup button of each step.
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
        if self.currentStep < len(self.infoList):
            self.ui.listWidget.addItem(self.infoList[self.currentStep])

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
                                   str(count * 20) + "分\n")
        self.score = count * 20
        self.ui.textBrowser.append("[成绩信息]\n最终得分：" + str(self.score))
        self.ui.textBrowser.append("\n练习已完成。退出当前窗口以上传成绩。")
        self.finishedSignal.emit(self.score)

    @Slot()
    def on_btnNext_clicked(self):
        items = self.ui.graphicsView.items()
        for item in items:
            if item.isSelected():
                print(item.pos())

    @Slot()
    def start(self):
        for item in self.startItemGroup:
            item.hide()
        self.setStep(0)
