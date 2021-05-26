"""
@file       : LeaveTheLab.py
@description: This is one of the simulation tests in simulation module.
@date       : 2021/02/25 14:40:44
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from simulation.generate.Ui_LeaveTheLab import Ui_LeaveTheLab


class LeaveTheLab(QWidget):
    finishedSignal = Signal(int)
    score = 100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LeaveTheLab()
        self.ui.setupUi(self)