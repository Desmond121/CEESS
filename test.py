from simulation.GasCylindersOperation import GasCylindersOperation
from simulation.EnterTheLab import EnterTheLab
import sys

from PySide2 import QtCore
from PySide2.QtGui import QFontDatabase
from PySide2.QtWidgets import QApplication, QMainWindow

from main.Navigator import Navigator
from utility.stylesManager import StyleQApplication

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


def runSimulation():
    # global pre-setting
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = StyleQApplication(sys.argv)
    app.dark()

    mainWin = QMainWindow()
    widget = GasCylindersOperation()
    mainWin.setCentralWidget(widget)
    mainWin.setFixedSize(1000, 600)
    mainWin.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    runSimulation()
