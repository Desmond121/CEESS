"""
@file       : Simulator.py
@description: For simulator module.
@date       : 2021/03/22 18:32:58
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from PySide2.QtCore import Qt, QUrl
from PySide2.QtWebEngineWidgets import QWebEngineSettings
from PySide2.QtWidgets import QMainWindow
from ui.generate.Ui_Simulator import Ui_Simulator


class Simulator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Simulator()
        self.ui.setupUi(self)
        self.ui.web.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.ui.web.load(QUrl("D:/Repo/CEESS/resources/pdf/example.pdf"))
        self.ui.web.show()
