"""
@file       : Navigator.py
@description: Navigation window for both student and teacher.
@date       : 2021/03/22 18:05:24
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

from embellish.styles import _ICON
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow
from ui.generate.Ui_Student import Ui_Student
from ui.generate.Ui_Teacher import Ui_Teacher

from main.Setting import Setting
from main.Simulator import Simulator
from main.Test import Test
from main.TestManage import TestManage
from main.UserManage import UserManage

_IMG_PATH = "./resources/img/"
_NAVIGATOR_STYLESHEET = "./resources/qss/navigator.qss"


class Navigator(QMainWindow):
    userId = None  # record the user.
    app = None
    signOutSignal = Signal()

    def __init__(self, userId, app, isTeacher=False):
        super().__init__()
        self.userId = userId  # record the user.
        self.app = app  # record the application.
        if isTeacher:
            self.setupTeacher()
        else:
            self.setupStudent()
        # Set icon style
        with open(_NAVIGATOR_STYLESHEET) as stylesheet:
            self.setStyleSheet(stylesheet.read())

    def setupTeacher(self):
        self.ui = Ui_Teacher()
        self.ui.setupUi(self)

        # Add svg banner icon
        self.ui.svgBanner.load(_ICON)
        # set svg in shape of square.
        self.ui.svgBanner.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        # Add icon for buttons
        self.ui.btnUserManage.setIcon(QIcon(_IMG_PATH + "btnUserManage"))
        self.ui.btnScoreAnalyse.setIcon(QIcon(_IMG_PATH + "btnScoreAnalyse"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting"))
        self.ui.btnTestManage.setIcon(QIcon(_IMG_PATH + "btnTestManage"))

        # Connect buttons with slot
        self.ui.btnUserManage.clicked.connect(self.openUserManage)
        self.ui.btnTestManage.clicked.connect(self.openTestManage)
        self.ui.btnSetting.clicked.connect(self.openSetting)

    def setupStudent(self):
        self.ui = Ui_Student()
        self.ui.setupUi(self)

        # Add svg banner icon
        self.ui.svgBanner.load(_ICON)
        self.ui.svgBanner.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        # Add icon for buttons
        self.ui.btnLearn.setIcon(QIcon(_IMG_PATH + "btnLearn.svg"))
        self.ui.btnSafetyTest.setIcon(QIcon(_IMG_PATH + "btnSafetyTest.svg"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting.svg"))
        self.ui.btnSimulator.setIcon(QIcon(_IMG_PATH + "btnSimulator.svg"))

        # Connect buttons with slot
        self.ui.btnSetting.clicked.connect(self.openSetting)
        self.ui.btnSimulator.clicked.connect(self.openSimulator)

    @Slot()
    def openExpTest(self):
        self.Test = Test(self)
        self.Test.show()

    @Slot()
    def openSetting(self):
        self.setting = Setting(self.userId, self)
        self.setting.show()
        # signal for switch display mode.
        self.setting.switchDisplaySignal.connect(self.app.switchTheme)

        # signal for signing out.
        self.setting.signOutSignal.connect(self.signOutSignal.emit)

    @Slot()
    def openSimulator(self):
        self.simulator = Simulator(self)
        self.simulator.show()

    @Slot()
    def openUserManage(self):
        self.userManage = UserManage(self)
        self.userManage.show()

    @Slot()
    def openTestManage(self):
        self.testManage = TestManage(self)
        self.testManage.show()
