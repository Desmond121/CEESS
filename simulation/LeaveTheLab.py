"""
@file       : LeaveTheLab.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/04/25 14:40:44
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget


class LeaveTheLab(QWidget):
    finishedSignal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.ui = Ui_EnterTheLab()
        # self.ui.setupUi(self)
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.setupScene()