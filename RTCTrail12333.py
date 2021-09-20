# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demo1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
#camara output import
import cv2
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QApplication,QDialog

#rtc

import SDL_DS3231
from PyQt5.QtCore import QTimer, QTime, Qt


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from call_cut_window import *
from calling import *
from camara1 import *
#from cameracall import *
import serial
import os, time
import RPi.GPIO as GPIO

import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib
from multiprocessing import Process
import sys
#import cv2 as cv


class Ui_MainWindow(object):
     #BLE Variable
    status="playing"
    track = "no Music"
    player_iface = None
    transport_prop_iface = None
    bus = None
    obj = None
    mgr=None
    #ds3231=None
    #Wakie Takie
    GPIO.setmode(GPIO.BOARD)
    port = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
    #rtc
    ##GAte
    GPIO.setwarnings(False) # Ignore warning for now
  
    gate=37
    ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        #MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setStyleSheet("background-color:black;")
        
        #central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #rtc time
        #timer = QTimer(self)
        #timer.timeout.connect(self.showTime)
  
        # update the timer every second
        #timer.start(1000)
        self.rtc_time_label = QtWidgets.QLabel(self.centralwidget)
        self.rtc_time_label.setGeometry(QtCore.QRect(0,5, 160,20))
        self.rtc_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rtc_time_label.setObjectName("rtc_time_label")
        self.rtc_time_label.setStyleSheet("color:white;")
        a=self.ds3231.read_datetime()
        #print(type(a))
        time.sleep(10.0)
        self.rtc_time_label.setText(str(a))
        #self.ds3231.write_now()
        
        
        
        #main tab that contain all 5 windows music,camara,calling,stats,setting 
        self.main_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tab.setGeometry(QtCore.QRect(0, 30, 801, 481))#adjusted to show time
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_tab.sizePolicy().hasHeightForWidth())
        self.main_tab.setSizePolicy(sizePolicy)
        self.main_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.main_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_tab.setStyleSheet("QTabBar::tab { height: 86px; width: 80px; }QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 2px solid #C2C7CB;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #9B9B9B;\n"
"border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"QTabBar::tab:selected { font: bold; color: skyblue; }")
        self.main_tab.setTabPosition(QtWidgets.QTabWidget.East)
        self.main_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_tab.setIconSize(QtCore.QSize(120,80))
        self.main_tab.setObjectName("main_tab")
        
        #music window TAB 1
        self.music_tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.music_tab.setFont(font)
        self.music_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.music_tab.setAutoFillBackground(False)
        self.music_tab.setObjectName("music_tab")
        
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

        #music window box main tabs
        self.music_box_window = QtWidgets.QTabWidget(self.music_tab)
        self.music_box_window.setGeometry(QtCore.QRect(0, 0, 791, 491))
        self.music_box_window.setIconSize(QtCore.QSize(100, 60))
        self.music_box_window.setObjectName("music_box_window")
        
        #music box tab 1 fm #
        self.fm = QtWidgets.QWidget()
        self.fm.setObjectName("fm")
        
        #music box  music tab fm tab fm_label
        self.fm_label = QtWidgets.QLabel(self.fm)
        self.fm_label.setGeometry(QtCore.QRect(190, 70, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.fm_label.setFont(font)
        self.fm_label.setStyleSheet("background:none;color:white;border:none;")
        self.fm_label.setObjectName("fm_label")
        
        #music box  music tab fm tab fm_channel_label 
        self.fm_channel_label = QtWidgets.QLabel(self.fm)
        self.fm_channel_label.setGeometry(QtCore.QRect(310, 70, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.fm_channel_label.setFont(font)
        self.fm_channel_label.setStyleSheet("background:none;color:white;border:none;")
        self.fm_channel_label.setObjectName("fm_channel_label")
        
        #music box  music tab fm tab horizontal slider
        self.horizontalSlider_fm_channels = QtWidgets.QSlider(self.fm)
        self.horizontalSlider_fm_channels.setEnabled(True)
        self.horizontalSlider_fm_channels.setGeometry(QtCore.QRect(130, 170, 431, 26))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        self.horizontalSlider_fm_channels.setFont(font)
        self.horizontalSlider_fm_channels.setTabletTracking(False)
        self.horizontalSlider_fm_channels.setAcceptDrops(False)
        self.horizontalSlider_fm_channels.setAutoFillBackground(False)
        self.horizontalSlider_fm_channels.setStyleSheet("background:none;")
        self.horizontalSlider_fm_channels.setTracking(False)
        self.horizontalSlider_fm_channels.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_fm_channels.setInvertedAppearance(False)
        self.horizontalSlider_fm_channels.setInvertedControls(False)
        self.horizontalSlider_fm_channels.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_fm_channels.setObjectName("horizontalSlider_fm_channels")
        
        #music box  music tab fm tab next channel button fm 
        self.next_btn_fm = QtWidgets.QPushButton(self.fm)
        self.next_btn_fm.setGeometry(QtCore.QRect(410, 210, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.next_btn_fm.setFont(font)
        self.next_btn_fm.setStyleSheet("")
        #self.next_btn_fm.setText("")
        #self.next_btn_fm.setText("border-radius:50%;background-color:None;border:2px solid white;color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logos/forward_music_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn_fm.setIcon(icon)
        self.next_btn_fm.setIconSize(QtCore.QSize(100, 120))
        self.next_btn_fm.setObjectName("next_btn_fm")
        
        #music box  music tab fm tab pprevious channel button fm
        self.previous_btn_fm = QtWidgets.QPushButton(self.fm)
        self.previous_btn_fm.setGeometry(QtCore.QRect(80, 210, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.previous_btn_fm.setFont(font)
        self.previous_btn_fm.setStyleSheet("")
        self.previous_btn_fm.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/logos/backward__music_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_btn_fm.setIcon(icon1)
        self.previous_btn_fm.setIconSize(QtCore.QSize(100, 120))
        self.previous_btn_fm.setObjectName("previous_btn_fm")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo/logos/fm_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        #music box  music tab aux tab 
        self.music_box_window.addTab(self.fm, icon2, "")
        self.AUX_USB = QtWidgets.QWidget()
        self.AUX_USB.setObjectName("AUX_USB")
        #music box  music tab aux tab fm_aux_player_song_title_label
        self.fm_aux_player_song_title_label = QtWidgets.QLabel(self.AUX_USB)
        self.fm_aux_player_song_title_label.setGeometry(QtCore.QRect(180, 60, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.fm_aux_player_song_title_label.setFont(font)
        self.fm_aux_player_song_title_label.setStyleSheet("background:none;color:white;border:none;")
        self.fm_aux_player_song_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fm_aux_player_song_title_label.setObjectName("fm_aux_player_song_title_label")
        #music box  music tab aux tab fm_aux_player_song_artist
        self.fm_aux_player_song_artist_ = QtWidgets.QLabel(self.AUX_USB)
        self.fm_aux_player_song_artist_.setGeometry(QtCore.QRect(210, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.fm_aux_player_song_artist_.setFont(font)
        self.fm_aux_player_song_artist_.setStyleSheet("background:none;color:white;border:none;")
        self.fm_aux_player_song_artist_.setAlignment(QtCore.Qt.AlignCenter)
        self.fm_aux_player_song_artist_.setObjectName("fm_aux_player_song_artist_")
        
        #music box  music tab aux tab fm_aux_player_song_album_label

        self.fm_aux_player_song_album_label = QtWidgets.QLabel(self.AUX_USB)
        self.fm_aux_player_song_album_label.setGeometry(QtCore.QRect(210, 140, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.fm_aux_player_song_album_label.setFont(font)
        self.fm_aux_player_song_album_label.setStyleSheet("background:none;color:white;border:none;")
        self.fm_aux_player_song_album_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fm_aux_player_song_album_label.setObjectName("fm_aux_player_song_album_label")
        
        #music box  music tab aux tab bt_song_next_btn_2
        self.bt_song_next_btn_2 = QtWidgets.QPushButton(self.AUX_USB)
        self.bt_song_next_btn_2.setGeometry(QtCore.QRect(490, 220, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bt_song_next_btn_2.setFont(font)
        self.bt_song_next_btn_2.setStyleSheet("")
        self.bt_song_next_btn_2.setText("")
        self.bt_song_next_btn_2.setIcon(icon)
        self.bt_song_next_btn_2.setIconSize(QtCore.QSize(100, 120))
        self.bt_song_next_btn_2.setObjectName("bt_song_next_btn_2")
        
        
        #music box  music tab aux tab bt_play_pause_btn_2
        self.bt_play_pause_btn_2 = QtWidgets.QPushButton(self.AUX_USB)
        self.bt_play_pause_btn_2.setGeometry(QtCore.QRect(270, 220, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bt_play_pause_btn_2.setFont(font)
        self.bt_play_pause_btn_2.setStyleSheet("")
        self.bt_play_pause_btn_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/logo/logos/play_music_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_play_pause_btn_2.setIcon(icon3)
        self.bt_play_pause_btn_2.setIconSize(QtCore.QSize(100, 120))
        self.bt_play_pause_btn_2.setObjectName("bt_play_pause_btn_2")
        
        #music box  music tab aux tab bt_previous_btn_2
        self.bt_previous_btn_2 = QtWidgets.QPushButton(self.AUX_USB)
        self.bt_previous_btn_2.setGeometry(QtCore.QRect(70, 220, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bt_previous_btn_2.setFont(font)
        self.bt_previous_btn_2.setStyleSheet("")
        self.bt_previous_btn_2.setText("")
        self.bt_previous_btn_2.setIcon(icon1)
        self.bt_previous_btn_2.setIconSize(QtCore.QSize(100, 120))
        self.bt_previous_btn_2.setObjectName("bt_previous_btn_2")
        
        #music box  music tab aux tab tool button 
        self.toolButton = QtWidgets.QToolButton(self.AUX_USB)
        self.toolButton.setGeometry(QtCore.QRect(10, 20, 101, 61))
        self.toolButton.setStyleSheet("color:white;border:2px solid white;border-radius:30px;")
        self.toolButton.setObjectName("toolButton")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/logo/logos/usb_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        #music box  music tab bt tab
        self.music_box_window.addTab(self.AUX_USB, icon4, "")
        self.BT = QtWidgets.QWidget()
        self.BT.setObjectName("BT")
        #music box  music tab bt tab title label
        #BLE CODE
        
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()
        self.obj = self.bus.get_object('org.bluez', "/")
        self.mgr = dbus.Interface(self.obj, 'org.freedesktop.DBus.ObjectManager')
        ##
        self.bt_player_connect_label = QtWidgets.QLabel(self.BT)
        self.bt_player_connect_label.setGeometry(QtCore.QRect(100, 30, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.bt_player_connect_label.setFont(font)
        self.bt_player_connect_label.setStyleSheet("background:none;color:white;border:none;")
        self.bt_player_connect_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_player_connect_label.setObjectName("bt_player_song_title_label")
        
        self.bt_player_connect_btn = QtWidgets.QPushButton(self.BT)
        self.bt_player_connect_btn.setGeometry(QtCore.QRect(30, 30, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bt_player_connect_btn.setFont(font)
        self.bt_player_connect_btn.setStyleSheet("")
        self.bt_player_connect_btn.setText("")
        self.bt_player_connect_btn.setIcon(icon)
        self.bt_player_connect_btn.setIconSize(QtCore.QSize(100, 120))
        self.bt_player_connect_btn.setObjectName("bt_song_next_btn")
        self.bt_player_connect_btn.clicked.connect(self.bluetooth)
        ##
        self.bt_player_song_title_label = QtWidgets.QLabel(self.BT)
        self.bt_player_song_title_label.setGeometry(QtCore.QRect(160, 60, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.bt_player_song_title_label.setFont(font)
        self.bt_player_song_title_label.setStyleSheet("background:none;color:white;border:none;")
        self.bt_player_song_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_player_song_title_label.setObjectName("bt_player_song_title_label")
        
        
        
        #music box  music tab bt tab artist label 
        self.bt_player_song_artist_label = QtWidgets.QLabel(self.BT)
        self.bt_player_song_artist_label.setGeometry(QtCore.QRect(190, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bt_player_song_artist_label.setFont(font)
        self.bt_player_song_artist_label.setStyleSheet("background:none;color:white;border:none;")
        self.bt_player_song_artist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_player_song_artist_label.setObjectName("bt_player_song_artist_label")
        
        #music box  music tab bt tab album label
        self.bt_palyer_song_album_label = QtWidgets.QLabel(self.BT)
        self.bt_palyer_song_album_label.setGeometry(QtCore.QRect(190, 140, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bt_palyer_song_album_label.setFont(font)
        self.bt_palyer_song_album_label.setStyleSheet("background:none;color:white;border:none;")
        self.bt_palyer_song_album_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_palyer_song_album_label.setObjectName("bt_palyer_song_album_label")
        #music box  music tab bt tab bt next song button
        self.bt_song_next_btn = QtWidgets.QPushButton(self.BT)
        self.bt_song_next_btn.setGeometry(QtCore.QRect(470, 200, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bt_song_next_btn.setFont(font)
        self.bt_song_next_btn.setStyleSheet("")
        self.bt_song_next_btn.setText("")
        self.bt_song_next_btn.setIcon(icon)
        self.bt_song_next_btn.setIconSize(QtCore.QSize(100, 120))
        self.bt_song_next_btn.setObjectName("bt_song_next_btn")
        self.bt_song_next_btn.clicked.connect(self.next_song)
        #music box  music tab bt tab bt song play pause button
        self.bt_play_pause_btn = QtWidgets.QPushButton(self.BT)
        self.bt_play_pause_btn.setGeometry(QtCore.QRect(260, 200, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bt_play_pause_btn.setFont(font)
        self.bt_play_pause_btn.setStyleSheet("")
        self.bt_play_pause_btn.setText("")
        self.bt_play_pause_btn.setIcon(icon3)
        self.bt_play_pause_btn.setIconSize(QtCore.QSize(100, 120))
        self.bt_play_pause_btn.setObjectName("bt_play_pause_btn")
        self.bt_play_pause_btn.clicked.connect(self.play_pause)
        #music box  music tab bt tab previous song button
        self.bt_previous_btn = QtWidgets.QPushButton(self.BT)
        self.bt_previous_btn.setGeometry(QtCore.QRect(90, 200, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bt_previous_btn.setFont(font)
        self.bt_previous_btn.setStyleSheet("")
        self.bt_previous_btn.setText("")
        self.bt_previous_btn.setIcon(icon1)
        self.bt_previous_btn.setIconSize(QtCore.QSize(100, 120))
        self.bt_previous_btn.setObjectName("bt_previous_btn")
        self.bt_previous_btn.clicked.connect(self.previous_song)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/logo/logos/bt_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.music_box_window.addTab(self.BT, icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/logo/logos/music_final.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #camara TAB 2
        self.main_tab.addTab(self.music_tab, icon6, "")
        self.camara_tab = QtWidgets.QWidget()
        self.camara_tab.setObjectName("camara_tab")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/logo/logos/open_camara_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #gear camara
        self.gear_camara = QtWidgets.QPushButton(self.camara_tab)
        self.gear_camara.setGeometry(QtCore.QRect(30, 20, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.gear_camara.setFont(font)
        self.gear_camara.setStyleSheet("border:2px solid white;color:white;")
        self.gear_camara.setObjectName("person1_button_wakitaki")
        self.gear_camara.clicked.connect(self.open_gear_camara)
        
        ##camara label outpuy

        self.camara_output_label = QtWidgets.QLabel(self.camara_tab)
        self.camara_output_label.setGeometry(QtCore.QRect(30,100 , 661,320))
        self.camara_output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camara_output_label.setObjectName("label")
        #self.camara_output_label.setStyleSheet("color:white;")
        
        ######
      
        ########
        #calling TAB 3

    
        self.main_tab.addTab(self.camara_tab, icon7, "")
        self.calling_tab = QtWidgets.QWidget()
        self.calling_tab.setObjectName("calling_tab")
        
        #person calling 1 btn
        self.person1_button_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person1_button_wakitaki.setGeometry(QtCore.QRect(30, 20, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person1_button_wakitaki.setFont(font)
        self.person1_button_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        self.person1_button_wakitaki.setObjectName("person1_button_wakitaki")
        self.person1_button_wakitaki.clicked.connect(self.calling1)
        #person calling 2 btn
        self.person2_button_2_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person2_button_2_wakitaki.setGeometry(QtCore.QRect(30, 110, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person2_button_2_wakitaki.setFont(font)
        self.person2_button_2_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        self.person2_button_2_wakitaki.setObjectName("person2_button_2_wakitaki")
        self.person2_button_2_wakitaki.clicked.connect(self.calling2)
        
        #person calling 3 btn
        self.person3_button_3_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person3_button_3_wakitaki.setGeometry(QtCore.QRect(30, 200, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person3_button_3_wakitaki.setFont(font)
        self.person3_button_3_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        self.person3_button_3_wakitaki.setObjectName("person3_button_3_wakitaki")
        self.person3_button_3_wakitaki.clicked.connect(self.calling3)
        
        #person calling 4 btn
        self.person4_button_4_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person4_button_4_wakitaki.setGeometry(QtCore.QRect(30, 290, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person4_button_4_wakitaki.setFont(font)
        self.person4_button_4_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/logo/logos/police-badge_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.person4_button_4_wakitaki.setIcon(icon8)
        self.person4_button_4_wakitaki.setIconSize(QtCore.QSize(60, 40))
        self.person4_button_4_wakitaki.setObjectName("person4_button_4_wakitaki")
        self.person4_button_4_wakitaki.clicked.connect(self.calling4)
        
        #person calling 5 btn
        self.person5_button_5_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person5_button_5_wakitaki.setGeometry(QtCore.QRect(30, 380, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person5_button_5_wakitaki.setFont(font)
        self.person5_button_5_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/logo/logos/ambulance_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.person5_button_5_wakitaki.setIcon(icon9)
        self.person5_button_5_wakitaki.setIconSize(QtCore.QSize(80, 60))
        self.person5_button_5_wakitaki.setObjectName("person5_button_5_wakitaki")
        self.person5_button_5_wakitaki.clicked.connect(self.calling5)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/logo/logos/phone11.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #stats TAB 3
        self.main_tab.addTab(self.calling_tab, icon10, "")
        self.setting_tab = QtWidgets.QWidget()
        self.setting_tab.setObjectName("setting_tab")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/logo/logos/status_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        
        #GAte Code
        GPIO.setup(self.gate, GPIO.OUT)
        self.person_name = QtWidgets.QLabel(self.setting_tab)
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
        self.gate_open_button = QtWidgets.QPushButton(self.setting_tab)
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
        self.gate_close_button = QtWidgets.QPushButton(self.setting_tab)
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
        
        #setting TAB 3
        self.main_tab.addTab(self.setting_tab, icon11, "")
        self.stats_tab = QtWidgets.QWidget()
        self.stats_tab.setObjectName("stats_tab")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/logo/logos/settings_player.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_tab.addTab(self.stats_tab, icon12, "")
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_tab.setCurrentIndex(0)
        self.music_box_window.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #BLE  Code before connectivity
        
        for path, ifaces in self.mgr.GetManagedObjects().items():
            if 'org.bluez.MediaPlayer1' in ifaces:
                self.player_iface = dbus.Interface(
                        self.bus.get_object('org.bluez', path),
                        'org.bluez.MediaPlayer1')
                self.bt_player_connect_label.setText("Connected")
                
            elif 'org.bluez.MediaTransport1' in ifaces:
                self.transport_prop_iface = dbus.Interface(
                        self.bus.get_object('org.bluez', path),
                        'org.freedesktop.DBus.Properties')
        time.sleep(1)
        self.bus.add_signal_receiver(
                self.on_property_changed,
                bus_name='org.bluez',
                signal_name='PropertiesChanged',
                dbus_interface='org.freedesktop.DBus.Properties')

         
# ble functions
    def bluetooth (self):
        #BLE  Code
        
        for path, ifaces in self.mgr.GetManagedObjects().items():
            if 'org.bluez.MediaPlayer1' in ifaces:
                self.player_iface = dbus.Interface(
                        self.bus.get_object('org.bluez', path),
                        'org.bluez.MediaPlayer1')
                self.bt_player_connect_label.setText("Connected")
                
            elif 'org.bluez.MediaTransport1' in ifaces:
                self.transport_prop_iface = dbus.Interface(
                        self.bus.get_object('org.bluez', path),
                        'org.freedesktop.DBus.Properties')
        time.sleep(1)
        self.bus.add_signal_receiver(
                self.on_property_changed,
                bus_name='org.bluez',
                signal_name='PropertiesChanged',
                dbus_interface='org.freedesktop.DBus.Properties')
    
    def on_property_changed(self,interface, changed, invalidated):
        if interface != 'org.bluez.MediaPlayer1':
            return
        for prop, value in changed.items():
            if prop == 'Status':
                print('Playback Status: {}'.format(value))
                self.status = value
                if self.status == "playing":
                    self.bt_play_pause_btn.setIcon(QIcon('/home/pi/Desktop/demo/logos/music_3.svg'))
                elif self.status == "paused":
                    self.bt_play_pause_btn.setIcon(QIcon('/home/pi/Desktop/demo/logos/music_4.svg'))
            elif prop == 'Track':
                self.track = value
                for key in ('Title', 'Artist', 'Album'):
                    print('   {}: {}'.format(key, value.get(key, '')))                    
                    self.bt_player_song_title_label.setText(value.get("Title"))
                    self.bt_player_song_artist_label.setText(value.get("Album"))
                    self.bt_palyer_song_album_label.setText(value.get("Artist"))


    #volume slider value

    def Volume_value(self,value):
        pass
    #     return valueof#ask once pooja about the range and of volume
    
    def play_pause(self):
        try:
            if self.status == "playing":
                self.player_iface.Pause()        
                self.status = "paused"
            elif self.status == "paused":
                self.player_iface.Play()
                self.status = "playing"
        except:
            print("play exceptiom")
            

        
       #Ble.play_pause_read() 
    
    def next_song(self):
        try:
            
            self.player_iface.Next()
        except:
            print("next exc")

        
    
    def previous_song(self):
        try:            
            self.player_iface.Previous()
        except:
            print("prev excep")
    
                        
    def calling1(self):
        try:
            self.player_iface.Pause()
        except:
            print("no music")
        try:
            
            self.Window=QtWidgets.QMainWindow()
            self.ui=Call_cut()
            self.ui.setupUi(self.Window)
            self.Window.show()
            self.port.write(b'AT+SNFS=0\r')
            rcv = self.port.read(10)
            print(rcv)
            #time.sleep(1)
            self.port.write(b'ATD9617241556;\r')#AT Command write
            #time.sleep(1)               
            rcv = self.port.read(50)#gsm Value reasding
            print(rcv.decode())
            #time.sleep(1)
        except:
            print("module disconnected")

    def calling2(self):
        try:
            self.player_iface.Pause()
        except:
            print("no music")
        try:
            
            self.Window=QtWidgets.QMainWindow()
            self.ui=Call_cut()
            self.ui.setupUi(self.Window)
            self.Window.show()
            self.port.write(b'AT+SNFS=0\r')
            rcv = self.port.read(10)
            print(rcv)
            #time.sleep(1)
            self.port.write(b'ATD9617241556;\r')#AT Command write
            #time.sleep(1)               
            rcv = self.port.read(50)#gsm Value reasding
            print(rcv.decode())
            #time.sleep(1)
        except:
            print("module disconnected")
      
    def calling3(self):
        try:
            self.player_iface.Pause()
        except:
            print("no music")
        try:
            
            self.Window=QtWidgets.QMainWindow()
            self.ui=Call_cut()
            self.ui.setupUi(self.Window)
            self.Window.show()
            self.port.write(b'AT+SNFS=0\r')
            rcv = self.port.read(10)
            print(rcv)
            #time.sleep(1)
            self.port.write(b'ATD7049912353;\r')#AT Command write
            #time.sleep(1)               
            rcv = self.port.read(50)#gsm Value reasding
            print(rcv.decode())
            #time.sleep(1)
        except:
            print("module disconnected")  
        
        
       
        
    def calling4(self):
        try:
            self.player_iface.Pause()
        except:
            print("no music")
         
        try:
            
            self.Window=QtWidgets.QMainWindow()
            self.ui=Call_cut()
            self.ui.setupUi(self.Window)
            self.Window.show()
            
            self.port.write(b'AT+SNFS=0\r')
            rcv = self.port.read(10)
            print(rcv)
            #time.sleep(1)
            self.port.write(b'ATD9617241556;\r')#AT Command write
            #time.sleep(1)               
            rcv = self.port.read(50)#gsm Value reasding
            print(rcv.decode())
            #time.sleep(1)
        except:
            print("module disconnected")
        
    def calling5(self):
        try:
            self.player_iface.Pause()
        except:
            print("no music")      
        try:
            
            self.Window=QtWidgets.QMainWindow()
            self.ui=Call_cut()
            self.ui.setupUi(self.Window)
            self.Window.show()
            self.port.write(b'AT+SNFS=0\r')
            rcv = self.port.read(10)
            print(rcv)
            #time.sleep(1)
            self.port.write(b'ATD9407386981;\r')#AT Command write
            #time.sleep(1)               
            rcv = self.port.read(50)#gsm Value reasding
            print(rcv.decode())
            #time.sleep(1)
        except:
            print("module disconnected")
        

    def open_gear_camara(self):

        
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)
    
    def update_frame(self):
        ret,self.image=self.capture.read()
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image,1)
    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outImage=outImage.rgbSwapped()
        
        if window==1:
            self.camara_output_label.setPixmap(QPixmap.fromImage(outImage))
            self.camara_output_label.setScaledContents(True)
        


    def changeTime(self):
        a=self.ds3231.read_datetime()
        #print(type(a))
        time.sleep(10.0)
        self.rtc_time_label.setText(str(a))
    
    def callreceive(self):
        a=0
        while True:
            try:
                
                #self.port.write(b'AT\r')
                rcv = self.port.read(30)
                rcv =rcv.decode()
                time.sleep(2)
                while rcv == " ":
                    print("..*",endl="")
                    #pass
                print(rcv)
                time.sleep(1)
                if 'RING' in rcv:
                    
                    print("ringing  ")
                    
                    try:
                        self.player_iface.Pause()
                    except:
                        print("no music")  
                    self.port.write(b'ATA\r')
                    rcv = self.port.read(10)
                if '+CIEV: "CALL",0' in rcv:
                    
                    print("ringing  ")
    
                    self.port.write(b'ATH\r')
                    rcv = self.port.read(10)

            except:
                pass
                #print("..")       
        
  ##Gate
    def close(self):
        try:
            print("clicked")
            GPIO.output(self.gate, GPIO.LOW)
            self.person_name.setText("Closed")
        #print(rcv.decode())
        except:
            print("..cuttpick")
        
       
    def open(self):
        try:
            print("clicked")
            GPIO.output(self.gate, GPIO.HIGH)
            self.person_name.setText("Open")
        #print(rcv.decode())
        except:
            print("..cuttpick")
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fm_label.setText(_translate("MainWindow", "FM"))
        self.fm_channel_label.setText(_translate("MainWindow", "99.9"))
        self.fm_aux_player_song_title_label.setText(_translate("MainWindow", "TITLE LOADING..."))
        self.fm_aux_player_song_artist_.setText(_translate("MainWindow", "ARTIST LOADING ..."))
        self.fm_aux_player_song_album_label.setText(_translate("MainWindow", "ALBUM LOADING ..."))
        self.toolButton.setText(_translate("MainWindow", "...open"))
        self.bt_player_song_title_label.setText(_translate("MainWindow", "TITLE LOADING..."))
        self.bt_player_song_artist_label.setText(_translate("MainWindow", "ARTIST LOADING ..."))
        self.bt_palyer_song_album_label.setText(_translate("MainWindow", "ALBUM LOADING ..."))
        
        ##
        self.bt_player_connect_label .setText(_translate("MainWindow", "Not Connected"))
        #bt_player_connect_btn
        ##
        self.person1_button_wakitaki.setText(_translate("MainWindow", "Manager"))
        self.person2_button_2_wakitaki.setText(_translate("MainWindow", "Head Office Pune"))
        self.person3_button_3_wakitaki.setText(_translate("MainWindow", "Head Office Mumbai"))
        self.person4_button_4_wakitaki.setText(_translate("MainWindow", "Police"))
        self.person5_button_5_wakitaki.setText(_translate("MainWindow", "Ambulance"))
        ##bt_player_connect_label 
        #camara display label
        self.camara_output_label.setText(_translate("MainWindow", "OPEN"))
        #rtc
        #self.rtc_time_label.setText(_translate("MainWindow", "Time"))
        ##GAtwe
        self.person_name.setText(_translate("gateopen", "Gate Closed"))
        self.gate_open_button.setText(_translate("gateopen", ""))
        self.gate_close_button.setText(_translate("gateopen", ""))        
        #p3 = Process(target=self.changeTime)
        #p3.start()
        #p3.join()
        
def uiWindow():
    import icon_rc
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #MainWindow.showFullScreen()
    sys.exit(app.exec_())
    
    
 
if __name__ == "__main__":
    a =Ui_MainWindow()
    p1 = Process(target=uiWindow)
    p2 = Process(target=a.callreceive)
    #p3 = Process(target=a.changeTime)
    p1.start()
    p2.start()
    #p3.start()
    p1.join()
    p2.join()#+CIEV: "CALL",0\r\n\r\nNO CARRIER\r\n'
    #p3.join()
    
    

