"""
@file       : windowsManager.py
@description: Control signals between different windows.
@date       : 2021/02/10 18:08:07
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtCore import Slot
from main.Navigator import Navigator
from main.Login import Login


class WindowsManager():
    def __init__(self, app):
        self.application = app
        app.light()

    def start(self):
        self.login = Login()
        self.login.show()
        self.navigator = None
        self.login.loginType.connect(self.createMainWindow)

    @Slot(bool)
    def createMainWindow(self, isTeacher):
        self.navigator = Navigator(isTeacher)
        self.navigator.show()
        self.login.close()
