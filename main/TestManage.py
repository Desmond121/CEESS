"""
@file       : TestManage.py
@description: A window for test questions managing.
@date       : 2021/03/22 18:34:15
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow
from ui.generate.Ui_TestManage import Ui_TestManage


class TestManage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TestManage()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem("这是第一题，测试测试测试测试测试...")
        self.ui.listWidget.addItem("这是第二题测试测试测试测试测试测...")
        self.ui.textBrowser.setTextBackgroundColor(Qt.white)
