


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demo1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import os
import random,time
from pygame import mixer
from mutagen.mp3 import MP3

#initialize the basis things
mixer.init()#mixer inisiated
musiclist=[]#song empty list
##mute = False#mute is false
play = False#play is false
current_song = None#current song is none
count = 0#count is 0
songLength = 0#song length is 0
index = 0#index is 0



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960,540)
        MainWindow.setMinimumSize(QtCore.QSize(960,540))     
    
        MainWindow.setMaximumSize(QtCore.QSize(960,540))
        MainWindow.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tab.setGeometry(QtCore.QRect(0, 30, 960, 540))
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
        self.main_tab.setIconSize(QtCore.QSize(100, 60))
        self.main_tab.setObjectName("main_tab")
        self.music_tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.music_tab.setFont(font)
        self.music_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.music_tab.setAutoFillBackground(False)
        self.music_tab.setObjectName("music_tab")
        self.music_box_window = QtWidgets.QTabWidget(self.music_tab)
        ###Ch
        self.music_box_window.setGeometry(QtCore.QRect(0, 0, 870, 540))
        self.music_box_window.setIconSize(QtCore.QSize(80, 50))
        self.music_box_window.setObjectName("music_box_window")
        self.fm = QtWidgets.QWidget()
        self.fm.setObjectName("fm")
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
        self.next_btn_fm = QtWidgets.QPushButton(self.fm)
        self.next_btn_fm.setGeometry(QtCore.QRect(410, 210, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.next_btn_fm.setFont(font)
        self.next_btn_fm.setStyleSheet("")
        self.next_btn_fm.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logos/forward_music_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn_fm.setIcon(icon)
        self.next_btn_fm.setIconSize(QtCore.QSize(100, 120))
        self.next_btn_fm.setObjectName("next_btn_fm")
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
        self.music_box_window.addTab(self.fm, icon2, "")

        ####AUX
        self.AUX_USB = QtWidgets.QWidget()
        self.AUX_USB.setObjectName("AUX_USB")
        self.label = QtWidgets.QLabel(self.AUX_USB)
        self.label.setGeometry(QtCore.QRect(210, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background:none;color:white;border:none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nextButton = QtWidgets.QPushButton(self.AUX_USB)
        self.nextButton.setGeometry(QtCore.QRect(490, 220, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("")
        self.nextButton.setText("")
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(100, 120))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.nextsong)
        
        self.playButton = QtWidgets.QPushButton(self.AUX_USB)
        self.playButton.setGeometry(QtCore.QRect(270, 220, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("")
        self.playButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/logo/logos/play_music_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon3)
        self.playButton.setIconSize(QtCore.QSize(100, 120))
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.playsong)#function for playing song`

        self.previousButton = QtWidgets.QPushButton(self.AUX_USB)
        self.previousButton.setGeometry(QtCore.QRect(70, 220, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.previousButton.setFont(font)
        self.previousButton.setStyleSheet("")
        self.previousButton.setText("")
        self.previousButton.setIcon(icon1)
        self.previousButton.setIconSize(QtCore.QSize(100, 120))
        self.previousButton.setObjectName("previousButton")
        self.previousButton.clicked.connect(self.previoussong)
        
        
        self.toolButton = QtWidgets.QToolButton(self.AUX_USB)
        self.toolButton.setGeometry(QtCore.QRect(10, 20, 101, 61))
        self.toolButton.setStyleSheet("color:white;border:2px solid white;border-radius:30px;")
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.addSound)#function fo adding song
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/logo/logos/usb_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_box_window.addTab(self.AUX_USB, icon4, "")
        #list view1
        
        self.playlist = QtWidgets.QListWidget(self.AUX_USB)
        self.playlist.setObjectName("playlist")
        self.playlist.setGeometry(QtCore.QRect(680, 2, 182,400))
        font = QtGui.QFont()
        font.setPointSize(12)
        #font.setWeight(10)
        font.setStrikeOut(False)
        self.playlist.setFont(font)
        self.playlist.setStyleSheet("color:white;")
        self.playlist.doubleClicked.connect(self.playsong_1)# dobble click song play

        
        ##BLE
        self.BT = QtWidgets.QWidget()
        self.BT.setObjectName("BT")
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/logo/logos/bt_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_box_window.addTab(self.BT, icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/logo/logos/music_final.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_tab.addTab(self.music_tab, icon6, "")
        self.camara_tab = QtWidgets.QWidget()
        self.camara_tab.setObjectName("camara_tab")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/logo/logos/open_camara_tab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_tab.addTab(self.camara_tab, icon7, "")
        self.calling_tab = QtWidgets.QWidget()
        self.calling_tab.setObjectName("calling_tab")
        self.person1_button_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person1_button_wakitaki.setGeometry(QtCore.QRect(30, 20, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person1_button_wakitaki.setFont(font)
        self.person1_button_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        self.person1_button_wakitaki.setObjectName("person1_button_wakitaki")
        self.person2_button_2_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person2_button_2_wakitaki.setGeometry(QtCore.QRect(30, 110, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person2_button_2_wakitaki.setFont(font)
        self.person2_button_2_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        self.person2_button_2_wakitaki.setObjectName("person2_button_2_wakitaki")
        self.person3_button_3_wakitaki = QtWidgets.QPushButton(self.calling_tab)
        self.person3_button_3_wakitaki.setGeometry(QtCore.QRect(30, 200, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.person3_button_3_wakitaki.setFont(font)
        self.person3_button_3_wakitaki.setStyleSheet("border:2px solid white;color:white;")
        self.person3_button_3_wakitaki.setObjectName("person3_button_3_wakitaki")
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/logo/logos/phone11.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_tab.addTab(self.calling_tab, icon10, "")
        self.setting_tab = QtWidgets.QWidget()
        self.setting_tab.setObjectName("setting_tab")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/logo/logos/status_2_player.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_tab.addTab(self.setting_tab, icon11, "")
        self.stats_tab = QtWidgets.QWidget()
        self.stats_tab.setObjectName("stats_tab")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/logo/logos/settings_player.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_tab.addTab(self.stats_tab, icon12, "")
        MainWindow.setCentralWidget(self.centralwidget)
        ####
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateprogressbar)

        ###
        self.retranslateUi(MainWindow)
        self.main_tab.setCurrentIndex(0)
        self.music_box_window.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#####
    def addSound(self):
        # 
        # directory=QFileDialog.getOpenFileName(MainWindow,"Add Sound","","Sound Filed(*.mp3 *.ogg *.wav)")        
        # filename = os.path.basename(directory[0])
        # # print(filename)
        # musiclist.append(directory[0])
        # self.playlist.addItem(filename)
        # print(musiclist)
        dir_path = os.path.dirname("E:\music")
  
        for root, dirs, files in os.walk(dir_path):
            for file in files: 
  
        # change the extension from '.mp3' to 
        # the one of your choice.
                if file.endswith('.mp3'):
                    directory=os.path.join(root, file)
                    musiclist.append(directory)
                    self.playlist.addItem(file)
                    #print(musiclist)
                    #print(directory)

    
    def playsong_1(self):
        global play,current_song,songLength,count,index
        count = 0
        index = self.playlist.currentRow()      
        try:
            mixer.music.load(str(musiclist[index]))
            mixer.music.play()
            play =True
            current_song = index
            #title print
            print("when clicked")
            song_name=musiclist[index]
            song_name=song_name.split("\\")
            song_name=song_name[-1]
            song_name=song_name.split(".")
            print(song_name[0])
            self.label.setText(song_name[0])
            #####
            
            self.timer.start()
            sound = MP3(str(musiclist[index]))
            songLength = sound.info.length
            songLength =round(songLength)
            #print(songLength)
            min,sec=divmod(songLength,60)
            #print(min,sec)
            
        except:
            pass                
    
###########################################
    def playsong(self):
        global play,current_song,songLength,count,index
        index = self.playlist.currentRow()
        
        if play == False:
            if current_song == index:
                
                play = True
                self.timer.start()
                mixer.music.unpause()

            else:   
                try:
                    count = 0
                    mixer.music.load(musiclist[index])
                    ####
                    print("when clicked")
                    song_name=musiclist[index]
                    song_name=song_name.split("\\")
                    song_name=song_name[-1]
                    song_name=song_name.split(".")
                    print(song_name[0])
                    self.label.setText(song_name[0])
                    ####
                    mixer.music.play()
                    current_song = index
                    #print(current_song)
                    self.timer.start()
                    sound = MP3(str(musiclist[index]))
                    songLength = sound.info.length
                    songLength =round(songLength)
                    #print(songLength)
                    min,sec=divmod(songLength,60)

                except:
                    pass 
            play = True        
        elif play ==True:
            play = False
            self.timer.stop()
            mixer.music.pause()
############################################
    def previoussong(self):
        
        global play,current_song,songLength,count,index
        if index ==0:
            index = len(musiclist)-1
        else:
            index-=1    
        try:
            count = 0
            mixer.music.load(musiclist[index])
            mixer.music.play()
            current_song = index
            self.timer.start()
            sound = MP3(str(musiclist[index]))
            songLength = sound.info.length
            songLength =round(songLength)
            #print(songLength)
            min,sec=divmod(songLength,60)
            ####
            print("when clicked")
            song_name=musiclist[index]
            song_name=song_name.split("\\")
            song_name=song_name[-1]
            song_name=song_name.split(".")
            print(song_name[0])
            self.label.setText(song_name[0])
            ####            
        except:
            pass
############################################
    def nextsong(self):
        #print("next song")
        global play,current_song,songLength,count,index
        if index ==len(musiclist)-1:
            index = 0
        else:
            index+=1    
        try:
            count = 0
            mixer.music.load(musiclist[index])
            mixer.music.play()
            current_song = index
            self.timer.start()
            sound = MP3(str(musiclist[index]))
            songLength = sound.info.length
            songLength =round(songLength)
            #print(songLength)
            min,sec=divmod(songLength,60)
            ####
            print("when clicked")
            song_name=musiclist[index]
            song_name=song_name.split("\\")
            song_name=song_name[-1]
            song_name=song_name.split(".")
            print(song_name[0])
            self.label.setText(song_name[0])
            ####
    
        except:
            pass
############################################
    def updateprogressbar(self):
        global count,songLength
        count +=1
       
        if count == songLength:
            self.timer.stop()
            self.nextsong()                     
                 
#####
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fm_label.setText(_translate("MainWindow", "FM"))
        self.fm_channel_label.setText(_translate("MainWindow", "99.9"))
        self.label.setText(_translate("MainWindow", "ARTIST LOADING ..."))
        self.toolButton.setText(_translate("MainWindow", "...open"))
        self.bt_player_song_title_label.setText(_translate("MainWindow", "TITLE LOADING..."))
        self.bt_player_song_artist_label.setText(_translate("MainWindow", "ARTIST LOADING ..."))
        self.bt_palyer_song_album_label.setText(_translate("MainWindow", "ALBUM LOADING ..."))
        self.person1_button_wakitaki.setText(_translate("MainWindow", "Manager"))
        self.person2_button_2_wakitaki.setText(_translate("MainWindow", "Head Office Pune"))
        self.person3_button_3_wakitaki.setText(_translate("MainWindow", "Head Office Mumbai"))
        self.person4_button_4_wakitaki.setText(_translate("MainWindow", "Police"))
        self.person5_button_5_wakitaki.setText(_translate("MainWindow", "Ambulance"))



if __name__ == "__main__":
    import icon_rc
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
