"""
@file       : windowsManager.py
@description: Control signals between different windows.
@date       : 2021/02/10 18:08:07
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from main.Login import Login
from main.Navigator import Navigator
from PySide2.QtCore import Slot


class WindowsManager():
    def __init__(self, app):
        self.app = app

    def start(self):
        self.login = Login()
        self.login.show()
        self.navigator = None
        self.login.loginType.connect(self.createMainWindow)

    @Slot(tuple)
    def createMainWindow(self, result):
        isTeacher = result[0]
        userId = result[1]
        self.navigator = Navigator(userId, self.app, isTeacher)
        self.navigator.show()
        self.login.close()

        # signal for signing out.
        # todo
        def signOut():
            self.navigator.close()
            self.start()

        self.navigator.signOutSignal.connect(signOut)
