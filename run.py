"""
@file       : run.py
@description: The entrance of this program.
@date       : 2021/02/10 17:20:20
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

import sys

from PySide2 import QtCore
from PySide2.QtGui import QFontDatabase

from utility.styles import StyleQApplication
from utility.WindowsManager import WindowsManager

_FONTPATH = "./resources/font/SourceHanSansCN-Regular.ttf"

if __name__ == "__main__":
    # settings
    # global pre-setting
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # run qt application and setup color theme
    app = StyleQApplication(sys.argv)
    # load font family
    QFontDatabase.addApplicationFont(_FONTPATH)

    # start
    ceess = WindowsManager(app)
    ceess.start()

    sys.exit(app.exec_())
