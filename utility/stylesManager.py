"""
@file       : styles.py
@description: Embedding skins and fonts into the QApplication class.
@date       : 2021/02/10 17:39:17
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtGui import QColor, QIcon, QPalette
from PySide2.QtWidgets import QApplication

_STYLESHEET = "./resources/qss/style.qss"
_ICON = "./resources/img/icon.svg"


class StyleQApplication(QApplication):
    isDark = False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyle("fusion")
        self.setWindowIcon(QIcon(_ICON))
        self.applyBaseTheme()
        self.dark()

    def applyBaseTheme(self):
        styleSheet = open(_STYLESHEET)
        self.setStyleSheet(styleSheet.read())

    def dark(self):
        darkPalette = QPalette()

        # basic colors
        darkPalette.setColor(QPalette.WindowText, QColor(180, 180, 180))
        darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.Light, QColor(180, 180, 180))
        darkPalette.setColor(QPalette.Midlight, QColor(90, 90, 90))
        darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
        darkPalette.setColor(QPalette.Text, QColor(180, 180, 180))
        darkPalette.setColor(QPalette.BrightText, QColor(180, 180, 180))
        darkPalette.setColor(QPalette.ButtonText, QColor(180, 180, 180))
        darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
        darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.HighlightedText, QColor(180, 180, 180))
        darkPalette.setColor(QPalette.Link, QColor(56, 252, 196))
        darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        darkPalette.setColor(QPalette.ToolTipBase, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.ToolTipText, QColor(180, 180, 180))
        darkPalette.setColor(QPalette.LinkVisited, QColor(80, 80, 80))

        # colors while disabled
        darkPalette.setColor(QPalette.Disabled, QPalette.WindowText,
                             QColor(127, 127, 127))
        darkPalette.setColor(QPalette.Disabled, QPalette.Text,
                             QColor(127, 127, 127))
        darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                             QColor(127, 127, 127))
        darkPalette.setColor(QPalette.Disabled, QPalette.Highlight,
                             QColor(80, 80, 80))
        darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                             QColor(127, 127, 127))

        self.setPalette(darkPalette)
        self.isDark = True

    def light(self):
        lightPalette = QPalette()

        # basic colors
        lightPalette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        lightPalette.setColor(QPalette.Button, QColor(240, 240, 240))
        lightPalette.setColor(QPalette.Light, QColor(180, 180, 180))
        lightPalette.setColor(QPalette.Midlight, QColor(200, 200, 200))
        lightPalette.setColor(QPalette.Dark, QColor(225, 225, 225))
        lightPalette.setColor(QPalette.Text, QColor(0, 0, 0))
        lightPalette.setColor(QPalette.BrightText, QColor(0, 0, 0))
        lightPalette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        lightPalette.setColor(QPalette.Base, QColor(237, 237, 237))
        lightPalette.setColor(QPalette.Window, QColor(240, 240, 240))
        lightPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        lightPalette.setColor(QPalette.Highlight, QColor(76, 163, 224))
        lightPalette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        lightPalette.setColor(QPalette.Link, QColor(0, 162, 232))
        lightPalette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
        lightPalette.setColor(QPalette.ToolTipBase, QColor(240, 240, 240))
        lightPalette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        lightPalette.setColor(QPalette.LinkVisited, QColor(222, 222, 222))

        # colors while disabled
        lightPalette.setColor(QPalette.Disabled, QPalette.WindowText,
                              QColor(115, 115, 115))
        lightPalette.setColor(QPalette.Disabled, QPalette.Text,
                              QColor(115, 115, 115))
        lightPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                              QColor(115, 115, 115))
        lightPalette.setColor(QPalette.Disabled, QPalette.Highlight,
                              QColor(190, 190, 190))
        lightPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                              QColor(115, 115, 115))

        self.setPalette(lightPalette)
        self.isDark = False

    def switchTheme(self):
        if self.isDark:
            self.light()
            self.applyBaseTheme()

        else:
            self.dark()
            self.applyBaseTheme()
