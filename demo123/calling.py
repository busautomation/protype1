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

class Call_Pick(object):
    #Wakie Takie
    GPIO.setmode(GPIO.BOARD)
    port = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
    def setupUi(self, CallPick):
        #print("........")
        self.port.write(b'ATA\r')
        rcv = self.port.read(10)
        CallPick.setObjectName("CallPick")
        CallPick.resize(400, 240)
        CallPick.setMinimumSize(QtCore.QSize(400, 240))
        CallPick.setMaximumSize(QtCore.QSize(400, 16777215))
        CallPick.setStyleSheet("background:black;")
        self.calling_window = QtWidgets.QWidget(CallPick)
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
        ##

        ##
        self.call_cut_button = QtWidgets.QPushButton(self.calling_window)
        self.call_cut_button.setGeometry(QtCore.QRect(200, 100, 141, 81))
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
        CallPick.setCentralWidget(self.calling_window)
        #print("........")
        self.retranslateUi(CallPick)
        QtCore.QMetaObject.connectSlotsByName(CallPick)
    def cutt(self):
        try:
            
            self.port.write(b'ATH\r')
            time.sleep(1)
            rcv = self.port.read(10)
        #print(rcv.decode())
        except:
            print("..cuttpick")
   
    def retranslateUi(self, CallPick):
        _translate = QtCore.QCoreApplication.translate
        CallPick.setWindowTitle(_translate("CallPick", "CallPick"))
        self.person_name.setText(_translate("CallPick", "Incoming"))
        self.call_cut_button.setText(_translate("CallPick", ""))
        #self.call_pick_button.setText(_translate("CallPick", ""))
        #print("........")

def main():
    import sys
    print("callling")
    app = QtWidgets.QApplication(sys.argv)
    CallPick = QtWidgets.QMainWindow()
    ui = Call_Pick()
    ui.setupUi(CallPick)
    CallPick.show()
    
        
            
                               
    sys.exit(app.exec_())
