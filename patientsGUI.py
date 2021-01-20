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
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('patients')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('checkUp')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Ticket Number")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Age")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Address")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Contact")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Time In")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Time Out")
        self.ui.cuView.setModel(self.model)
        self.ui.cuView.setColumnWidth(0, 90)
        self.ui.cuView.setColumnWidth(2, 30)
        self.ui.cuView.setColumnWidth(3, 140)
        self.ui.cuView.setColumnWidth(4, 80)
        self.ui.cuView.setColumnWidth(5, 60)
        self.ui.cuView.setColumnWidth(6, 60)
        self.ui.saveBtn.clicked.connect(self.addToDb)
        self.show()
        self.ui.timeOutBtn.clicked.connect(self.timeOut)
        self.ui.saveAndPrintBtn.clicked.connect(self.saveAndPrint)
        self.i = self.model.rowCount()
        self.onlyInt = QIntValidator()
        self.ui.ageEdit.setValidator(self.onlyInt)
        self.ui.ContactEdit.setValidator(self.onlyInt)
        self.ui.timeInEdit.setValidator(self.onlyInt)
        self.ui.ageEdit.setMaxLength(3)
        self.ui.ContactEdit.setMaxLength(11)
        self.ui.timeInEdit.setMaxLength(4)

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def addToDb(self):
        try:
            if (self.ui.nameEdit.text()) and (self.ui.ageEdit.text() and
                                              (self.ui.addressEdit.text()) and (self.ui.timeInEdit.text())) :
                self.model.insertRows(self.i, 1)
                self.model.setData(self.model.index(self.i, 1), self.ui.nameEdit.text())
                self.model.setData(self.model.index(self.i, 2), self.ui.ageEdit.text())
                self.model.setData(self.model.index(self.i, 3), self.ui.addressEdit.text())
                self.model.setData(self.model.index(self.i, 4), str(self.ui.ContactEdit.text()))
                self.model.setData(self.model.index(self.i, 5), self.ui.timeInEdit.text())
                self.model.submitAll()
                self.i += 1
                self.ui.nameEdit.clear()
                self.ui.ageEdit.clear()
                self.ui.addressEdit.clear()
                self.ui.ContactEdit.clear()
                self.ui.timeInEdit.clear()
                QMessageBox.information(QMessageBox(), 'Successful', 'Data Input Successfully!')
            else:
                QMessageBox.warning(QMessageBox(), "Unsuccessful", "Please Input Necessary Informations!")
        except:
            QMessageBox.warning(QMessageBox(),'Unsuccessful','Data Input Unsuccessfully!')

    def timeOut(self):
        if self.ui.cuView.currentIndex().row() > -1:
            text, ok = QInputDialog.getInt(self, "TIME OUT", "Enter Patient's Time Out")
            if ok:
                record = self.model.record(self.ui.cuView.currentIndex().row())
                if text > 2359:
                    QMessageBox.warning(QMessageBox(), 'Unsuccessful', 'Please Input Military Time!')
                else:
                    record.setValue(6, text)
                    self.model.setRecord(self.ui.cuView.currentIndex().row(), record)
                    QMessageBox.information(QMessageBox(), 'Successful', 'Time Out Successfully!')
        else:
            QMessageBox.question(self, 'Message', "Please select a row would you like to update", QMessageBox.Ok)
            self.show()
    def saveAndPrint(self):
        QMessageBox.warning(QMessageBox(), 'Unsuccessful', 'ERROR!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = realMainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("EXITING SYSTEM")
