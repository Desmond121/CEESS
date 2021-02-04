"""
Author: Desmond
This is the running file for this programme.
"""
import sys
import qtmodern.styles
import qtmodern.windows
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from forms import LoginForm

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = LoginForm()
    # mainWindow.show()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(mainWindow)
    mw.show()

    sys.exit(app.exec_())
