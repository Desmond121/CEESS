import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QFileInfo, QUrl

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.setUrl(QUrl(QFileInfo("./web/index.html").absoluteFilePath()))
    web.show()
    sys.exit(app.exec_())