"""
Author: Desmond
This is the running file for this programme.
"""
import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore

from forms import LoginForm, StudentForm
from styles import StyleQApplication
from frameless import FramelessWindow
from qtmodern import windows

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = StyleQApplication(sys.argv)
    app.light()
    Login = FramelessWindow(LoginForm())
    Login.show()

    sys.exit(app.exec_())
