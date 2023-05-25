import os, time, sys, random, requests, json

from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QMessageBox, QHBoxLayout, QVBoxLayout, QSlider, QListWidget,
                            QPushButton, QLabel, QFileDialog, QTabWidget, QApplication, QLineEdit, QGridLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QUrl, QTimer, QFileSystemWatcher
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent,QAudioFormat, QAudioOutput

from MyQLabel import MyQLabel

from eq import eq
from path_convert import format_path_string
from spectrum_graph import plot_and_display_spectrogram

class MP3Player(QWidget):
    def __init__(self):
        ## 继承父类
        super().__init__()
        
        self.startTimeLabel = QLabel('00:00')
        self.endTimeLabel = QLabel('00:00')


        self.musicList = QListWidget()
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.songs_list = []
        self.cur_playing_song = ''
        self.is_pause = True
        self.player = QMediaPlayer()
        self.is_switching = False
        self.playMode = 0

        ## 播放进度条
        self.slider = QSlider(Qt.Horizontal, self)

        ## 按键
        self.PlayModeBtn = QPushButton(self)
        self.playBtn = QPushButton(self)
        self.prevBtn = QPushButton(self)
        self.nextBtn = QPushButton(self)
        self.openBtn = QPushButton(self)

        ## 一言
        self.textLable = MyQLabel()
        self.textLable.setText("点击体验个性化一言推送")
        self.textLable.connect_customized_slot(self.yiyan)
        font = QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        self.textLable.setFont(font)
        self.textLable.setAlignment(Qt.AlignCenter)

        self.tab_widget = QTabWidget(self)
        ## 第一个Widget，音乐列表
        widget1 = QWidget()
        layout1 = QVBoxLayout(widget1)

        self.musicList = QListWidget()
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.songs_list = []
        self.cur_playing_song = ''

        layout1.addWidget(self.musicList)

        ## 第二个Widget，简易均衡器
        widget2 = QWidget()
        layout2 = QVBoxLayout(widget2)
        h_layout_slider = QHBoxLayout()

        # 创建均衡器滑动条和标签
        self.slider_group1,self.slider_label1 = self.widget2_create_slider("低频调整(30-300Hz):")
        self.slider_group2,self.slider_label2 = self.widget2_create_slider("中频调整(300-5000Hz):")
        self.slider_group3,self.slider_label3 = self.widget2_create_slider("高频调整(5000-16000Hz):")

        h_layout_slider.addLayout(self.slider_group1)
        h_layout_slider.addLayout(self.slider_group2)
        h_layout_slider.addLayout(self.slider_group3)

        h_layout_btn = QHBoxLayout()
        self.eseq_confirmBtn = QPushButton("确认调整")
        h_layout_btn.ddStretch()
        h_layout_btn . addWidget(self.eseq_confirmBtn)
        h_layout_btn.addStretch()

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_slider)
        v_layout.addSpacing(20)
        v_layout.addLayout(h_layout_btn)

        layout2.addLayout(v_layout)

        ## 第三、四个Widget 两个表单，从函数中返回
        widget3 = self.widget3_create_form()
        widget4 = self.widget4_create_form()

        # 将四个Widget添加到TabWidget中
        self.tab_widget.addTab(widget1, "音乐列表")
        self.tab_widget.addTab(widget2, "简易均衡器")
        self.tab_widget.addTab(widget3, "高级均衡器")
        self.tab_widget.addTab(widget4, "声谱图生成")
        font = QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.tab_widget.setFont(font)

        ## 设置按键样式
        self.playBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/play.png)}")
        self.playBtn.setFixedSize(60, 60)
        self.nextBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/47最后一页、末页、下一首.png)}")
        self.nextBtn.setFixedSize(60, 60)
        self.prevBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/46第一页、首页、上一首.png)}")
        self.prevBtn.setFixedSize(60, 60)
        self.openBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/打开文件夹.png)}")
        self.openBtn.setFixedSize(50, 50)
        self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(./resource/image/顺序播放.png)}")
        self.PlayModeBtn.setFixedSize(50, 50)

        ## 计时器Timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.playByMode)

        ## 页面布局设置

        ## 底部播放布局
        self.hBoxSlider = QHBoxLayout()
        self.hBoxSlider.addWidget(self.startTimeLabel)
        self.hBoxSlider.addWidget(self.slider)
        self.hBoxSlider.addWidget(self.endTimeLabel)

        ## 底部按键布局
        self.hBoxButton = QHBoxLayout()
        self.hBoxButton.addWidget(self.PlayModeBtn)
        self.hBoxButton.addStretch(1)
        self.hBoxButton.addWidget(self.prevBtn)
        self.hBoxButton.addWidget(self.playBtn)
        self.hBoxButton.addWidget(self.nextBtn)
        self.hBoxButton.addStretch(1)
        self.hBoxButton.addWidget(self.openBtn)

        ## 以上两个水平布局 垂直排列
        self.vBoxControl = QVBoxLayout()
        self.vBoxControl.addLayout(self.hBoxSlider)
        self.vBoxControl.addLayout(self.hBoxButton)

        ## 最底部一言布局
        self.hBoxYiyan = QHBoxLayout()
        self.hBoxYiyan.addWidget(self.textLable)

        ## 整个布局垂直排布
        self.vboxMain = QVBoxLayout()
        self.vboxMain.addWidget(self.tab_widget)
        self.vboxMain.addLayout(self.vBoxControl)
        self.vboxMain.addLayout(self.hBoxYiyan)
        self.setLayout(self.vboxMain)

        ## 信号链接机制
        self.openBtn.clicked.connect(self.openMusicFloder)
        self.playBtn.clicked.connect(self.playMusic)
        self.prevBtn.clicked.connect(self.prevMusic)
        self.nextBtn.clicked.connect(self.nextMusic)
        self.musicList.itemDoubleClicked.connect(self.doubleClicked)
        self.slider.sliderMoved[int].connect(lambda: self.player.setPosition(self.slider.value()))
        self.PlayModeBtn.clicked.connect(self.playModeSet)
        self.eseq_confirmBtn.clicked.connect(self.easy_Equalizer)

        ## 监测文件夹是否变化
        self.file_watcher = QFileSystemWatcher(self)
        self.file_watcher.directoryChanged.connect(self.updateMusicList)

        self.initUI()


    # 初始化界面
    def initUI(self):
        self.resize(1000, 700)
        self.center()
        self.setWindowTitle('U-Player 本地音频播放工具')   
        self.setWindowIcon(QIcon('resource/favicon.png'))
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
            self.file_watcher.addPath(self.cur_path)
            self.showMusicList()
            self.cur_playing_song = ''
            self.startTimeLabel.setText('00:00')
            self.endTimeLabel.setText('00:00')
            self.slider.setSliderPosition(0)
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

    # 更新音乐列表
    def updateMusicList(self):
        existing_songs = [item[0] for item in self.songs_list]
        new_songs = []
        for song in os.listdir(self.cur_path):
            if song.split('.')[-1] in self.song_formats and song not in existing_songs:
                new_songs.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])
                self.musicList.addItem(song)
        self.songs_list.extend(new_songs)

    # 设置当前播放的音乐
    def setCurPlaying(self):
        self.cur_playing_song = self.songs_list[self.musicList.currentRow()][-1]
        self.player.setMedia(QMediaContent(QUrl(self.cur_playing_song)))

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
                self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/暂停 (1).png)}")
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

    def widget2_create_slider(self, label_text):
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

    ## 访问一言api
    def yiyan(self):
        #一言
        api_url = 'https://v1.hitokoto.cn/?c=b&encode=json'
        response = requests.get(api_url)
        res = json.loads(response.text)
        a_word = res['hitokoto']+' --'+'《'+res['from']+'》'
        self.textLable.setText(a_word)

    ## 建议均衡器实现
    def easy_Equalizer(self):
        
        low_gain = int(self.slider_label1.text().split()[-1])
        mid_gain = int(self.slider_label2.text().split()[-1])
        hig_gain = int(self.slider_label3.text().split()[-1]) 

        if int(self.slider_label1.text().split()[-1]) != 0 :
            freq_range = [30,300]
            gain = int(self.slider_label1.text().split()[-1])
        if int(self.slider_label2.text().split()[-1]) != 0:
            freq_range = [300,5000]
            gain = int(self.slider_label2.text().split()[-1])
        if  int(self.slider_label3.text().split()[-1]) != 0:
            freq_range = [5000,20000]
            gain = int(self.slider_label3.text().split()[-1])

        input_file = format_path_string(self.cur_playing_song)
        eq_output_file = eq(input_file, freq_range, gain, "./resource/media")
    ## Widget3建立表单
    def widget3_create_form(self):

        widget3_form_widget = QWidget()
        widget3_form_layout = QVBoxLayout(widget3_form_widget)

        widget3_sheet_layout = QGridLayout()

        # 创建起始频率输入框和标签
        start_freq_label = QLabel("起始频率(Hz):")
        self.start_freq_input = QLineEdit()
        widget3_sheet_layout.addWidget(start_freq_label, 0, 0)  # 第0行第0列
        widget3_sheet_layout.addWidget(self.start_freq_input, 0, 1)  # 第0行第1列

        # 创建截止频率输入框和标签
        stop_freq_label = QLabel("截止频率(Hz):")
        self.stop_freq_input = QLineEdit()
        widget3_sheet_layout.addWidget(stop_freq_label, 5, 0)  # 第1行第0列
        widget3_sheet_layout.addWidget(self.stop_freq_input, 5, 1)  # 第1行第1列

        # 创建增益倍数输入框和标签
        gain_label = QLabel("增益倍数(dB):")
        self.gain_input = QLineEdit()
        widget3_sheet_layout.addWidget(gain_label, 3, 2)  # 第2行第0列
        widget3_sheet_layout.addWidget(self.gain_input, 3, 3)  # 第2行第1列

        # 创建提交按钮并放置在底部居中
        btn_h_layout = QHBoxLayout()
        hdeq_confirmBtn = QPushButton("确认调整")
        btn_h_layout.addStretch()
        btn_h_layout.addWidget(hdeq_confirmBtn)
        btn_h_layout.addStretch()

        hdeq_confirmBtn.clicked.connect(self.widget3_run)

        widget3_form_layout.addLayout(widget3_sheet_layout)
        widget3_form_layout.addLayout(btn_h_layout)

        # 设置LineEdit的宽度
        self.start_freq_input.setFixedWidth(400)
        self.stop_freq_input.setFixedWidth(400)
        self.gain_input.setFixedWidth(400)

        return widget3_form_widget

    ## widget3 运行
    def widget3_run(self):
        try:
            self.start_freq_value = float(self.start_freq_input.text())
            self.stop_freq_value = float(self.stop_freq_input.text())
            self.gain_value = float(self.gain_input.text())
        except ValueError:
            # 处理无效输入的错误情况
            pass

        input_file = format_path_string(self.cur_playing_song)
        print(input_file)
        freq_range = [self.start_freq_value,self.stop_freq_value]
        gain_factor = self.gain_value
        eq_output_file = eq(input_file, freq_range, gain_factor, "./resource/media")

    ## widget4 
    def widget4_run(self):

        self.offset_time_value_min = int(self.offset_time_input.text().split(":")[0])
        
        self.offset_time_value_sec = int(self.offset_time_input.text().split(":")[1])
        self.offset_time_value = self.offset_time_value_min * 60 +self.offset_time_value_sec
        print(self.offset_time_value)
        self.duration_time_value = int(self.duration_time_input.text())


        input_file = format_path_string(self.cur_playing_song)
        plot_and_display_spectrogram(input_file,self.offset_time_value,self.duration_time_value)

    def widget4_create_form(self):

        widget4_form_widget = QWidget()
        widget4_form_layout = QVBoxLayout(widget4_form_widget)

        widget4_sheet_layout = QGridLayout()

        # 创建起始频率输入框和标签
        offset_time_label = QLabel("起始时间(分:秒):")
        self.offset_time_input = QLineEdit()
        widget4_sheet_layout.addWidget(offset_time_label, 0, 1)  # 第0行第0列
        widget4_sheet_layout.addWidget(self.offset_time_input, 0, 2)  # 第0行第1列

        

        # 创建截止频率输入框和标签
        duration_time_label = QLabel("持续时间(s):")
        self.duration_time_input = QLineEdit()
        widget4_sheet_layout.addWidget(duration_time_label, 3, 1)  # 第1行第0列
        widget4_sheet_layout.addWidget(self.duration_time_input, 3, 2)  # 第1行第1列


        # 创建提交按钮并放置在底部居中
        widget4_btn_h_layout = QHBoxLayout()
        confirm_specturm_Btn = QPushButton("确认生成")
        widget4_btn_h_layout.addStretch()
        widget4_btn_h_layout.addWidget(confirm_specturm_Btn)
        widget4_btn_h_layout.addStretch()

        confirm_specturm_Btn.clicked.connect(self.widget4_run)

        widget4_form_layout.addLayout(widget4_sheet_layout)
        widget4_form_layout.addLayout(widget4_btn_h_layout)

        # 设置LineEdit的宽度
        self.offset_time_input.setFixedWidth(400)
        self.duration_time_input.setFixedWidth(400)
        self.gain_input.setFixedWidth(400)

        return widget4_form_widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MP3Player()
    sys.exit(app.exec_())




