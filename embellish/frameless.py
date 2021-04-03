"""
@file       : frameless.py
@description: Make windows frameless. This file is modified from qtmodern
              library by gmarull.
@date       : 2021/02/10 17:27:53
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtCore import QMetaObject, QPoint, Qt, Signal, Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import (
    QApplication,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QLabel,
    QSizeGrip,
    QSizePolicy,
    QSpacerItem,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

_FL_STYLESHEET = "./resources/qss/frameless.qss"


class WindowDragger(QWidget):
    """Window dragger.

    Args:
        window (QWidget): Associated window.
        parent (QWidget, optional): Parent widget.
    """

    doubleClicked = Signal()

    def __init__(self, window, parent=None):
        QWidget.__init__(self, parent)

        self._window = window
        self._mousePressed = False

    def mousePressEvent(self, event):
        self._mousePressed = True
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()

    def mouseMoveEvent(self, event):
        if self._mousePressed:
            if self._window.windowState() == Qt.WindowMaximized:
                self._window.on_btnRestore_clicked()
                self._window.move(self._mousePos - QPoint(
                    0.5 * self.geometry().width(),
                    0.5 * self.geometry().height(),
                ))
                # refresh _windowPos
                self._windowPos = self._window.pos()
            self._window.move(self._windowPos +
                              (event.globalPos() - self._mousePos))

    def mouseReleaseEvent(self, event):
        self._mousePressed = False

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()


class FramelessWindow(QWidget):
    """Modern window.

    Args:
        w (QWidget): Main widget.
        parent (QWidget, optional): Parent widget.
    """
    def __init__(self, w, isResizable=True, parent=None):
        QWidget.__init__(self, parent)

        self._w = w
        self.setupUi()

        contentLayout = QHBoxLayout()
        contentLayout.setContentsMargins(10, 10, 10, 10)
        contentLayout.addWidget(w)

        self.windowContent.setLayout(contentLayout)

        self.setWindowTitle(w.windowTitle())
        self.setGeometry(w.geometry())

        # Determine whether to maximize
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, isResizable)

        # Determine whether to add resize grip buttom
        if isResizable:
            self.sizeGrip = QSizeGrip(self.windowFrame)
            self.vboxFrame.addWidget(self.sizeGrip, 0,
                                     Qt.AlignBottom | Qt.AlignRight)

        # Adding shadow for window
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setOffset(0, 0)
        shadowEffect.setBlurRadius(10)
        shadowEffect.setColor(QColor(0x141414))
        self.setGraphicsEffect(shadowEffect)

        # Adding attribute to clean up the parent window
        # when the child is closed
        self._w.setAttribute(Qt.WA_DeleteOnClose, True)
        self._w.destroyed.connect(self.__child_was_closed)

        # Align to the center of screen
        self.move(QApplication.desktop().rect().center() -
                  self.rect().center())

    def setupUi(self):
        # create title bar, content
        self.vboxWindow = QVBoxLayout(self)
        self.vboxWindow.setContentsMargins(5, 5, 5, 5)

        self.windowFrame = QWidget(self)
        self.windowFrame.setObjectName("windowFrame")

        self.vboxFrame = QVBoxLayout(self.windowFrame)
        self.vboxFrame.setContentsMargins(0, 0, 0, 0)

        self.titleBar = WindowDragger(self, self.windowFrame)
        self.titleBar.setObjectName("titleBar")
        self.titleBar.setSizePolicy(
            QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))

        self.hboxTitle = QHBoxLayout(self.titleBar)
        self.hboxTitle.setContentsMargins(0, 0, 0, 0)
        self.hboxTitle.setSpacing(0)

        self.spcTitle = QSpacerItem(58, 14, QSizePolicy.Fixed,
                                    QSizePolicy.Fixed)

        self.lblTitle = QLabel("Title")
        self.lblTitle.setObjectName("lblTitle")
        self.lblTitle.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        spButtons = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btnMinimize = QToolButton(self.titleBar)
        self.btnMinimize.setObjectName("btnMinimize")
        self.btnMinimize.setSizePolicy(spButtons)

        self.btnRestore = QToolButton(self.titleBar)
        self.btnRestore.setObjectName("btnRestore")
        self.btnRestore.setSizePolicy(spButtons)

        self.btnMaximize = QToolButton(self.titleBar)
        self.btnMaximize.setObjectName("btnMaximize")
        self.btnMaximize.setSizePolicy(spButtons)

        self.btnClose = QToolButton(self.titleBar)
        self.btnClose.setObjectName("btnClose")
        self.btnClose.setSizePolicy(spButtons)

        self.vboxFrame.addWidget(self.titleBar)

        self.windowContent = QWidget(self.windowFrame)
        self.vboxFrame.addWidget(self.windowContent)

        self.vboxWindow.addWidget(self.windowFrame)

        self.hboxTitle.addSpacerItem(self.spcTitle)
        self.hboxTitle.addWidget(self.lblTitle)
        self.hboxTitle.addWidget(self.btnMinimize)
        self.hboxTitle.addWidget(self.btnRestore)
        self.hboxTitle.addWidget(self.btnMaximize)
        self.hboxTitle.addWidget(self.btnClose)

        # set window flags
        self.setWindowFlags(Qt.Window
                            | Qt.FramelessWindowHint
                            | Qt.WindowSystemMenuHint
                            | Qt.WindowCloseButtonHint
                            | Qt.WindowMinimizeButtonHint)

        self.setAttribute(Qt.WA_TranslucentBackground)

        # set stylesheet
        with open(_FL_STYLESHEET) as stylesheet:
            self.setStyleSheet(stylesheet.read())

        # automatically connect slots
        QMetaObject.connectSlotsByName(self)

    def __child_was_closed(self):
        # The child was deleted, remove the reference
        # to it and close the parent window
        self._w = None
        self.close()

    def closeEvent(self, event):
        if not self._w:
            event.accept()
        else:
            self._w.close()
            event.setAccepted(self._w.isHidden())

    def setWindowTitle(self, title):
        """Set window title.

        Args:
            title (str): Title.
        """

        super().setWindowTitle(title)
        self.lblTitle.setText(title)

    def _setWindowButtonState(self, hint, state):
        btns = {
            Qt.WindowCloseButtonHint: self.btnClose,
            Qt.WindowMinimizeButtonHint: self.btnMinimize,
            Qt.WindowMaximizeButtonHint: self.btnMaximize,
        }
        button = btns.get(hint)

        maximized = bool(self.windowState() & Qt.WindowMaximized)

        if button == self.btnMaximize:  # special rules for max/restore
            self.btnRestore.setEnabled(state)
            self.btnMaximize.setEnabled(state)

            if maximized:
                self.btnRestore.setVisible(state)
                self.btnMaximize.setVisible(False)
            else:
                self.btnMaximize.setVisible(state)
                self.btnRestore.setVisible(False)
        else:
            button.setEnabled(state)

        allButtons = [
            self.btnClose,
            self.btnMinimize,
            self.btnMaximize,
            self.btnRestore,
        ]
        if True in [b.isEnabled() for b in allButtons]:
            for b in allButtons:
                b.setVisible(True)
            if maximized:
                self.btnMaximize.setVisible(False)
            else:
                self.btnRestore.setVisible(False)
            self.lblTitle.setContentsMargins(0, 0, 0, 0)
        else:
            for b in allButtons:
                b.setVisible(False)
            self.lblTitle.setContentsMargins(0, 2, 0, 0)

    def setWindowFlag(self, Qt_WindowType, on=True):
        buttonHints = [
            Qt.WindowCloseButtonHint,
            Qt.WindowMinimizeButtonHint,
            Qt.WindowMaximizeButtonHint,
        ]

        if Qt_WindowType in buttonHints:
            self._setWindowButtonState(Qt_WindowType, on)
        else:
            QWidget.setWindowFlag(self, Qt_WindowType, on)

    def setWindowFlags(self, Qt_WindowFlags):
        buttonHints = [
            Qt.WindowCloseButtonHint,
            Qt.WindowMinimizeButtonHint,
            Qt.WindowMaximizeButtonHint,
        ]
        for hint in buttonHints:
            self._setWindowButtonState(hint, bool(Qt_WindowFlags & hint))

        QWidget.setWindowFlags(self, Qt_WindowFlags)

    @Slot()
    def on_btnMinimize_clicked(self):
        self.setWindowState(Qt.WindowMinimized)

    @Slot()
    def on_btnRestore_clicked(self):
        if self.btnMaximize.isEnabled() or self.btnRestore.isEnabled():
            self.btnRestore.setVisible(False)
            self.btnRestore.setEnabled(False)
            self.btnMaximize.setVisible(True)
            self.btnMaximize.setEnabled(True)

        self.vboxWindow.setContentsMargins(10, 10, 10, 10)
        self.setWindowState(Qt.WindowNoState)

    @Slot()
    def on_btnMaximize_clicked(self):
        if self.btnMaximize.isEnabled() or self.btnRestore.isEnabled():
            self.btnRestore.setVisible(True)
            self.btnRestore.setEnabled(True)
            self.btnMaximize.setVisible(False)
            self.btnMaximize.setEnabled(False)

        self.vboxWindow.setContentsMargins(0, 0, 0, 0)
        self.setWindowState(Qt.WindowMaximized)

    @Slot()
    def on_btnClose_clicked(self):
        self.close()

    @Slot()
    def on_titleBar_doubleClicked(self):

        if not bool(self.windowState() & Qt.WindowMaximized):
            if self.btnMaximize.isEnabled():
                self.on_btnMaximize_clicked()
        else:
            self.on_btnRestore_clicked()
