"""
@file       : SignRecognizing.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/04/25 15:30:44
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
import random

from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import QBrush, QColor, QFont, QPixmap
from PySide2.QtWidgets import (QGraphicsItem, QGraphicsPixmapItem,
                               QGraphicsScene, QGraphicsTextItem, QWidget)

from simulation.generate.Ui_SignRecognizing import Ui_SignRecognizing

_RESOURCE_PATH = "./resources/img/simulation/SignRecognizing/"


class SignRecognizing(QWidget):
    finishedSignal = Signal(int)
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignRecognizing()
        self.ui.setupUi(self)
        self.ui.textBrowser.append("[提示信息]\n单击图中括号，再左侧点击按钮填写组件名称。\n")
        self.currentScene = 0
        self.setupScene(self.currentScene)
        self.totalErr = 0

    def setupScene(self, index):
        setupMethods = [self.setupScene1, self.setupScene2, self.setupScene3]
        if index < len(setupMethods):
            setupMethods[index]()
        else:
            self.setFinished()

    def setupScene1(self):
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

        # group 1
        imgInfolist = [
            "必须穿防护服",  #
            "必须穿防护鞋",
            "必须穿防护手套",
            "必须穿防护面具",
            "必须穿防护帽",
            "必须穿防护眼镜"
        ]
        self.imgItemList = []
        self.textItemList = []

        font = QFont()
        font.setPixelSize(20)
        defaultText = "(_________)"

        for y in range(2):
            for x in range(3):
                # set img item
                imgItem = QGraphicsPixmapItem(
                    QPixmap(_RESOURCE_PATH + "img1" + str(y * 3 + x + 1) +
                            ".jpg"))
                self.imgItemList.append(imgItem)
                imgItem.setPos(x * 170, y * 170)
                imgItem.setScale(1)
                scene.addItem(imgItem)

                # set text item
                textItem = QGraphicsTextItem()
                textItem.setFont(font)
                textItem.setPos(x * 160 - 15, y * 170 + 120)
                textItem.setPlainText(defaultText)
                textItem.setDefaultTextColor(Qt.red)
                scene.addItem(textItem)
                textItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
                textItem.setData(Qt.UserRole,
                                 "(" + imgInfolist[y * 3 + x] + ")")
                self.textItemList.append(textItem)

        random.shuffle(imgInfolist)
        for item in imgInfolist:
            self.ui.listWidget.addItem(item)

    def setupScene2(self):
        for item in self.imgItemList:
            item.hide()
        for item in self.textItemList:
            item.hide()

        scene = self.ui.graphicsView.scene()
        self.ui.listWidget.clear()

        # group 2
        imgInfolist = [
            "当心爆炸",  #
            "当心触电",
            "当心感染",
            "当心腐蚀",
            "当心中毒",
            "当心烫伤"
        ]
        self.imgItemList = []
        self.textItemList = []

        font = QFont()
        font.setPixelSize(20)
        defaultText = "(_________)"

        for y in range(2):
            for x in range(3):
                # set img item
                imgItem = QGraphicsPixmapItem(
                    QPixmap(_RESOURCE_PATH + "img2" + str(y * 3 + x + 1) +
                            ".jpg"))
                self.imgItemList.append(imgItem)
                imgItem.setPos(x * 170, y * 170)
                imgItem.setScale(1)
                scene.addItem(imgItem)

                # set text item
                textItem = QGraphicsTextItem()
                textItem.setFont(font)
                textItem.setPos(x * 170, y * 170 + 120)
                textItem.setPlainText(defaultText)
                textItem.setDefaultTextColor(Qt.red)
                scene.addItem(textItem)
                textItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
                textItem.setData(Qt.UserRole,
                                 "(" + imgInfolist[y * 3 + x] + ")")
                self.textItemList.append(textItem)

        random.shuffle(imgInfolist)
        for item in imgInfolist:
            self.ui.listWidget.addItem(item)

    def setupScene3(self):
        for item in self.imgItemList:
            item.hide()
        for item in self.textItemList:
            item.hide()

        scene = self.ui.graphicsView.scene()
        self.ui.listWidget.clear()

        # group 3
        imgInfolist = [
            "禁止穿化纤衣物",  #
            "禁止穿钉鞋",
            "禁止吸烟",
            "禁止饮用",
            "禁止用水灭火",
            "禁止触摸"
        ]
        self.imgItemList = []
        self.textItemList = []

        font = QFont()
        font.setPixelSize(20)
        defaultText = "(_________)"

        for y in range(2):
            for x in range(3):
                # set img item
                imgItem = QGraphicsPixmapItem(
                    QPixmap(_RESOURCE_PATH + "img3" + str(y * 3 + x + 1) +
                            ".jpg"))
                self.imgItemList.append(imgItem)
                imgItem.setPos(x * 170, y * 170)
                imgItem.setScale(0.35)
                scene.addItem(imgItem)

                # set text item
                textItem = QGraphicsTextItem()
                textItem.setFont(font)
                textItem.setPos(x * 160, y * 170 + 120)
                textItem.setPlainText(defaultText)
                textItem.setDefaultTextColor(Qt.red)
                scene.addItem(textItem)
                textItem.setFlag(QGraphicsItem.ItemIsSelectable, True)
                textItem.setData(Qt.UserRole,
                                 "(" + imgInfolist[y * 3 + x] + ")")
                self.textItemList.append(textItem)

        random.shuffle(imgInfolist)
        for item in imgInfolist:
            self.ui.listWidget.addItem(item)

    @Slot()
    def on_listWidget_itemClicked(self):
        items = self.ui.graphicsView.scene().selectedItems()
        if len(items) != 0:
            item = items[0]
            answer = self.ui.listWidget.selectedItems()[0].text()
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
                                       str(errorCount) + "处。\n")

        self.totalErr += errorCount

        self.ui.btnNext.setEnabled(True)
        self.ui.listWidget.setEnabled(False)
        self.ui.btnCheck.setEnabled(False)

    @Slot()
    def on_btnNext_clicked(self):
        self.ui.btnCheck.setEnabled(True)
        self.ui.listWidget.setEnabled(True)
        self.ui.btnNext.setEnabled(False)

        self.currentScene += 1
        self.setupScene(self.currentScene)

    def setFinished(self):
        if self.totalErr != 18:
            self.score = self.score - 5 * self.totalErr
        else:
            self.score = 0

        self.ui.graphicsView.setEnabled(False)
        self.ui.textBrowser.append("[完成信息]\n错误: " + str(self.totalErr) +
                                   "个\n得分: " + str(self.score) + "分\n")

        self.ui.textBrowser.append("[成绩信息]\n最终得分：" + str(self.score))
        self.ui.textBrowser.append("\n练习已完成。退出当前窗口以上传成绩。")
        self.finishedSignal.emit(self.score)
