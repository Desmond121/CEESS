import sys

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QBrush, QColor, QPen, QPixmap
from PySide2.QtWidgets import (QApplication, QGraphicsScene, QGraphicsView,
                               QHBoxLayout, QLabel, QSplitter, QWidget)


class MyFrame(QGraphicsView):
    itemDoubleClicked = Signal(object)

    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent)
        scene = QGraphicsScene()
        self.setScene(scene)
        self.setFixedSize(1000, 1000)

        item = scene.addPixmap(QPixmap("resources/simulation/clothes.png"))
        item.setData(0, "clothes")

    def mouseDoubleClickEvent(self, event):
        item = self.itemAt(event.pos())
        if item is not None:
            self.itemDoubleClicked.emit(item)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        top = QLabel('Double Click the clothes')
        bottom = MyFrame()
        bottom.itemDoubleClicked.connect(self.printItem)
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(top)
        splitter.addWidget(bottom)
        hbox.addWidget(splitter)
        self.setLayout(hbox)
        self.setGeometry(0, 0, 500, 600)
        self.show()
    
    def printItem(self):
        print()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
