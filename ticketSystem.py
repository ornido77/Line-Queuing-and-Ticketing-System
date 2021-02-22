import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIntValidator)
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWidgets import *
import sqlite3

# GUI FILE
from ticket import *

# IMPORT FUNCTIONS
from ticketFunction import *
checkup = 1
vaccine = 1
dental = 1
priority = 1

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

        self.ui.checkUpBtn.clicked.connect(self.printCuTicket)
        self.ui.checkUpBtn.clicked.connect(self.cuIncre)
        self.ui.vaccineBtn.clicked.connect(self.printVcTicket)
        self.ui.vaccineBtn.clicked.connect(self.vcIncre)
        self.ui.dentalBtn.clicked.connect(self.printDtTicket)
        self.ui.dentalBtn.clicked.connect(self.dtIncre)
        self.ui.priorityBtn.clicked.connect(self.printPtTicket)
        self.ui.priorityBtn.clicked.connect(self.ptIncre)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        self.ui.cuTicket.setText(str(checkup))
        self.ui.vcTicket.setText(str(vaccine))
        self.ui.dtTicket.setText(str(dental))
        self.ui.ptTicket.setText(str(priority))


    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def printCuTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.cuTicket.print_(printer)
    def printVcTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.vcTicket.print_(printer)
    def printDtTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.dtTicket.print_(printer)
    def printPtTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.ptTicket.print_(printer)

    def cuIncre(self):
        global checkup
        checkup += 1
        self.ui.cuTicket.setText(str(checkup))
    def vcIncre(self):
        global vaccine
        vaccine += 1
        self.ui.vcTicket.setText(str(vaccine))
    def dtIncre(self):
        global dental
        dental += 1
        self.ui.dtTicket.setText(str(dental))
    def ptIncre(self):
        global priority
        priority += 1
        self.ui.ptTicket.setText(str(priority))






###
    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec()

    def print_preview(self, printer):
        global checkup
        self.ui.textEdit.print_(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = realMainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("EXITING SYSTEM")

