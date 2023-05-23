from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
    QMessageBox, QHBoxLayout, QVBoxLayout, QSlider, QListWidget,
    QPushButton, QLabel, QComboBox, QFileDialog, QTabWidget, QApplication)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent,QAudioFormat, QAudioOutput
import os, time
import configparser
from pydub import AudioSegment

import sys
import random
from MyQLabel import MyQLabel
import requests
import json


class MP3Player(QWidget):
    def __init__(self):
        super().__init__()

        self.startTimeLabel = QLabel('00:00')
        self.endTimeLabel = QLabel('00:00')
        self.slider = QSlider(Qt.Horizontal, self)
        self.PlayModeBtn = QPushButton(self)
        self.playBtn = QPushButton(self)
        self.prevBtn = QPushButton(self)
        self.nextBtn = QPushButton(self)
        self.openBtn = QPushButton(self)
        self.musicList = QListWidget()
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.songs_list = []
        self.cur_playing_song = ''
        self.is_pause = True
        self.player = QMediaPlayer()
        self.is_switching = False
        self.playMode = 0
        self.settingfilename = 'config.ini'

        self.textLable = MyQLabel()
        self.textLable.setText("点击体验个性化一言推送")
        self.textLable.connect_customized_slot(self.yiyan)
        font = QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        self.textLable.setFont(font)
        self.textLable.setAlignment(Qt.AlignCenter)
        

        self.tab_widget = QTabWidget(self)
        # 第一个Widget
        widget1 = QWidget()
        layout1 = QVBoxLayout(widget1)
        layout1.addWidget(self.musicList)
        # 创建第二个Widget
        widget2 = QWidget()
        layout2 = QVBoxLayout(widget2)
        h_layout = QHBoxLayout()

        # 创建均衡器滑动条和标签
        self.slider_group1,self.slider_label1 = self.create_slider_group("Slider 1:")
        self.slider_group2,self.slider_label2 = self.create_slider_group("Slider 2:")
        self.slider_group3,self.slider_label3 = self.create_slider_group("Slider 3:")

        h_layout.addLayout(self.slider_group1)
        h_layout.addLayout(self.slider_group2)
        h_layout.addLayout(self.slider_group3)

        layout2.addLayout(h_layout)



        # 将两个Widget添加到TabWidget中
        self.tab_widget.addTab(widget1, "音乐列表")
        self.tab_widget.addTab(widget2, "均衡器")

        self.playBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/play.png)}")
        self.playBtn.setFixedSize(48, 48)
        self.nextBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/47最后一页、末页、下一首.png)}")
        self.nextBtn.setFixedSize(48, 48)
        self.prevBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/46第一页、首页、上一首.png)}")
        self.prevBtn.setFixedSize(48, 48)
        self.openBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/下载.png)}")
        self.openBtn.setFixedSize(36, 36)
        self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/顺序播放.png)}")
        self.PlayModeBtn.setFixedSize(36, 36)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.playByMode)

        self.hBoxSlider = QHBoxLayout()
        self.hBoxSlider.addWidget(self.startTimeLabel)
        self.hBoxSlider.addWidget(self.slider)
        self.hBoxSlider.addWidget(self.endTimeLabel)

        self.hBoxButton = QHBoxLayout()
        self.hBoxButton.addWidget(self.PlayModeBtn)
        self.hBoxButton.addStretch(1)
        self.hBoxButton.addWidget(self.prevBtn)
        self.hBoxButton.addWidget(self.playBtn)
        self.hBoxButton.addWidget(self.nextBtn)
        self.hBoxButton.addStretch(1)
        self.hBoxButton.addWidget(self.openBtn)

        self.vBoxControl = QVBoxLayout()
        self.vBoxControl.addLayout(self.hBoxSlider)
        self.vBoxControl.addLayout(self.hBoxButton)

        self.hBoxYiyan = QHBoxLayout()
        self.hBoxYiyan.addWidget(self.textLable)


        self.vboxMain = QVBoxLayout()
        self.vboxMain.addWidget(self.tab_widget)
        self.vboxMain.addLayout(self.vBoxControl)
        self.vboxMain.addLayout(self.hBoxYiyan)
        
        self.setLayout(self.vboxMain)

        self.openBtn.clicked.connect(self.openMusicFloder)
        self.playBtn.clicked.connect(self.playMusic)
        self.prevBtn.clicked.connect(self.prevMusic)
        self.nextBtn.clicked.connect(self.nextMusic)
        self.musicList.itemDoubleClicked.connect(self.doubleClicked)
        self.slider.sliderMoved[int].connect(lambda: self.player.setPosition(self.slider.value()))
        self.PlayModeBtn.clicked.connect(self.playModeSet)

        # self.format = QAudioFormat()
        # self.format.setSampleRate(44100)
        # self.format.setChannelCount(2)
        # self.format.setSampleSize(16)
        # self.format.setCodec("audio/pcm")
        # self.format.setByteOrder(QAudioFormat.LittleEndian)
        # self.format.setSampleType(QAudioFormat.SignedInt)

        # self.audio_output = QAudioOutput(self.format)
        # self.audio_output.setNotifyInterval(100)  # 设置通知间隔

        # self.buffer = self.audio_output.start()
        # self.data = None


        self.loadingSetting()

        self.initUI()

    # 初始化界面
    def initUI(self):
        self.resize(600, 400)
        self.center()
        self.setWindowTitle('音乐播放器')   
        self.setWindowIcon(QIcon('resource/image/favicon.ico'))
        self.show()
        
    # 窗口显示居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 打开文件夹
    def openMusicFloder(self):
        self.cur_path = QFileDialog.getExistingDirectory(self, "选取音乐文件夹", './')
        if self.cur_path:
            self.showMusicList()
            self.cur_playing_song = ''
            self.startTimeLabel.setText('00:00')
            self.endTimeLabel.setText('00:00')
            self.slider.setSliderPosition(0)
            self.updateSetting()
            self.is_pause = True
            self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/play.png)}")
    
    # 显示音乐列表
    def showMusicList(self):
        self.musicList.clear()
        for song in os.listdir(self.cur_path):
            if song.split('.')[-1] in self.song_formats:
                self.songs_list.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])
                self.musicList.addItem(song)
        self.musicList.setCurrentRow(0)
        if self.songs_list:
                self.cur_playing_song = self.songs_list[self.musicList.currentRow()][-1]

    # 提示
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

    # 设置当前播放的音乐
    def setCurPlaying(self):
        self.cur_playing_song = self.songs_list[self.musicList.currentRow()][-1]
        self.player.setMedia(QMediaContent(QUrl(self.cur_playing_song)))

        # format = QAudioFormat()
        # format.setSampleRate(44100)
        # format.setChannelCount(2)
        # format.setSampleSize(16)
        # format.setCodec("audio/pcm")
        # format.setByteOrder(QAudioFormat.LittleEndian)
        # format.setSampleType(QAudioFormat.SignedInt)
        
        # audio_output = QAudioOutput(format)
        # audio_output.setNotifyInterval(100)  # 设置通知间隔
        
        # buffer = audio_output.start()
        
        # # 将 MP3 文件加载为 AudioSegment 对象
        # audio = AudioSegment.from_file(self.cur_playing_song, format="mp3")

        # audio = AudioSegment.from_file(self.cur_playing_song, format="mp3")  # 加载 MP3 文件为 AudioSegment 对象
        # self.data = audio.raw_data  # 将音频数据转换为字节流  # 将数据写入缓冲区
        # print(self.data)
    


    # 播放/暂停播放
    def playMusic(self):
        if self.musicList.count() == 0:
                self.Tips('当前路径内无可播放的音乐文件')
                return
        if not self.player.isAudioAvailable():
                self.setCurPlaying()
        if self.is_pause or self.is_switching:
                self.player.play()
                print(self.cur_playing_song)
                self.is_pause = False
                self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/pause.png)}")
        elif (not self.is_pause) and (not self.is_switching):
                self.player.pause() # 暂停播放
                self.is_pause = True
                self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/play.png)}")
 	
    # 上一曲
    def prevMusic(self):
        self.slider.setValue(0)
        if self.musicList.count() == 0:
            self.Tips('当前路径内无可播放的音乐文件')
            return
        pre_row = self.musicList.currentRow()-1 if self.musicList.currentRow() != 0 else self.musicList.count() - 1
        self.musicList.setCurrentRow(pre_row)
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False

    # 下一曲
    def nextMusic(self):
        self.slider.setValue(0)
        if self.musicList.count() == 0:
            self.Tips('当前路径内无可播放的音乐文件')
            return
        next_row = self.musicList.currentRow()+1 if self.musicList.currentRow() != self.musicList.count()-1 else 0
        self.musicList.setCurrentRow(next_row)
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False  

    # 双击歌曲名称播放音乐
    def doubleClicked(self):
        self.slider.setValue(0)
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False

    # 根据播放模式自动播放，并刷新进度条
    def playByMode(self):
        # 刷新进度条
        if (not self.is_pause) and (not self.is_switching):
            self.slider.setMinimum(0)
            self.slider.setMaximum(self.player.duration())
            self.slider.setValue(self.slider.value() + 1000)
        self.startTimeLabel.setText(time.strftime('%M:%S', time.localtime(self.player.position()/1000)))
        self.endTimeLabel.setText(time.strftime('%M:%S', time.localtime(self.player.duration()/1000)))
        # 顺序播放
        if (self.playMode == 0) and (not self.is_pause) and (not self.is_switching):
            if self.musicList.count() == 0:
                return
            if self.player.position() == self.player.duration():
                self.nextMusic()
        # 单曲循环
        elif (self.playMode == 1) and (not self.is_pause) and (not self.is_switching):
            if self.musicList.count() == 0:
                return
            if self.player.position() == self.player.duration():
                self.is_switching = True
                self.setCurPlaying()
                self.slider.setValue(0)
                self.playMusic()
                self.is_switching = False
        # 随机播放
        elif (self.playMode == 2) and (not self.is_pause) and (not self.is_switching):
            if self.musicList.count() == 0:
                return
            if self.player.position() == self.player.duration():
                self.is_switching = True
                self.musicList.setCurrentRow(random.randint(0, self.musicList.count()-1))
                print(self.musicList.currentIndex)
                self.setCurPlaying()
                self.slider.setValue(0)
                self.playMusic()
                self.is_switching = False

    # 更新配置文件
    def updateSetting(self):
        config = configparser.ConfigParser()
        config.read(self.settingfilename)
        if not os.path.isfile(self.settingfilename):
            config.add_section('MP3Player')
        config.set('MP3Player', 'PATH', self.cur_path)
        config.write(open(self.settingfilename, 'w'))

    # 加载配置文件
    def loadingSetting(self):
        config = configparser.ConfigParser()
        config.read(self.settingfilename)
        if not os.path.isfile(self.settingfilename):
            return
        self.cur_path = config.get('MP3Player', 'PATH')
        self.showMusicList()
    
    # 播放模式设置
    def playModeSet(self):
        # 设置为单曲循环模式
        if self.playMode == 0:
            self.playMode = 1
            self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(resource/image/播放-循环播放.png)}")
        # 设置为随机播放模式
        elif self.playMode == 1:
            self.playMode = 2
            self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(resource/image/随机播放.png)}")
        # 设置为顺序播放模式
        elif self.playMode == 2:
            self.playMode = 0
            self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(resource/image/顺序播放.png)}")

    # 确认用户是否要真正退出
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "确定要退出吗？", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def create_slider_group(self, label_text):
        # 创建垂直布局
        slider_group = QVBoxLayout()

        # 创建滑动条和标签
        slider = QSlider()
        slider.setMinimum(-10)
        slider.setMaximum(10)
        slider.setTickInterval(1)
        slider.setOrientation(Qt.Vertical)

        slider_label = QLabel(label_text + " 0")

            # 创建水平布局
        slider_h_layout_1 = QHBoxLayout()
        # 添加弹性空间使滑动条和标签居中
        slider_h_layout_1.addStretch()
        slider_h_layout_1.addWidget(slider)
        slider_h_layout_1.addStretch()

        slider_h_layout_2 = QHBoxLayout()
        slider_h_layout_2.addStretch()
        slider_h_layout_2.addWidget(slider_label)
        slider_h_layout_2.addStretch()


        # 滑动条与标签绑定数值
        slider.valueChanged.connect(lambda value: slider_label.setText(label_text + " " + str(value)))

        # 将滑动条和标签添加到垂直布局
        slider_group.addLayout(slider_h_layout_1)
        slider_group.addLayout(slider_h_layout_2)

        return slider_group,slider_label
    
    def test_slider_label(self):
        print(self.slider_label1)
        print('\n')
        print(self.slider_label3)
        
    def yiyan(self):
        #一言


        api_url = 'https://v1.hitokoto.cn/?c=b&encode=json'
        response = requests.get(api_url)
        res = json.loads(response.text)
        a_word = res['hitokoto']+' --'+'《'+res['from']+'》'
        self.textLable.setText(a_word)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MP3Player()
    sys.exit(app.exec_())




