from PySide6 import QtGui, QtCore
from PySide6.QtCore import QPoint
from PySide6.QtGui import Qt, QCursor


class ui_Functions():
    """ Functions for the main UI """
    # is the window maximized or not """
    isMaximized = False

    def __init__(self, window, ui):
        """
        :param window: is the calling QMainWindow
        :param ui: the connectet UI Component """
        self.window = window
        self.ui = ui
        self.setup()

    def setup(self):
        """ define Window and style it """
        # Frameless
        self.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.title_bar.mouseDoubleClickEvent = self.maxDoubleClick

        # title_bar
        self.ui.title_bar.mouseMoveEvent = self.moveWindow
        self.dragPos = self.window.pos()
        self.ui.title_bar.mousePressEvent = self.mousePressEvent

        # size grip
        self.ui.sizegrip.mouseMoveEvent = self.sizeWindow
        self.ui.sizegrip.mousePressEvent = self.mousePressEvent

        self.clearStatus()

    def setWindowTitle(self, title):
        """ sets the Titel in Window Bar """
        self.window.setWindowTitle(title)
        self.ui.window_title.setText(title)

    def setStatus(self, msg):
        """ sets a Message in the Statusbar """
        self.ui.status.setText(msg)

    def clearStatus(self):
        """ delete StatusBar Message """
        self.ui.status.setText("")

    def maximize_restore(self):
        if self.isMaximized is False:
            self.isMaximized = True
            self.window.showMaximized()
            self.setMaximizedIcon()
        else:
            self.isMaximized = False
            self.window.showNormal()
            self.setMaximizedIcon()

    def setMaximizedIcon(self):
        """ set the icon for restore/maximize """
        if self.isMaximized is True:
            self.ui.btn_max.setToolTip("Restore")
            self.ui.btn_max.setIcon(QtGui.QIcon(":/qss_icons/themes/darkgray/icons/window_normal.svg"))
        else:
            self.ui.btn_max.setToolTip("Maximize")
            self.ui.btn_max.setIcon(QtGui.QIcon(":/qss_icons/themes/darkgray/icons/window_undock.svg"))

    def maxDoubleClick(self, stateMouse):
        """ maximize or restore window """
        if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
            QtCore.QTimer.singleShot(250, lambda: self.maximize_restore())

    def getGlobalPosition(self, event):
        """ as (int) Point2D """
        p = event.globalPosition()
        return p.toPoint()

    def moveWindow(self, event):
        """ Window is dragged with the top bar """
        if event.buttons() == Qt.LeftButton:
            # maximized > restore to drag
            if self.isMaximized is True:
                self.maximize_restore()
                p = self.setMousetoTitleBar()
                self.dragPos = QCursor.pos()

            p = self.getGlobalPosition(event)
            self.window.move(self.window.pos() + p - self.dragPos)
            self.dragPos = p
            event.accept()

    def setMousetoTitleBar(self):
        """ set the Mouse Cursor to Middel of Title Bar """
        t = self.ui.title_bar
        x = self.window.x() + t.pos().x() + int(t.width() / 2)
        y = self.window.y() + t.pos().y() + int(t.height() / 2)
        p = QPoint(x, y)
        QCursor.setPos(p)
        return p

    def mousePressEvent(self, event):
        """ capture Position """
        self.dragPos = self.getGlobalPosition(event)
        event.accept()

    def sizeWindow(self, event):
        """ the size of the window ist changing with sizegrip button """
        if event.buttons() == Qt.LeftButton:
            if self.isMaximized is True:
                # reset maximized status
                self.isMaximized = False
                # revert Status!
                self.window.setWindowState(Qt.WindowNoState)
                self.setMaximizedIcon()
            p = self.getGlobalPosition(event)
            wpos = self.window.pos()
            # new size
            width = p.x() - wpos.x()
            height = p.y() - wpos.y()
            self.window.resize(width, height)
            event.accept()
