import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from main import Ui_MainWindow

# IMPORT FUNCTIONS
from functions import *

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

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ##TICKET INCREMENT
    def ticketIncrement1(self):
        global value1
        if value1 > 99:
            self.ui.label_ticketValue1.setText(("CU") + str(value1))
            self.ui.label_ticketValue.setText(("CU") + str(value1))
        elif value1 < 10:
            self.ui.label_ticketValue1.setText(("CU00") + str(value1))
            self.ui.label_ticketValue.setText(("CU00") + str(value1))
        else:
            self.ui.label_ticketValue1.setText(("CU0") + str(value1))
            self.ui.label_ticketValue.setText(("CU0") + str(value1))
        self.ui.label_roomNo.setText("Room 101")
        self.ui.frame_rightBody.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.688, "
                                              "y2:0.306818, stop:0 rgba(204, 196, 183, 255), stop:1 rgba(211, 227, "
                                              "255, 255));")
        value1 += 1
    def ticketIncrement2(self):
        global value2
        if value2 > 99:
            self.ui.label_ticketValue2.setText(("VC") + str(value2))
            self.ui.label_ticketValue.setText(("VC") + str(value2))
        elif value2 < 10:
            self.ui.label_ticketValue2.setText(("VC00") + str(value2))
            self.ui.label_ticketValue.setText(("VC00") + str(value2))
        else:
            self.ui.label_ticketValue2.setText(("VC0") + str(value2))
            self.ui.label_ticketValue.setText(("VC0") + str(value2))
        self.ui.label_roomNo.setText("Room 102")
        self.ui.frame_rightBody.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.994318, "
                                              "y2:0.023, stop:0 rgba(255, 194, 237, 255), stop:1 rgba(175, 255, 231, "
                                              "255));")
        value2 += 1
    def ticketIncrement3(self):
        global value3
        if value3 > 99:
            self.ui.label_ticketValue3.setText(("DT") + str(value3))
            self.ui.label_ticketValue.setText(("DT") + str(value3))
        elif value3 < 10:
            self.ui.label_ticketValue3.setText(("DT00") + str(value3))
            self.ui.label_ticketValue.setText(("DT00") + str(value3))
        else:
            self.ui.label_ticketValue3.setText(("DT0") + str(value3))
            self.ui.label_ticketValue.setText(("DT0") + str(value3))
        self.ui.label_roomNo.setText("Room 103")
        self.ui.frame_rightBody.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, "
                                              "stop:0 rgba(245, 184, 168, 255), stop:1 rgba(164, 178, 255, 255));")
        value3 += 1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = realMainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("System Exiting")