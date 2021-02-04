"""
Author: Desmond
This is the running file for this programme.
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from forms import LoginForm

from styles import StyleQApplication

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = StyleQApplication(sys.argv)
    app.dark()
    Login = LoginForm()
    Login.show()

    sys.exit(app.exec_())
