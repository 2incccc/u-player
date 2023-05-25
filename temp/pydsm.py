import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
import numpy as np
import pydsm

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('音乐播放器')
        self.setWindowIcon(QIcon('resource/image/favicon.ico'))
        self.resize(400, 300)

        # 创建音频播放器
        self.player = QMediaPlayer()
        self.player.setVolume(50)

        # 创建低频增益调节滑块
        self.slider_low = QSlider(Qt.Vertical)
        self.slider_low.setRange(-10, 10)
        self.slider_low.setValue(0)
        self.slider_low.setTickInterval(1)
        self.slider_low.setTickPosition(QSlider.TicksLeft)
        self.slider_low.valueChanged.connect(self.updateLowGain)

        # 设置布局
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('低频增益'))
        layout.addWidget(self.slider_low)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 加载音乐
        self.loadMusic('path_to_music_file.mp3')

        # 创建均衡器
        self.eq = pydsm.Equalizer(1, 44100)  # 1通道，采样率44100Hz
        self.eq.set_gain(0, 1.0)  # 初始化低频增益为1.0

    def loadMusic(self, file_path):
        # 加载音乐文件
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))

    def updateLowGain(self, value):
        # 更新低频增益
        gain = value / 10.0  # 将滑块值映射到增益范围
        self.eq.set_gain(0, gain)  # 设置低频增益

    def processAudio(self, audio_data):
        # 在这里对音频数据应用均衡器效果
        processed_data = self.eq.process(audio_data)
        return processed_data

    def handleAudioData(self, audio_data):
        # 处理音频数据并播放
        processed_data = self.processAudio(audio_data)
        # 将处理后的数据传递给音频播放器
        self.player.audioOutput().write(processed_data)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                      "确定要退出吗？", QMessageBox.Yes |
                                      QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
