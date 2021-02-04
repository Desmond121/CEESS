from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton

from sys import exit as sysExit


class Marker(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint);
        self.setAttribute(Qt.WA_NoSystemBackground, True);
        self.setAttribute(Qt.WA_TranslucentBackground, True);
        self.clicked = False
        self.resize(350, 250)

        self.btnClose = QPushButton('Close')
        self.btnClose.clicked.connect(self.CloseApp)

        HBox = QHBoxLayout()
        HBox.addWidget(self.btnClose)
        HBox.addStretch(1)

        VBox = QVBoxLayout()
        VBox.addLayout(HBox)
        VBox.addStretch(1)

        self.setLayout(VBox)

    def CloseApp(self):
        sysExit()

    def paintEvent(self, event):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(128, 128, 128, 128))

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = event.screenPos()
        self.clicked = True

        return QWidget.mouseMoveEvent(self, event)


if __name__ == "__main__":
    MainEventThred = QApplication([])

    MainApp = Marker()
    MainApp.show()

    MainEventThred.exec()

  # If anyone wants more extensive free help I run an online lab-like classroom-like
  # message server feel free and drop by you will not be able to post until I clear
  # you as a student as this prevents spammers so if interested here is the invite
  # https://discord.gg/3D8huKC