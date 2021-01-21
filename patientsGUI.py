import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIntValidator)
from PyQt5.QtWidgets import *
import sqlite3

# GUI FILE
from dbwindow import *

# IMPORT FUNCTIONS
from dbFunction import *

class realMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.frame_title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

        ## LOAD DATABASE
        self.onlyInt = QIntValidator()
        self.num = QtCore.QRegExp("[0-9]{11}")
        self.val = QtGui.QRegExpValidator(self.num)
        self.ui.ageEdit.setValidator(self.onlyInt)
        self.ui.ContactEdit.setValidator(self.val)
        self.ui.nameEdit.setMaxLength(50)
        self.ui.ageEdit.setMaxLength(3)
        self.ui.addressEdit.setMaxLength(100)
        dbWindow.loadCheckUp(self)
        dbWindow.loadVaccine(self)
        dbWindow.loadDental(self)

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = realMainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("EXITING SYSTEM")

