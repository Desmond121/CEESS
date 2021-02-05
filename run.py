"""
Author: Desmond
This is the running file for this programme.
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

from forms import LoginForm,StudentForm
from styles import StyleQApplication
from frameless import FramelessWindow

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = StyleQApplication(sys.argv)
    app.dark()
    Login =FramelessWindow (LoginForm())
    Login.show()

    sys.exit(app.exec_())
