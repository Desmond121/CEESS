"""
Author: Desmond
This is the running file for this programme.
"""
import sys
from PySide2.QtWidgets import QApplication
from forms import LoginForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LoginForm()
    mainWindow.show()

    sys.exit(app.exec_())
