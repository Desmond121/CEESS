"""
@file       : windowManager.py
@description: Instantiation of all windows and signals between them.
@date       : 2021/02/10 18:08:07
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from utility.allWindows import Login, Student, Teacher
from embellish.frameless import FramelessWindow


class WinManager():
    def start(self):
        # login = FramelessWindow(Login(), False)
        # login.show()
        student = FramelessWindow(Student(), False)
        student.show()
