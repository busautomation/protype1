# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calling1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import serial
import os, time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
class Call_cut(object):
    #Wakie Takie
    
    port = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
    def setupUi(self, CallCut):
        CallCut.setObjectName("CallCut")
        CallCut.resize(400, 240)
        CallCut.setMinimumSize(QtCore.QSize(400, 240))
        CallCut.setMaximumSize(QtCore.QSize(400, 16777215))
        CallCut.setStyleSheet("background:black;")
        self.calling_window = QtWidgets.QWidget(CallCut)
        self.calling_window.setObjectName("calling_window")
        self.person_name = QtWidgets.QLabel(self.calling_window)
        self.person_name.setGeometry(QtCore.QRect(40, 20, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.person_name.setFont(font)
        self.person_name.setStyleSheet("color:white;")
        self.person_name.setAlignment(QtCore.Qt.AlignCenter)
        self.person_name.setObjectName("person_name")
        self.call_cut_button = QtWidgets.QPushButton(self.calling_window)
        self.call_cut_button.setGeometry(QtCore.QRect(130, 100, 141, 81))
        self.call_cut_button.setIcon(QIcon('/home/pi/Desktop/demo/phone_reject.png'))
        self.call_cut_button.setIconSize(QSize(80,80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.call_cut_button.setFont(font)
        self.call_cut_button.setStyleSheet("color:white")
        self.call_cut_button.setObjectName("call_cut_button")
        self.call_cut_button.clicked.connect(self.cutt)
        CallCut.setCentralWidget(self.calling_window)

        self.retranslateUi(CallCut)
        QtCore.QMetaObject.connectSlotsByName(CallCut)
        
                
        
    def cutt(self):
                  
        self.port.write(b'ATH\r')
        time.sleep(1)
        rcv = self.port.read(10)
        #print(rcv.decode())
       

        
        
    def retranslateUi(self, CallCut):
        _translate = QtCore.QCoreApplication.translate
        CallCut.setWindowTitle(_translate("CallCut", "CallCut"))
        self.person_name.setText(_translate("CallCut", "PERSON NAME"))
        self.call_cut_button.setText(_translate("CallCut", ""))
    def wakiewatch():
    
        while True:
                rcv = port.read(50)#gsm Value reasding
                print(rcv.decode())
                rcv =rcv.decode()
                time.sleep(1)
                if '+CIEV: "CALL",0' in rcv:
                        print("close ")
                    #cut the tab

def application():
    app = QtWidgets.QApplication(sys.argv)
    CallCut = QtWidgets.QMainWindow()
    ui = Call_cut()
    ui.setupUi(CallCut)
    #CallCut.show()
    sys.exit(app.exec_())

def functonf():
    import sys
    import threading
    t1 = threading.Thread(target = application)
    t2 = threading.Thread(target = wakiewatch)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    