## ==> GUI FILE
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QSizeGrip, QGraphicsDropShadowEffect

from MyProject import *
## ==> GLOBALS

GLOBAL_STATE = 0
value1 = 1
value2 = 1
value3 = 1
value4 = 1

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

        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        self.btn1 = QShortcut(QKeySequence('1'), self)
        self.btn1.activated.connect(lambda: ticketFunction.ticketIncrement1(self))
        self.btn2 = QShortcut(QKeySequence('2'), self)
        self.btn2.activated.connect(lambda: ticketFunction.ticketIncrement2(self))
        self.btn3 = QShortcut(QKeySequence('3'), self)
        self.btn3.activated.connect(lambda: ticketFunction.ticketIncrement3(self))
        self.btn4 = QShortcut(QKeySequence('4'), self)
        self.btn4.activated.connect(lambda: ticketFunction.ticketIncrement4(self))

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE

class ticketFunction(realMainWindow):
    def ticketIncrement1(self):
        global value1
        self.ui.label_ticketValue1.setText("C" + str(value1))
        self.ui.label_ticketValue.setText("C" + str(value1))
        self.ui.label_procedure.setText("Please Proceed To")
        self.ui.label_roomNo.setText("Room 101")
        value1 += 1
    def ticketIncrement2(self):
        global value2
        self.ui.label_ticketValue2.setText("V" + str(value2))
        self.ui.label_ticketValue.setText("V" + str(value2))
        self.ui.label_procedure.setText("Please Proceed To")
        self.ui.label_roomNo.setText("Room 102")
        value2 += 1
    def ticketIncrement3(self):
        global value3
        self.ui.label_ticketValue3.setText("D" + str(value3))
        self.ui.label_ticketValue.setText("D" + str(value3))
        self.ui.label_procedure.setText("Please Proceed To")
        self.ui.label_roomNo.setText("Room 103")
        value3 += 1

    def ticketIncrement4(self):
        global value4
        self.ui.label_ticketValue4.setText("P" + str(value4))
        self.ui.label_ticketValue.setText("P" + str(value4))
        self.ui.label_procedure.setText("You Can Now")
        self.ui.label_roomNo.setText("Proceed")
        value4 += 1


