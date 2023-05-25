import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFileDialog, QListWidget, QListWidgetItem
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QUrl, QTime
from PyQt5.QtMultimedia import QMediaPlayer,QMediaPlaylist 

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化播放器
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        # 初始化UI界面
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)

        # 设置窗口图标
        self.setWindowIcon(QIcon("icon.png"))

        # 添加音量调节和进度条
        self.volume_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.volume_slider.setGeometry(50, 500, 200, 30)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSingleStep(1)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.setVolume)

        self.position_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.position_slider.setGeometry(50, 550, 700, 30)
        self.position_slider.sliderMoved.connect(self.setPosition)

        # 添加标签
        self.current_time = QLabel(self)
        self.current_time.setGeometry(350, 500, 100, 30)

        self.total_time = QLabel(self)
        self.total_time.setGeometry(450, 500, 100, 30)

        # 添加按钮
        self.open_button = QPushButton("Open", self)
        self.open_button.setGeometry(50, 450, 100, 30)
        self.open_button.clicked.connect(self.openFile)

        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(200, 450, 100, 30)
        self.play_button.clicked.connect(self.play)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.setGeometry(350, 450, 100, 30)
        self.pause_button.clicked.connect(self.pause)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(500, 450, 100, 30)
        self.stop_button.clicked.connect(self.stop)

        self.previous_button = QPushButton("Previous", self)
        self.previous_button.setGeometry(650, 450, 100, 30)
        self.previous_button.clicked.connect(self.previous)

        self.next_button = QPushButton("Next", self)
        self.next_button.setGeometry(650, 500, 100, 30)
        self.next_button.clicked.connect(self.next)

        self.setStyleSheet("""
    QSlider {
        background-color: transparent;
    }

    QSlider::groove:horizontal {
        height: 5px;
        background-color: #D8D8D8;
        border-radius: 2px;
    }

    QSlider::handle:horizontal {
        width: 10px;
        height: 10px;
        background-color: #0077FF;
        border-radius: 5px;
        margin-top: -3px;
    }

    QPushButton {
        background-color: #0077FF;
        border: none;
        border-radius: 5px;
        color: #FFFFFF;
        font-size: 16px;
        padding: 5px 10px;
    }

    QPushButton:hover {
        background-color: #0066CC;
    }

    QLabel {
        font-size: 14px;
    }
""")
        # 显示窗口
        self.show()

    def openFile(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Music", ".", "Music Files (*.mp3 *.ogg *.wav)")

        # 如果有选择文件，则添加到播放列表中并播放
        if file_path:
            url = QUrl.fromLocalFile(file_path)
            self.playlist.addMedia(url)
            self.player.setVolume(self.volume_slider.value())
            self.player.play()

    def play(self):
        self.player.setVolume(self.volume_slider.value())
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def previous(self):
        self.playlist.previous()

    def next(self):
        self.playlist.next()

    def setVolume(self, value):
        self.player.setVolume(value)

    def setPosition(self, value):
        self.player.setPosition(value)

    def updatePosition(self, position):
        self.position_slider.setValue(position)

    # 显示当前时间和总时间
        current_time = QTime(0, 0, 0).addMSecs(position)
        total_time = QTime(0, 0, 0).addMSecs(self.player.duration())

        self.current_time.setText(current_time.toString("mm:ss"))
        self.total_time.setText(total_time.toString("mm:ss"))

    def updateButtonState(self, state):
        if state == QMediaPlayer.State.PlayingState:
            self.play_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.stop_button.setEnabled(True)
        else:
            self.play_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.stop_button.setEnabled(False)

    def updateMedia(self, media):
    # 设置窗口标题
        self.setWindowTitle(media.canonicalUrl().fileName())

    # 设置封面
        if media.hasMetaData():
            cover_image = media.metaData("CoverArt").value()
            if cover_image:
                pixmap = QPixmap()
                pixmap.loadFromData(cover_image)
                self.cover_label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        # 按下空格键切换播放/暂停
        if event.key() == Qt.Key.Key_Space:
            if self.player.state() == QMediaPlayer.State.PlayingState:
                self.player.pause()
            else:
                self.player.play()

    def closeEvent(self, event):
    # 退出时停止播放
        self.player.stop()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec())