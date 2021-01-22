from dbwindow import *
from patientsGUI import *

GLOBAL_STATE = 0

class UIFunctions(realMainWindow):

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.frame_main_bg_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_main_bg.setStyleSheet("background-color: #ffffff; border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.frame_main_bg.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.frame_main_bg.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        self.ui.saveBtn.clicked.connect(lambda: dbWindow.insertData(self))
        self.ui.saveBtn.clicked.connect(lambda: dbWindow.loadCheckUp(self))
        self.ui.saveBtn.clicked.connect(lambda: dbWindow.loadVaccine(self))
        self.ui.saveBtn.clicked.connect(lambda: dbWindow.loadDental(self))


        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE

class dbWindow(realMainWindow):
##DATABASE
    def loadCheckUp(self):
        self.ui.checkUpTable.setRowCount(150)
        self.ui.checkUpTable.setColumnWidth(0, 90)
        self.ui.checkUpTable.setColumnWidth(2, 30)
        self.ui.checkUpTable.setColumnWidth(3, 150)
        self.ui.checkUpTable.setColumnWidth(4, 80)
        self.ui.checkUpTable.setColumnWidth(5, 100)
        connection = sqlite3.connect('patients')
        cur = connection.cursor()
        pInfo = 'SELECT * FROM checkUp'

        tablerow=0
        results = cur.execute(pInfo)
        for row in results:
            if row[0] < 10:
                ticket = "CU00" + str(row[0])
            elif row[0] > 99:
                ticket = "CU" + str(row[0])
            else:
                ticket = "CU0" + str(row[0])
            self.ui.checkUpTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(ticket))
            self.ui.checkUpTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.checkUpTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.checkUpTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.checkUpTable.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.checkUpTable.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1
    def loadVaccine(self):
        self.ui.vaccineTable.setRowCount(150)
        self.ui.vaccineTable.setColumnWidth(0, 90)
        self.ui.vaccineTable.setColumnWidth(2, 30)
        self.ui.vaccineTable.setColumnWidth(3, 150)
        self.ui.vaccineTable.setColumnWidth(4, 80)
        self.ui.vaccineTable.setColumnWidth(5, 100)
        connection = sqlite3.connect('patients')
        cur = connection.cursor()
        pInfo = 'SELECT * FROM vaccine'

        tablerow=0
        results = cur.execute(pInfo)
        for row in results:
            if row[0] < 10:
                ticket = "VC00" + str(row[0])
            elif row[0] > 99:
                ticket = "VC" + str(row[0])
            else:
                ticket = "VC0" + str(row[0])
            self.ui.vaccineTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(ticket))
            self.ui.vaccineTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.vaccineTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.vaccineTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.vaccineTable.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.vaccineTable.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1
    def loadDental(self):
        self.ui.dentalTable.setRowCount(150)
        self.ui.dentalTable.setColumnWidth(0, 90)
        self.ui.dentalTable.setColumnWidth(2, 30)
        self.ui.dentalTable.setColumnWidth(3, 150)
        self.ui.dentalTable.setColumnWidth(4, 80)
        self.ui.dentalTable.setColumnWidth(5, 100)
        connection = sqlite3.connect('patients')
        cur = connection.cursor()
        pInfo = 'SELECT * FROM dental'

        tablerow=0
        results = cur.execute(pInfo)
        for row in results:
            if row[0] < 10:
                ticket = "DT00" + str(row[0])
            elif row[0] > 99:
                ticket = "DT" + str(row[0])
            else:
                ticket = "DT0" + str(row[0])
            self.ui.dentalTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(ticket))
            self.ui.dentalTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.dentalTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.dentalTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.dentalTable.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.dentalTable.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1

    def insertData(self):
        connection = sqlite3.connect('patients')
        with connection:
            cur = connection.cursor()
            if(self.ui.nameEdit.text()) and (self.ui.ageEdit.text() and
                                              (self.ui.addressEdit.text())) :
                if self.ui.checkUpBox.isChecked():
                    cur.execute("INSERT INTO checkUp(full_name, age, address, contact)"
                                "VALUES('%s', '%s', '%s', '%s')" % (''.join(self.ui.nameEdit.text()),
                                                                    ''.join(self.ui.ageEdit.text()),
                                                                    ''.join(self.ui.addressEdit.text()),
                                                                    ''.join(self.ui.ContactEdit.text())))
                    QMessageBox.about(self, 'Successful', 'Data Inserted Successfully')
                    self.ui.nameEdit.clear()
                    self.ui.ageEdit.clear()
                    self.ui.addressEdit.clear()
                    self.ui.ContactEdit.clear()
                elif self.ui.vaccineBox.isChecked():
                    cur.execute("INSERT INTO vaccine(full_name, age, address, contact)"
                                "VALUES('%s', '%s', '%s', '%s')" % (''.join(self.ui.nameEdit.text()),
                                                                    ''.join(self.ui.ageEdit.text()),
                                                                    ''.join(self.ui.addressEdit.text()),
                                                                    ''.join(self.ui.ContactEdit.text())))
                    self.ui.nameEdit.clear()
                    self.ui.ageEdit.clear()
                    self.ui.addressEdit.clear()
                    self.ui.ContactEdit.clear()
                    QMessageBox.about(self, 'Successful', 'Data Inserted Successfully')
                elif self.ui.dentalBox.isChecked():
                    cur.execute("INSERT INTO dental(full_name, age, address, contact)"
                                "VALUES('%s', '%s', '%s', '%s')" % (''.join(self.ui.nameEdit.text()),
                                                                    ''.join(self.ui.ageEdit.text()),
                                                                    ''.join(self.ui.addressEdit.text()),
                                                                    ''.join(self.ui.ContactEdit.text())))
                    self.ui.nameEdit.clear()
                    self.ui.ageEdit.clear()
                    self.ui.addressEdit.clear()
                    self.ui.ContactEdit.clear()
                    QMessageBox.about(self, 'Successful', 'Data Inserted Successfully')
                else:
                    pass
            else:
                QMessageBox.information(self, 'Information', 'Please Input Necessary Information')


