"""
@file       : Navigator.py
@description: Navigation window for both student and teacher.
@date       : 2021/03/22 18:05:24
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

from utility.DataManager import DataManager
from main.Grade import Grade
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QInputDialog, QMainWindow
from ui.generate.Ui_Student import Ui_Student
from ui.generate.Ui_Teacher import Ui_Teacher
from utility.StylesManager import _ICON

from main.Learn import Learn
from main.Setting import Setting
from main.Simulator import Simulator
from main.Test import Test
from main.TestManage import TestManage
from main.UserManage import UserManage

_IMG_PATH = "./resources/img/"
_NAVIGATOR_STYLESHEET = "./resources/qss/navigator.qss"


class Navigator(QMainWindow):
    userId = None  # record the user.
    isTeacher = None
    app = None
    signOutSignal = Signal()

    def __init__(self, userId, app, isTeacher=False):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.userId = userId  # record the user.
        self.isTeacher = isTeacher
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
        self.ui.btnUserManage.setIcon(QIcon(_IMG_PATH + "btnUserManage.svg"))
        self.ui.btnGrade.setIcon(QIcon(_IMG_PATH + "btnScoreAnalyse.svg"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting.svg"))
        self.ui.btnTestManage.setIcon(QIcon(_IMG_PATH + "btnTestManage.svg"))

        # Connect buttons with slot
        self.ui.btnUserManage.clicked.connect(self.openUserManage)
        self.ui.btnTestManage.clicked.connect(self.openTestManage)
        self.ui.btnSetting.clicked.connect(self.openSetting)
        self.ui.btnGrade.clicked.connect(self.openGradeAnalyse)

    def setupStudent(self):
        self.ui = Ui_Student()
        self.ui.setupUi(self)

        # Add svg banner icon
        self.ui.svgBanner.load(_ICON)
        self.ui.svgBanner.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        # Add icon for buttons
        self.ui.btnLearn.setIcon(QIcon(_IMG_PATH + "btnLearn.svg"))
        self.ui.btnTest.setIcon(QIcon(_IMG_PATH + "btnSafetyTest.svg"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting.svg"))
        self.ui.btnSimulator.setIcon(QIcon(_IMG_PATH + "btnSimulator.svg"))

        # Connect buttons with slot
        self.ui.btnSetting.clicked.connect(self.openSetting)
        self.ui.btnTest.clicked.connect(self.openTest)
        self.ui.btnSimulator.clicked.connect(self.openSimulator)
        self.ui.btnLearn.clicked.connect(self.openLearn)

    @Slot()
    def openTest(self):
        self.Test = Test(self.userId, self)
        self.Test.show()

    @Slot()
    def openSetting(self):
        self.setting = Setting(self.userId, self.isTeacher, self)
        self.setting.show()

        # signal for switch display mode.
        self.setting.switchDisplaySignal.connect(self.app.switchTheme)

        # signal for signing out.
        self.setting.signOutSignal.connect(self.signOutSignal.emit)

    @Slot()
    def openSimulator(self):
        db = DataManager()
        simulationDict = db.getTestTypeDict()
        db.closeConnect()

        simulationDict.pop(1)
        # reverse the key and value
        simulationDict = {
            value: key
            for (key, value) in simulationDict.items()
        }
        nameList = simulationDict.keys()

        result = QInputDialog.getItem(self, "CEESS-模拟", "请选择模拟操作：", nameList,
                                      0, False)
        isNotCancelled = result[1]
        if isNotCancelled:
            simulationName = result[0]
            self.simulator = Simulator(self.userId,
                                       simulationDict.get(simulationName),
                                       self)
            self.simulator.show()

    @Slot()
    def openUserManage(self):
        self.userManage = UserManage(self)
        self.userManage.show()

    @Slot()
    def openTestManage(self):
        self.testManage = TestManage(self)
        self.testManage.show()

    @Slot()
    def openLearn(self):
        self.learn = Learn(self)
        self.learn.show()

    @Slot()
    def openGradeAnalyse(self):
        self.grade = Grade(self)
        self.grade.show()
