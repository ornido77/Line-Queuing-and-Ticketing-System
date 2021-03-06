## ==> GUI FILE
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QSizeGrip, QGraphicsDropShadowEffect

from MyProject import *
## ==> GLOBALS

GLOBAL_STATE = 0
lcd1 = 1
lcd2 = 1

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
            self.ui.frame_main_bg.setStyleSheet("background-color: #000000; border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.frame_main_bg_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_main_bg.setStyleSheet("background-color: #000000; border-radius: 10px;")
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

        self.sc1 = QShortcut(QKeySequence('1'), self)
        self.sc1.activated.connect(self.lcd1Increment)
        self.sc2 = QShortcut(QKeySequence('2'), self)
        self.sc2.activated.connect(self.lcd2Increment)

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE


