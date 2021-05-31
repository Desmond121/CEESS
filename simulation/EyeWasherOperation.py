"""
@file       : EyeWasherOperation.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/05/10 18:39:46
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
import random
from typing import Sized

from PySide2.QtCore import QObject, Qt, Signal, Slot
from PySide2.QtGui import QBrush, QColor, QFont, QMovie, QPixmap
from PySide2.QtWidgets import (QGraphicsItem, QGraphicsPixmapItem,
                               QGraphicsScene, QGraphicsTextItem, QLabel,
                               QMessageBox, QPushButton, QWidget)

from simulation.generate.Ui_EyeWasherOperation import Ui_EyeWasherOperation

_RESOURCE_PATH = "./resources/img/simulation/eyeWasherOperation/"


class EyeWasherOperation(QWidget):
    finishedSignal = Signal(int)
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EyeWasherOperation()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setupScene()

    def setupScene(self):
        self.ui.textBrowser.append("[提示信息]\n单击图中横线，再左侧点击按钮填写答案。\n")
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

        # infoBackground
        infoBackgroundItem = QGraphicsPixmapItem(
            QPixmap(_RESOURCE_PATH + "background.png"))
        infoBackgroundItem.setPos(-32, 55)
        infoBackgroundItem.setScale(1)
        scene.addItem(infoBackgroundItem)
        # infoBackgroundItem.setFlags(QGraphicsItem.ItemIsMovable
        #                             | QGraphicsItem.ItemIsSelectable)

        # textItems
        textList = [
            ("不要犹豫，尽快使用", 0),
            ("尽快联系急救", 1),
            ("不要使用洗眼器以外的水龙头冲洗眼睛", 2),
            ("注意地滑，防止摔伤", 3),
            ("可以使用洗眼器以外的水龙头冲洗眼镜", -1),
            ("溅入眼后可以等待片刻再使用洗眼器", -1),
            ("不可重复使用", -1),
            ("如果需要，可以重复冲洗", 4),
        ]
        self.textItemList = []
        for i in range(5):
            textItem = QGraphicsTextItem("___________________________")
            self.textItemList.append(textItem)
            scene.addItem(textItem)
            font = textItem.font()
            font.setBold(True)
            textItem.setFont(font)
            textItem.setScale(1.5)
            textItem.setPos(17, i * 40 + 130)
            textItem.setDefaultTextColor(Qt.yellow)
            textItem.setFlag(QGraphicsItem.ItemIsSelectable, True)

        random.shuffle(textList)
        for i in range(len(textList)):
            self.ui.textList.addItem(textList[i][0])
            self.ui.textList.item(i).setData(Qt.UserRole, textList[i][1])

    def setupScene2(self):
        items = self.ui.graphicsView.items()
        for i in range(len(items) - 1):
            items[i].hide()

        scene = self.ui.graphicsView.scene()

        self.ui.textBrowser.append("[提示信息]\n请完成正确的操作流程\n")

        # load all movie
        self.movieList = []
        for i in range(7):
            movie = QMovie(_RESOURCE_PATH + "step" + str(i) + ".gif")
            self.movieList.append(movie)

        self.movieLabel = QLabel()
        self.movieLabel.setAttribute(Qt.WA_NoBackground)
        movieItem = scene.addWidget(self.movieLabel)
        movieItem.setScale(1)
        movieItem.setPos(13, 0)

        # before start
        self.movieLabel.setMovie(self.movieList[0])
        btnStart = QPushButton("开始操作")
        btnStart.setAttribute(Qt.WA_NoSystemBackground)
        startItem = scene.addWidget(btnStart)
        startItem.setPos(145, 290)
        startItem.setScale(2)
        btnStart.clicked.connect(self.start)

        startTextItem = QGraphicsTextItem("化学品泄露并溅入眼中")
        scene.addItem(startTextItem)
        startTextItem.setPos(100, 245)
        startTextItem.setScale(2)

        self.movieLabel.setMovie(self.movieList[0])
        self.movieLabel.movie().start()

        self.beforeStartItems = [startTextItem, startItem]

        # setup all buttoms
        self.buttomTextList = [
            "迅速前往洗眼器处",  # 0 step 0
            "用衣物擦拭眼睛再前往洗眼器处",
            "开启洗眼器",  # 2 step 1
            "用手撑开眼皮俯身冲洗",  # 3 step 2
            "用手接水清洗眼睛",
            "冲洗时保持眼珠旋转",  # 5 step 3
            "冲洗时保持眼珠不动",
            "冲洗时眼珠向上翻",
            "冲洗至少15分钟",  # 8 step 4
            "冲洗至少1分钟",
            "冲洗至少5分钟",
            "可冲洗多次，完成后关闭",  # 11 step 5
            "只能冲洗一次，完成后关闭",
        ]
        self.operationList = [
            "迅速前往洗眼器处",  # 0 step 0
            "开启洗眼器",  # 2 step 1
            "用手撑开眼皮俯身冲洗",  # 3 step 2
            "冲洗时保持眼珠旋转",  # 5 step 3
            "冲洗至少15分钟",  # 8 step 4
            "可冲洗多次，完成后关闭",  # 11 step 5
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
            (self.itemList[0], self.itemList[1]),
            (self.itemList[2], ),
            (self.itemList[3], self.itemList[4]),
            (self.itemList[5], self.itemList[6], self.itemList[7]),
            (self.itemList[8], self.itemList[9], self.itemList[10]),
            (self.itemList[11], self.itemList[12]),
        ]

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
    def wrongAnswer(self):
        if self.ui.lcdNumber.intValue() == 1:
            self.ui.lcdNumber.display(self.ui.lcdNumber.intValue() - 1)
            QMessageBox.warning(self, "CEESS-警告", "错误过程！无剩余次数！")
            self.setFinished()
        else:
            QMessageBox.warning(self, "CEESS-警告", "错误过程")
            self.ui.lcdNumber.display(self.ui.lcdNumber.intValue() - 1)

    @Slot()
    def start(self):
        for item in self.beforeStartItems:
            item.hide()
        self.setStep(0)

    @Slot()
    def on_textList_itemClicked(self):
        items = self.ui.graphicsView.scene().selectedItems()
        if len(items) != 0:
            item = items[0]
            answer = self.ui.textList.selectedItems()[0].text()
            data = self.ui.textList.selectedItems()[0].data(Qt.UserRole)
            item.setPlainText(answer)
            item.setData(Qt.UserRole, data)

    @Slot()
    def on_btnCheck_clicked(self):
        errorCount = 0
        errorList = list()
        answerSet = set()
        correctSet = {0, 1, 2, 3, 4}
        for item in self.textItemList:
            data = item.data(Qt.UserRole)
            if data is None:  # empty
                errorCount += 1
                errorList.append(item)
            elif data not in correctSet:  # wrong
                errorCount += 1
                errorList.append(item)
            elif data in answerSet:  # duplicate
                errorCount += 1
                errorList.append(item)
            else:  # correct
                answerSet.add(data)

        for item in errorList:
            item.setDefaultTextColor(Qt.red)

        if errorCount == 0:
            self.ui.textBrowser.append("[完成信息]\n全部正确。\n")
        else:
            self.ui.textBrowser.append("[错误信息]\n错误答案已标红。共" + str(errorCount) +
                                       "处\n")

        self.score -= errorCount * 10

        self.ui.btnNext.setEnabled(True)
        self.ui.textList.setEnabled(False)
        self.ui.btnCheck.setEnabled(False)

    @Slot()
    def on_btnNext_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.setupScene2()
