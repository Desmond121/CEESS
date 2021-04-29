"""
@file       : AutoclaveSafety.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/02/29 10:01:54
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QBrush, QColor, QPixmap
from PySide2.QtWidgets import (QGraphicsEllipseItem, QGraphicsItem,
                               QGraphicsPixmapItem, QGraphicsRectItem,
                               QGraphicsScene, QGraphicsTextItem,
                               QListWidgetItem, QWidget)

from simulation.generate.Ui_AutoclaveSafety import Ui_AutoclaveSafety

_RESOURCE_PATH = "./resources/img/simulation/autoclaveSafety/"


class AutoclaveSafety(QWidget):
    finishedSignal = Signal(int)
    simulationIndex = 5
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
