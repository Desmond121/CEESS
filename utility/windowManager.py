"""
@file       : windowManager.py
@description: Instantiation of all windows and signals between them.
@date       : 2021/02/10 18:08:07
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtCore import Slot
from utility.allWindows import Login, Navigator, UserManage


class WinManager():
    def __init__(self, app):
        self.application = app
        app.light()

    def start(self):
        # ! frameless
        # self.login = FramelessWindow(Login(), False)
        self.login = Login()
        self.login.show()
        self.navigator = None

        self.test()

        # ! for student window testing
        # self.mainWindow = FramelessWindow(Navigator(True))
        # self.mainWindow.show()
        # self.subWindow = FramelessWindow(Navigator(False))
        # self.subWindow.show()
        # self.testing = FramelessWindow(Test())
        # self.testing.show()

        # signal slot connection
        # ! frameless
        # self.login._w.loginType.connect(self.createMainWindow)
        self.login.loginType.connect(self.createMainWindow)

    def test(self):
        self.test = UserManage()
        self.test.show()

    @Slot(bool)
    def createMainWindow(self, isTeacher):
        # ! frameless
        # self.navigator = FramelessWindow(Navigator(isTeacher))
        self.navigator = Navigator(isTeacher)
        self.navigator.show()
        self.login.close()
