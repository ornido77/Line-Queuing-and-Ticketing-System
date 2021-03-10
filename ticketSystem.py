import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent, QSizeF, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIntValidator, QTextDocument)
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
checkup1 = 0
vaccine1 = 0
dental1 = 0
priority1 = 0
now = QDate.currentDate()
date = now.toString(Qt.ISODate)
time = QTime.currentTime()
timenow = time.toString()

class realMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.showTime
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
        self.btn1 = QShortcut(QKeySequence('c'), self)
        self.btn1.activated.connect(self.cprint_preview_dialog)
        self.btn2 = QShortcut(QKeySequence('v'), self)
        self.btn2.activated.connect(self.vprint_preview_dialog)
        self.btn3 = QShortcut(QKeySequence('d'), self)
        self.btn3.activated.connect(self.dprint_preview_dialog)
        self.btn4 = QShortcut(QKeySequence('p'), self)
        self.btn4.activated.connect(self.pprint_preview_dialog)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm:ss")
        self.ui.dateTime.setText(text)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

        ##### TICKETS
        # CHECKUP
        self.cuhtml ="<p class= 'head'>Bagbaguin Health Center</p><p class= 'head'> and Lying In Clinic</p>" \
                    "<p class= 'service'>Service: Vaccine       /       Room: 101</p> <p class = 'ticket'>C%s</p>" \
                    "<p class= 'dateTime'>%s %s</p>" % (str(checkup), str(date), self.ui.dateTime.text())
        self.cuDoc = QtGui.QTextDocument(self)
        self.cuDoc.setDefaultStyleSheet(".head { font-size: 60px; text-align: center }" ".service{ font-size: 45px; text-align: center}"
                                        ".ticket{ font-size: 275px; font-style: bold; text-align: center}" ".dateTime{font-size: 70px; text-align: center}")
        self.cuDoc.setHtml(self.cuhtml)

        # VACCINE
        self.vchtml = "<p class= 'head'>Bagbaguin Health Center</p><p class= 'head'> and Lying In Clinic</p>"\
                    "<p class= 'service'>Service: Vaccine       /       Room: 102</p><p class = 'ticket'>V%s</p>" \
                    "<p class= 'dateTime'>%s %s</p>" % (str(vaccine), str(date), self.ui.dateTime.text())
        self.vcDoc = QtGui.QTextDocument(self)
        self.vcDoc.setDefaultStyleSheet(".head { font-size: 60px; text-align:center }" ".service{ font-size: 45px; text-align: center}"
                                        ".ticket{ font-size: 275px; text-align: center; font-style: bold}" ".dateTime{font-size: 70px; text-align: center}")
        self.vcDoc.setHtml(self.vchtml)

        # DENTAL
        self.dthtml = "<p class= 'head'>Bagbaguin Health Center</p><p class= 'head'> and Lying In Clinic</p>" \
                      "<p class= 'service'>Service: Vaccine       /       Room: 103</p> <p class = 'ticket'>D%s</p>" \
                      "<p class= 'dateTime'>%s %s</p>" % (str(dental), str(date), self.ui.dateTime.text())
        self.dtDoc = QtGui.QTextDocument(self)
        self.dtDoc.setDefaultStyleSheet(".head { font-size: 60px; text-align:center }" ".service{ font-size: 45px; text-align: center}"
                                        ".ticket{ font-size: 275px; text-align: center; font-style: bold}" ".dateTime{font-size: 70px; text-align: center}")
        self.dtDoc.setHtml(self.dthtml)

        # PRIORITY
        self.pthtml = "<p class= 'head'>Bagbaguin Health Center</p><p class= 'head'> and Lying In Clinic</p>" \
                      "<p class= 'service'>PRIORITY</p> <p class = 'ticket'>P%s</p>" \
                      "<p class= 'dateTime'>%s %s</p>" % (str(priority), str(date), self.ui.dateTime.text())
        self.ptDoc = QtGui.QTextDocument(self)
        self.ptDoc.setDefaultStyleSheet(".head { font-size: 60px; text-align:center }" ".service{ font-size: 45px; text-align: center}"
                                        ".ticket{ font-size: 275px; text-align: center; font-style: bold}" ".dateTime{font-size: 70px; text-align: center}")
        self.ptDoc.setHtml(self.pthtml)



        self.ui.cuTicket1.setText(str(checkup1))
        self.ui.vcTicket1.setText(str(vaccine1))
        self.ui.dtTicket1.setText(str(dental1))
        self.ui.ptTicket1.setText(str(priority1))



    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

### PRINT TICKET
    def printCuTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A8)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.cuDoc.print_(printer)
    def printVcTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A8)
        self.vcDoc.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.vcDoc.print_(printer)
    def printDtTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A8)
        self.dtDoc.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.dtDoc.print_(printer)
    def printPtTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A8)
        self.ptDoc.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ptDoc.print_(printer)
### INCREMENT
    def cuIncre(self):
        global checkup, checkup1
        checkup += 1
        checkup1 += 1
        self.cuDoc.setHtml(self.cuhtml)
        self.ui.cuTicket1.setText(str(checkup1))
    def vcIncre(self):
        global vaccine, vaccine1
        vaccine += 1
        vaccine1 += 1
        self.vcDoc.setHtml(self.vchtml)
        self.ui.vcTicket1.setText(str(vaccine1))
    def dtIncre(self):
        global dental, dental1
        dental += 1
        dental1 += 1
        self.dtDoc.setHtml(self.dthtml)
        self.ui.dtTicket1.setText(str(dental1))
    def ptIncre(self):
        global priority, priority1
        priority += 1
        priority1 += 1
        self.ptDoc.setHtml(self.pthtml)
        self.ui.ptTicket1.setText(str(priority1))

### PREVIEW
    def cprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A8)
        self.cuDoc.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.cprint_preview)
        previewDialog.exec()

    def cprint_preview(self, printer):
        self.cuDoc.print_(printer)

    def vprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A8)
        self.vcDoc.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.vprint_preview)
        previewDialog.exec()

    def vprint_preview(self, printer):
        self.vcDoc.print_(printer)

    def dprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A8)
        self.dtDoc.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.dprint_preview)
        previewDialog.exec()

    def dprint_preview(self, printer):
        self.dtDoc.print_(printer)

    def pprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A8)
        self.ptDoc.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.pprint_preview)
        previewDialog.exec()

    def pprint_preview(self, printer):
        self.ptDoc.print_(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = realMainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("EXITING SYSTEM")

