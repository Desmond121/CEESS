"""
@file       : allWindows.py
@description: This file create classes to encapsulate all the QT-uic generated
              files with "Ui_" prefix.
@date       : 2021/02/10 17:22:10
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from embellish.frameless import FramelessWindow
from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt, Signal, Slot
from PySide2.QtGui import QIcon
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget

from ui.Ui_Login import Ui_Login
from ui.Ui_Student import Ui_Student
from ui.Ui_Teacher import Ui_Teacher
from ui.Ui_test import Ui_Test
from ui.Ui_Setting import Ui_Setting
from ui.Ui_UserManage import Ui_UserManage
from ui.Ui_TestManage import Ui_TestManage

from utility.dataManager import DBManager

_IMG_PATH = "./resources/img/"
_NAVIGATOR_STYLESHEET = "./resources/qss/navigator.qss"


class Login(QMainWindow):
    # signal
    loginType = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

    @Slot()
    def on_loginButtom_clicked(self):
        password = self.ui.pswLineEdit.text()
        userId = self.ui.accLineEdit.text()

        data = DBManager("./data/db.sqlite3")
        if data.isPasswordCorrect(userId, password):
            isTeacher = bool(data.getTypeById(userId))
            self.loginType.emit(isTeacher)
        else:
            QMessageBox.information(self, "CEESS-提示", "用户名或密码错误!")


class Navigator(QMainWindow):
    def __init__(self, isTeacher=False):
        super().__init__()
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

        # Add icon for buttons
        self.ui.btnUserManage.setIcon(QIcon(_IMG_PATH + "btnUserManage"))
        self.ui.btnScoreAnalyse.setIcon(QIcon(_IMG_PATH + "btnScoreAnalyse"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting"))
        self.ui.btnTestManage.setIcon(QIcon(_IMG_PATH + "btnTestManage"))

        # Connect buttons with slot
        self.ui.btnUserManage.clicked.connect(self.openUserManage)
        self.ui.btnTestManage.clicked.connect(self.openTestManage)

    def setupStudent(self):
        self.ui = Ui_Student()
        self.ui.setupUi(self)

        # Add icon for buttons
        self.ui.btnDataProcess.setIcon(QIcon(_IMG_PATH + "btnDataProcess.svg"))
        self.ui.btnExpTest.setIcon(QIcon(_IMG_PATH + "btnExpTest.svg"))
        self.ui.btnPreparing.setIcon(QIcon(_IMG_PATH + "btnPrepare.svg"))
        self.ui.btnSafetyTest.setIcon(QIcon(_IMG_PATH + "btnSafetyTest.svg"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting.svg"))
        self.ui.btnSimulator.setIcon(QIcon(_IMG_PATH + "btnSimulator.svg"))

        # Connect buttons with slot
        self.ui.btnExpTest.clicked.connect(self.openExpTest)
        self.ui.btnSetting.clicked.connect(self.openSetting)

    @Slot()
    def openExpTest(self):
        # ! frameless
        # self.Test = FramelessWindow(Test(), True, self)
        self.Test = Test(self)
        self.Test.show()

    @Slot()
    def openSetting(self):
        # ! frameless
        # self.setting = FramelessWindow(Setting(), True, self)
        self.setting = Setting(self)
        self.setting.show()

    @Slot()
    def openUserManage(self):
        self.userManage = UserManage(self)
        self.userManage.show()

    @Slot()
    def openTestManage(self):
        self.testManage = TestManage(self)
        self.testManage.show()


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


class Setting(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Setting()
        self.ui.setupUi(self)
        self.ui.pushButton.setStyleSheet("border-color : red")


class UserManage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UserManage()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem("USER_1")
        self.ui.listWidget.addItem("ADMIN")


class TestManage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TestManage()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem("这是第一题，测试测试测试测试测试...")
        self.ui.listWidget.addItem("这是第二题测试测试测试测试测试测...")
        self.ui.textBrowser.setTextBackgroundColor(Qt.white)