import os
import sys

from PyQt6.QtCore import Qt, QUrl, QTime
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QFileDialog, QGridLayout, QHBoxLayout,QLabel, QMainWindow, QProgressBar, QPushButton,QSlider, QStatusBar, QVBoxLayout, QWidget)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化音乐播放器和播放列表
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)
        self.player.durationChanged.connect(self.update_duration)

        # 创建 UI
        self.create_ui()

    def create_ui(self):
        # 创建控件
        self.cover_label = QLabel()
        self.cover_label.setFixedSize(300, 300)
        self.cover_label.setScaledContents(True)
        self.cover_label.setObjectName("cover_label")

        self.title_label = QLabel("Music Title")
        self.title_label.setObjectName("title_label")

        self.artist_label = QLabel("Artist Name")
        self.artist_label.setObjectName("artist_label")

        self.current_time = QLabel("00:00")
        self.current_time.setObjectName("current_time")

        self.total_time = QLabel("00:00")
        self.total_time.setObjectName("total_time")

        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_bar.valueChanged.connect(self.set_position)

        self.volume_slider = QSlider(Qt.Orientation.Horizontal,self)
        self.volume_slider.setObjectName("volume_slider")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)

        self.play_button = QPushButton("Play")
        self.play_button.setObjectName("play_button")
        self.play_button.clicked.connect(self.play)

        self.pause_button = QPushButton("Pause")
        self.pause_button.setObjectName("pause_button")
        self.pause_button.clicked.connect(self.pause)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setObjectName("stop_button")
        self.stop_button.clicked.connect(self.stop)

        self.previous_button = QPushButton("Previous")
        self.previous_button.setObjectName("previous_button")
        self.previous_button.clicked.connect(self.playlist.previous)

        self.next_button = QPushButton("Next")
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.playlist.next)

        self.add_button = QPushButton("Add")
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_song)

        # 创建布局
        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)

        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(20)

        grid_layout.addWidget(self.cover_label, 0, 0, 3, 1, Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(self.title_label, 0, 1)
        grid_layout.addWidget(self.artist_label, 1, 1)
        grid_layout.addWidget(self.current_time, 2, 1, Qt.AlignmentFlag.AlignLeft)
        grid_layout.addWidget(self.total_time, 2, 1, Qt.AlignmentFlag.AlignRight)
        grid_layout.addWidget(self.progress_bar, 3, 0, Qt.AlignmentFlag.AlignLeft)
        grid_layout.addWidget(self.volume_slider, 3, 1, Qt.AlignmentFlag.AlignRight)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.pause_button)
        control_layout.addWidget(self.stop_button)
        control_layout.addWidget(self.previous_button)
        control_layout.addWidget(self.next_button)
        control_layout.addWidget(self.add_button)

        layout.addLayout(grid_layout)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.volume_slider)
        layout.addLayout(control_layout)

        # 设置状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 设置窗口属性
        self.setWindowTitle("Music Player")
        self.setFixedSize(500, 700)
        self.setWindowIcon(QIcon("icon.png"))
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

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, value):
        self.player.setVolume(value)

    def set_position(self, position):
        self.player.setPosition(position)

    def update_duration(self, duration):
        self.progress_bar.setMaximum(duration)
        self.total_time.setText(str(QTime(0, 0).addMSecs(duration).toString("mm:ss")))

    def add_song(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
        if file_path != "":
            song_name = os.path.basename(file_path)
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.playlist.setCurrentIndex(self.playlist.mediaCount() - 1)

            item = QWidget()
            layout = QHBoxLayout(item)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)

            icon_label = QLabel()
            icon_label.setFixedSize(30, 30)
            icon_label.setScaledContents(True)
            icon_label.setPixmap(QPixmap("music_icon.png"))

            name_label = QLabel(song_name)
            name_label.setObjectName("song_name")

            layout.addWidget(icon_label)
            layout.addWidget(name_label)

            self.progress_bar.setValue(0)
            self.statusBar.showMessage(f"Added {song_name}")
            self.playlist.currentMediaChanged.connect(lambda: self.change_song(item))
            self.progress_bar.valueChanged.connect(self.update_position)

            self.layout().addWidget(item)

    def change_song(self, item):
        name_label = item.findChild(QLabel, "song_name")
        media = self.player.currentMedia()
        if media.isValid():
            song_name = media.canonicalUrl().fileName()
            name_label.setText(song_name)

    def update_position(self, position):
        self.current_time.setText(str(QTime(0, 0).addMSecs(position).toString("mm:ss")))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec())