import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
import numpy as np

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('音乐播放器')
        self.setWindowIcon(QIcon('resource/image/favicon.ico'))
        self.resize(800, 600)

        # 创建音频播放器
        self.player = QMediaPlayer()
        self.player.setVolume(50)

        # 创建频谱可视化控件
        self.spectrum = pg.PlotWidget()
        self.spectrum.setWindowTitle('频谱可视化')
        self.spectrum.plotItem.showGrid(True, True)
        self.spectrum.setLabel('left', '能量')
        self.spectrum.setLabel('bottom', '频率')

        # 创建频带控制滑块
        self.slider_low = QSlider(Qt.Horizontal)
        self.slider_low.setRange(-10, 10)
        self.slider_low.setValue(0)
        self.slider_low.setTickInterval(1)
        self.slider_low.setTickPosition(QSlider.TicksBelow)
        self.slider_low.valueChanged.connect(self.updateEqualizer)

        self.slider_mid = QSlider(Qt.Horizontal)
        self.slider_mid.setRange(-10, 10)
        self.slider_mid.setValue(0)
        self.slider_mid.setTickInterval(1)
        self.slider_mid.setTickPosition(QSlider.TicksBelow)
        self.slider_mid.valueChanged.connect(self.updateEqualizer)

        self.slider_high = QSlider(Qt.Horizontal)
        self.slider_high.setRange(-10, 10)
        self.slider_high.setValue(0)
        self.slider_high.setTickInterval(1)
        self.slider_high.setTickPosition(QSlider.TicksBelow)
        self.slider_high.valueChanged.connect(self.updateEqualizer)

        # 创建控制按钮
        self.play_btn = QPushButton('播放')
        self.play_btn.clicked.connect(self.playMusic)

        # 设置布局
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.spectrum)
        layout.addWidget(QLabel('低音'))
        layout.addWidget(self.slider_low)
        layout.addWidget(QLabel('中音'))
        layout.addWidget(self.slider_mid)
        layout.addWidget(QLabel('高音'))
        layout.addWidget(self.slider_high)
        layout.addWidget(self.play_btn)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 加载音乐
        self.loadMusic('path_to_music_file.mp3')

    def loadMusic(self, file_path):
        # 加载音乐文件
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))

    def playMusic(self):
        # 播放/暂停音乐
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_btn.setText('播放')
        else:
            self.player.play()
            self.play_btn.setText('暂停')

    def updateEqualizer(self):
        # 更新均衡器设置
        low_gain = self.slider_low.value()
        mid_gain = self.slider_mid.value()
        high_gain = self.slider_high.value()

        # 在此处设置音频均衡器效果
        # 示例代码中，将音频的低音、中音和高音频段增益应用到音频播放器中

    def updateSpectrum(self):
        # 更新频谱可视化
        fft_data = self.getFFTData()
        self.spectrum.plotItem.plot(fft_data, clear=True)

    def getFFTData(self):
        # 获取频谱数据
        # 示例代码中，随机生成一个频谱数据
        data = np.random.rand(1000)
        return data

    def closeEvent(self, event):
        # 确认用户是否要真正退出
        reply = QMessageBox.question(self, 'Message',
                                      "确定要退出吗？", QMessageBox.Yes |
                                      QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.player.stop()
            event.accept()
        else:
            event.ignore()

