"""
@file       : Learn.py
@description: this module provide pdf view for students
              to browse learning material
@date       : 2021/04/07 10:11:44
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

import os

from PySide2.QtCore import QFile, QUrl, Slot
from PySide2.QtGui import QIcon
from PySide2.QtWebEngineWidgets import QWebEngineSettings
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from ui.generate.Ui_Learn import Ui_Learn

_IMG_PATH = "./resources/img/"


class Learn(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Learn()
        self.ui.setupUi(self)
        self.ui.btnDownload.setIcon(QIcon(_IMG_PATH + "book.svg"))
        self.showMaximized()
        self.ui.webViewer.settings().setAttribute(
            QWebEngineSettings.PluginsEnabled, True)

        self.path = os.path.join(os.path.abspath("."), "resources", "learn")
        self.filenames = os.listdir(self.path)
        self.filenames.sort(key=lambda x: int(x.split(".")[0]))
        for filename in self.filenames:
            filenameNoSurfix = filename.removesuffix(".pdf")
            self.ui.learningList.addItem(filenameNoSurfix)

    @Slot(int)
    def on_learningList_currentRowChanged(self, row: int):
        file = os.path.join(self.path, self.filenames[row]).replace('\\', '/')
        self.ui.webViewer.load(QUrl(file))

    @Slot()
    def on_btnDownload_clicked(self):
        file = QFile("./resources/download/downloadLearningMaterial")
        if file.open(QFile.ReadOnly):
            filePath = QFileDialog.getSaveFileName(self, "CEESS-安全手册下载",
                                                   "学习内容.pdf",
                                                   "PDF Files (*.pdf)")
            if len(filePath[0]) != 0:
                file.copy(filePath[0])
        else:
            QMessageBox.warning(self, "CEESS-通知", "模板文件丢失，请重装本系统或联系管理员！")
