"""
@file       : Test.py
@description: For testing module.
@date       : 2021/03/22 18:23:26
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtWidgets import QMainWindow
from ui.generate.Ui_test import Ui_Test


class Test(QMainWindow):
    def __init__(self, testType=0, parent=None):
        """__init__

        Keyword Arguments:
            testType {int} -- (default: {0})
            {0} means safety test
            {1} means experiment test
        """
        super().__init__(parent)
        self.ui = Ui_Test()
        self.ui.setupUi(self)
