# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_centralwidget_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.frame_centralwidget_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_centralwidget_layout.setSpacing(0)
        self.frame_centralwidget_layout.setObjectName("frame_centralwidget_layout")
        self.frame_main_bg = QtWidgets.QFrame(self.centralwidget)
        self.frame_main_bg.setStyleSheet("border-radius: 10px;\n"
"background-color: white;")
        self.frame_main_bg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_bg.setObjectName("frame_main_bg")
        self.frame_main_bg_layout = QtWidgets.QVBoxLayout(self.frame_main_bg)
        self.frame_main_bg_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_bg_layout.setSpacing(0)
        self.frame_main_bg_layout.setObjectName("frame_main_bg_layout")
        self.frame_title_bar = QtWidgets.QFrame(self.frame_main_bg)
        self.frame_title_bar.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_title_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_title_bar.setStyleSheet("")
        self.frame_title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_bar.setObjectName("frame_title_bar")
        self.title_bar_layout = QtWidgets.QHBoxLayout(self.frame_title_bar)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar_layout.setSpacing(0)
        self.title_bar_layout.setObjectName("title_bar_layout")
        self.frame_title = QtWidgets.QFrame(self.frame_title_bar)
        self.frame_title.setStyleSheet("background-color: none;")
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.title_layout = QtWidgets.QHBoxLayout(self.frame_title)
        self.title_layout.setContentsMargins(5, 0, 0, 0)
        self.title_layout.setSpacing(0)
        self.title_layout.setObjectName("title_layout")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(52, 217, 182);")
        self.label_title.setObjectName("label_title")
        self.title_layout.addWidget(self.label_title)
        self.title_bar_layout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.frame_title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setStyleSheet("background-color: none;")
        self.frame_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.btn_layout = QtWidgets.QHBoxLayout(self.frame_btns)
        self.btn_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_layout.setSpacing(0)
        self.btn_layout.setObjectName("btn_layout")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 0);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.btn_layout.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(85, 0, 255);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 0, 127);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.btn_layout.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_close.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 60, 105);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.btn_layout.addWidget(self.btn_close)
        self.title_bar_layout.addWidget(self.frame_btns)
        self.frame_main_bg_layout.addWidget(self.frame_title_bar)
        self.frame_content_bar = QtWidgets.QFrame(self.frame_main_bg)
        self.frame_content_bar.setAccessibleName("")
        self.frame_content_bar.setStyleSheet("border-radius: 1px;")
        self.frame_content_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_bar.setObjectName("frame_content_bar")
        self.frame_contentBar_layout = QtWidgets.QHBoxLayout(self.frame_content_bar)
        self.frame_contentBar_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_contentBar_layout.setSpacing(10)
        self.frame_contentBar_layout.setObjectName("frame_contentBar_layout")
        self.frame_leftBody = QtWidgets.QFrame(self.frame_content_bar)
        self.frame_leftBody.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_leftBody.setStyleSheet("")
        self.frame_leftBody.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_leftBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_leftBody.setObjectName("frame_leftBody")
        self.frame_leftBody_layout = QtWidgets.QVBoxLayout(self.frame_leftBody)
        self.frame_leftBody_layout.setContentsMargins(10, 0, 0, 0)
        self.frame_leftBody_layout.setSpacing(10)
        self.frame_leftBody_layout.setObjectName("frame_leftBody_layout")
        self.frame_service1 = QtWidgets.QFrame(self.frame_leftBody)
        self.frame_service1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 10, 153, 255), stop:1 rgba(0, 145, 255, 150));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_service1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_service1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_service1.setObjectName("frame_service1")
        self.frame_service1_layout = QtWidgets.QVBoxLayout(self.frame_service1)
        self.frame_service1_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_service1_layout.setSpacing(0)
        self.frame_service1_layout.setObjectName("frame_service1_layout")
        self.frame_ticket1 = QtWidgets.QFrame(self.frame_service1)
        self.frame_ticket1.setStyleSheet("background: none;")
        self.frame_ticket1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ticket1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ticket1.setObjectName("frame_ticket1")
        self.frame_ticket1_layout = QtWidgets.QHBoxLayout(self.frame_ticket1)
        self.frame_ticket1_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_ticket1_layout.setSpacing(0)
        self.frame_ticket1_layout.setObjectName("frame_ticket1_layout")
        self.label_ticketNo1 = QtWidgets.QLabel(self.frame_ticket1)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_ticketNo1.setFont(font)
        self.label_ticketNo1.setIndent(20)
        self.label_ticketNo1.setObjectName("label_ticketNo1")
        self.frame_ticket1_layout.addWidget(self.label_ticketNo1)
        self.label_ticketValue1 = QtWidgets.QLabel(self.frame_ticket1)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_ticketValue1.setFont(font)
        self.label_ticketValue1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ticketValue1.setIndent(20)
        self.label_ticketValue1.setObjectName("label_ticketValue1")
        self.frame_ticket1_layout.addWidget(self.label_ticketValue1)
        self.frame_service1_layout.addWidget(self.frame_ticket1)
        self.label_room1 = QtWidgets.QLabel(self.frame_service1)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_room1.setFont(font)
        self.label_room1.setStyleSheet("background: none;")
        self.label_room1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_room1.setObjectName("label_room1")
        self.frame_service1_layout.addWidget(self.label_room1)
        self.frame_leftBody_layout.addWidget(self.frame_service1)
        self.frame_service2 = QtWidgets.QFrame(self.frame_leftBody)
        self.frame_service2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 10, 153, 255), stop:1 rgba(0, 145, 255, 150));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_service2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_service2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_service2.setObjectName("frame_service2")
        self.frame_service2_layout = QtWidgets.QVBoxLayout(self.frame_service2)
        self.frame_service2_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_service2_layout.setSpacing(0)
        self.frame_service2_layout.setObjectName("frame_service2_layout")
        self.frame_ticket2 = QtWidgets.QFrame(self.frame_service2)
        self.frame_ticket2.setStyleSheet("background: none;")
        self.frame_ticket2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ticket2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ticket2.setObjectName("frame_ticket2")
        self.frame_ticket2_layout = QtWidgets.QHBoxLayout(self.frame_ticket2)
        self.frame_ticket2_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_ticket2_layout.setSpacing(0)
        self.frame_ticket2_layout.setObjectName("frame_ticket2_layout")
        self.label_ticketNo2 = QtWidgets.QLabel(self.frame_ticket2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_ticketNo2.setFont(font)
        self.label_ticketNo2.setIndent(20)
        self.label_ticketNo2.setObjectName("label_ticketNo2")
        self.frame_ticket2_layout.addWidget(self.label_ticketNo2)
        self.label_ticketValue2 = QtWidgets.QLabel(self.frame_ticket2)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_ticketValue2.setFont(font)
        self.label_ticketValue2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ticketValue2.setIndent(20)
        self.label_ticketValue2.setObjectName("label_ticketValue2")
        self.frame_ticket2_layout.addWidget(self.label_ticketValue2)
        self.frame_service2_layout.addWidget(self.frame_ticket2)
        self.label_room2 = QtWidgets.QLabel(self.frame_service2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_room2.setFont(font)
        self.label_room2.setStyleSheet("background: none;")
        self.label_room2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_room2.setObjectName("label_room2")
        self.frame_service2_layout.addWidget(self.label_room2)
        self.frame_leftBody_layout.addWidget(self.frame_service2)
        self.frame_service3 = QtWidgets.QFrame(self.frame_leftBody)
        self.frame_service3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 10, 153, 255), stop:1 rgba(0, 145, 255, 150));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_service3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_service3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_service3.setObjectName("frame_service3")
        self.frame_service3_layout = QtWidgets.QVBoxLayout(self.frame_service3)
        self.frame_service3_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_service3_layout.setSpacing(0)
        self.frame_service3_layout.setObjectName("frame_service3_layout")
        self.frame_ticket3 = QtWidgets.QFrame(self.frame_service3)
        self.frame_ticket3.setStyleSheet("background: none;")
        self.frame_ticket3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ticket3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ticket3.setObjectName("frame_ticket3")
        self.frame_ticket3_layout = QtWidgets.QHBoxLayout(self.frame_ticket3)
        self.frame_ticket3_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_ticket3_layout.setSpacing(0)
        self.frame_ticket3_layout.setObjectName("frame_ticket3_layout")
        self.label_ticketNo3 = QtWidgets.QLabel(self.frame_ticket3)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_ticketNo3.setFont(font)
        self.label_ticketNo3.setIndent(20)
        self.label_ticketNo3.setObjectName("label_ticketNo3")
        self.frame_ticket3_layout.addWidget(self.label_ticketNo3)
        self.label_ticketValue3 = QtWidgets.QLabel(self.frame_ticket3)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_ticketValue3.setFont(font)
        self.label_ticketValue3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ticketValue3.setIndent(20)
        self.label_ticketValue3.setObjectName("label_ticketValue3")
        self.frame_ticket3_layout.addWidget(self.label_ticketValue3)
        self.frame_service3_layout.addWidget(self.frame_ticket3)
        self.label_room3 = QtWidgets.QLabel(self.frame_service3)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_room3.setFont(font)
        self.label_room3.setStyleSheet("background: none;")
        self.label_room3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_room3.setObjectName("label_room3")
        self.frame_service3_layout.addWidget(self.label_room3)
        self.frame_leftBody_layout.addWidget(self.frame_service3)
        self.frame_contentBar_layout.addWidget(self.frame_leftBody)
        self.frame_rightBody = QtWidgets.QFrame(self.frame_content_bar)
        self.frame_rightBody.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_rightBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rightBody.setObjectName("frame_rightBody")
        self.frame_rightBody_layout = QtWidgets.QVBoxLayout(self.frame_rightBody)
        self.frame_rightBody_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_rightBody_layout.setSpacing(0)
        self.frame_rightBody_layout.setObjectName("frame_rightBody_layout")
        self.label_compName = QtWidgets.QLabel(self.frame_rightBody)
        self.label_compName.setMinimumSize(QtCore.QSize(0, 100))
        self.label_compName.setMaximumSize(QtCore.QSize(300, 130))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_compName.setFont(font)
        self.label_compName.setStyleSheet("border-radius: 20px;\n"
"background-image: url(:/newPrefix/01.png);")
        self.label_compName.setText("")
        self.label_compName.setTextFormat(QtCore.Qt.RichText)
        self.label_compName.setPixmap(QtGui.QPixmap(":/newPrefix/01.png"))
        self.label_compName.setScaledContents(True)
        self.label_compName.setIndent(10)
        self.label_compName.setObjectName("label_compName")
        self.frame_rightBody_layout.addWidget(self.label_compName)
        self.label_ticket = QtWidgets.QLabel(self.frame_rightBody)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_ticket.setFont(font)
        self.label_ticket.setStyleSheet("color: rgb(71, 214, 214); background-color:none;")
        self.label_ticket.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ticket.setObjectName("label_ticket")
        self.frame_rightBody_layout.addWidget(self.label_ticket)
        self.label_ticketValue = QtWidgets.QLabel(self.frame_rightBody)
        font = QtGui.QFont()
        font.setPointSize(120)
        self.label_ticketValue.setFont(font)
        self.label_ticketValue.setStyleSheet("color: rgb(255, 0, 0); background-color:none")
        self.label_ticketValue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ticketValue.setObjectName("label_ticketValue")
        self.frame_rightBody_layout.addWidget(self.label_ticketValue)
        self.label_procedure = QtWidgets.QLabel(self.frame_rightBody)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_procedure.setFont(font)
        self.label_procedure.setStyleSheet("color: rgb(71, 214, 214); background-color:none")
        self.label_procedure.setAlignment(QtCore.Qt.AlignCenter)
        self.label_procedure.setObjectName("label_procedure")
        self.frame_rightBody_layout.addWidget(self.label_procedure)
        self.label_roomNo = QtWidgets.QLabel(self.frame_rightBody)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_roomNo.setFont(font)
        self.label_roomNo.setStyleSheet("color: rgb(255, 0, 0); background-color:none")
        self.label_roomNo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_roomNo.setObjectName("label_roomNo")
        self.frame_rightBody_layout.addWidget(self.label_roomNo)
        self.frame_contentBar_layout.addWidget(self.frame_rightBody)
        self.frame_main_bg_layout.addWidget(self.frame_content_bar)
        self.frame_etc_bar = QtWidgets.QFrame(self.frame_main_bg)
        self.frame_etc_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_etc_bar.setStyleSheet("")
        self.frame_etc_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_etc_bar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_etc_bar.setObjectName("frame_etc_bar")
        self.etc_layout = QtWidgets.QHBoxLayout(self.frame_etc_bar)
        self.etc_layout.setContentsMargins(0, 0, 0, 5)
        self.etc_layout.setSpacing(0)
        self.etc_layout.setObjectName("etc_layout")
        self.frame_credits = QtWidgets.QFrame(self.frame_etc_bar)
        self.frame_credits.setStyleSheet("background-color: none;")
        self.frame_credits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_credits.setObjectName("frame_credits")
        self.credits_layout = QtWidgets.QHBoxLayout(self.frame_credits)
        self.credits_layout.setContentsMargins(5, -1, -1, 0)
        self.credits_layout.setObjectName("credits_layout")
        self.label_credits = QtWidgets.QLabel(self.frame_credits)
        self.label_credits.setStyleSheet("color: rgb(99, 99, 149);")
        self.label_credits.setObjectName("label_credits")
        self.credits_layout.addWidget(self.label_credits)
        self.etc_layout.addWidget(self.frame_credits)
        self.frame_grip = QtWidgets.QFrame(self.frame_etc_bar)
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("background-color: none; padding: 5px; ")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.etc_layout.addWidget(self.frame_grip)
        self.frame_main_bg_layout.addWidget(self.frame_etc_bar)
        self.frame_centralwidget_layout.addWidget(self.frame_main_bg)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Qeueuing System"))
        self.label_ticketNo1.setText(_translate("MainWindow", "Ticket No."))
        self.label_ticketValue1.setText(_translate("MainWindow", "CU00"))
        self.label_room1.setText(_translate("MainWindow", "Room 101"))
        self.label_ticketNo2.setText(_translate("MainWindow", "Ticket No."))
        self.label_ticketValue2.setText(_translate("MainWindow", "VC00"))
        self.label_room2.setText(_translate("MainWindow", "Room 102"))
        self.label_ticketNo3.setText(_translate("MainWindow", "Ticket No."))
        self.label_ticketValue3.setText(_translate("MainWindow", "DT00"))
        self.label_room3.setText(_translate("MainWindow", "Room 103"))
        self.label_ticket.setText(_translate("MainWindow", "Ticket Number"))
        self.label_ticketValue.setText(_translate("MainWindow", "NULL"))
        self.label_procedure.setText(_translate("MainWindow", "Please Proceed To"))
        self.label_roomNo.setText(_translate("MainWindow", "Room 101"))
        self.label_credits.setText(_translate("MainWindow", "Powered By: Python"))
import test
