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

class Gate(object):
    #Wakie Takie
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)
    gate=37# Use physical pin numbering
     # Set pin 8 to be an output pin and set initial value to low (off)

    def setupUi(self, gateopen):
        GPIO.setup(self.gate, GPIO.OUT)
        gateopen.setObjectName("gateopen")
        gateopen.resize(400, 240)
        gateopen.setMinimumSize(QtCore.QSize(400, 240))
        gateopen.setMaximumSize(QtCore.QSize(400, 16777215))
        gateopen.setStyleSheet("background:black;")
        self.calling_window = QtWidgets.QWidget(gateopen)
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
        self.gate_open_button = QtWidgets.QPushButton(self.calling_window)
        self.gate_open_button.setGeometry(QtCore.QRect(50, 100, 141, 81))
        self.gate_open_button.setIcon(QIcon('/home/pi/Desktop/demo/phone_reject.png'))
        self.gate_open_button.setIconSize(QSize(80,80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.gate_open_button.setFont(font)
        self.gate_open_button.setStyleSheet("color:white")
        self.gate_open_button.setObjectName("gate_open_button")
        self.gate_open_button.clicked.connect(self.open)
        ##
        self.gate_close_button = QtWidgets.QPushButton(self.calling_window)
        self.gate_close_button.setGeometry(QtCore.QRect(200, 100, 141, 81))
        self.gate_close_button.setIcon(QIcon('/home/pi/Desktop/demo/phone_reject.png'))
        self.gate_close_button.setIconSize(QSize(80,80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.gate_close_button.setFont(font)
        self.gate_close_button.setStyleSheet("color:white")
        self.gate_close_button.setObjectName("gate_open_button")
        self.gate_close_button.clicked.connect(self.close)
        gateopen.setCentralWidget(self.calling_window)
        #print("........")
        self.retranslateUi(gateopen)
        QtCore.QMetaObject.connectSlotsByName(gateopen)
    def close(self):
        try:
            
            GPIO.output(self.gate, GPIO.LOW)
            self.person_name.setText("Closed")
        #print(rcv.decode())
        except:
            print("..cuttpick")
    def open(self):
        try:
            
            GPIO.output(self.gate, GPIO.HIGH)
            self.person_name.setText("Open")
        #print(rcv.decode())
        except:
            print("..cuttpick")
   
    def retranslateUi(self, gateopen):
        _translate = QtCore.QCoreApplication.translate
        gateopen.setWindowTitle(_translate("gateopen", "gate"))
        self.person_name.setText(_translate("gateopen", "Gate Closed"))
        self.gate_open_button.setText(_translate("gateopen", ""))
        self.gate_close_button.setText(_translate("gateopen", ""))
        #print("........")

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gateopen = QtWidgets.QMainWindow()
    ui = Gate()
    ui.setupUi(gateopen)
    gateopen.show()                          
    sys.exit(app.exec_())

main()

