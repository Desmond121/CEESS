"""
@file       : Setting.py
@description: For setting windows.
@date       : 2021/03/22 18:03:32
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from PySide2.QtWidgets import QMainWindow
from ui.generate.Ui_Setting import Ui_Setting


class Setting(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Setting()
        self.ui.setupUi(self)
        self.ui.pushButton.setStyleSheet("border-color : red")
