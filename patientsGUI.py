import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import sqlite3

# GUI FILE
from dbwindow import Ui_MainWindow

# IMPORT FUNCTIONS
from dbFunction import *

class realMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loaddata()
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
## DATABASE
    def loaddata(self):
        connection = sqlite3.connect('patients')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM checkUp'

        tablerow=0
        results = cur.execute(sqlstr)
        self.checkUpTable.setRowCount(150)
        for row in results:
            if row[0] < 10:
                ticket = "CU00" + str(row[0])
            elif row[0] > 99:
                ticket = "CU" + str(row[0])
            else:
                ticket = "CU0" + str(row[0])
            self.checkUpTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(ticket))
            self.checkUpTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.checkUpTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.checkUpTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.checkUpTable.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.checkUpTable.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.checkUpTable.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            tablerow+=1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = realMainWindow()
    sys.exit(app.exec_())