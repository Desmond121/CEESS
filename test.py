from os import truncate
from main.Navigator import Navigator
import sys

from PySide2 import QtCore
from PySide2.QtGui import QFontDatabase

from embellish.styles import StyleQApplication
from utility.WindowsManager import WindowsManager

_FONTPATH = "./resources/font/SourceHanSansCN-Regular.ttf"


def runStudent():
    # global pre-setting
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # run qt application and setup color theme
    app = StyleQApplication(sys.argv)
    app.light()
    # load font family
    QFontDatabase.addApplicationFont(_FONTPATH)
    # run this app
    student = Navigator("abc", app, False)
    student.show()
    sys.exit(app.exec_())


def runTeacher():
    # global pre-setting
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # run qt application and setup color theme
    app = StyleQApplication(sys.argv)
    app.light()
    # load font family
    QFontDatabase.addApplicationFont(_FONTPATH)
    # run this app
    teacher = Navigator("abc", app, True)
    teacher.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    runStudent()
