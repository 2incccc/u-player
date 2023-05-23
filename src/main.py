import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSlider, QTableWidget, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt, QFileInfo, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from pydub import AudioSegment

from ..src import FrontEnd

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setGeometry(100, 100, 600, 400)


        ## 建立连接
        self.previous_button.clicked.connect(self.previous_song)

        self.next_button.clicked.connect(self.next_song)

        self.import_button.clicked.connect(self.import_files)

        self.play_button.clicked.connect(self.play_current_song)

        self.pause_button.clicked.connect(self.pause_song)

        # self.add_to_queue_button.clicked.connect(self.add_to_queue)

        # 创建文件列表
        # self.file_list = QTableWidget(self)
        # self.file_list.setGeometry(50, 50, 500, 250)
        # self.file_list.setColumnCount(4)
        self.file_list.setHorizontalHeaderLabels(['名称', '时长', '所在文件夹'])


        # 创建上一首按钮1
        self.previous_button = QPushButton('上一首', self)
        self.previous_button.setGeometry(50, 320, 80, 30)

        # 创建下一首按钮
        self.next_button = QPushButton('下一首', self)
        self.next_button.setGeometry(150, 320, 80, 30)

        # 创建音量条
        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setGeometry(250, 320, 150, 30)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)

        # 创建进度条
        self.progress_slider = QSlider(Qt.Horizontal, self)
        self.progress_slider.setGeometry(450, 320, 150, 30)
        self.progress_slider.setRange(0, 100)
        self.progress_slider.setValue(0)

        # 创建导入按钮

        self.play_button = QPushButton('播放', self)
        self.play_button.setGeometry(150, 360, 80, 30)

        self.pause_button = QPushButton('暂停', self)
        self.pause_button.setGeometry(250, 360, 80, 30)

        self.player = QMediaPlayer()
        self.player.mediaStatusChanged.connect(self.on_media_status_changed)

        self.play_queue = []  # 播放队列
        self.current_song_index = -1  # 当前播放歌曲的索引
# 导入文件
    def import_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles | QFileDialog.Directory)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                if self.is_supported_audio(file):
                    file_info = QFileInfo(file)
                    print(file_info)
                    file_name = file_info.fileName()
                    file_duration = self.get_file_duration(file)
                    file_folder = file_info.dir().dirName()

                    file_path = file_info.absoluteFilePath()
                    self.play_queue.append(file_path)  # 将文件路径添加到播放队列

                    row_count = self.file_list.rowCount()
                    self.file_list.insertRow(row_count)
                    self.file_list.setItem(row_count, 0, QTableWidgetItem(file_name))
                    self.file_list.setItem(row_count, 1, QTableWidgetItem(file_duration))
                    self.file_list.setItem(row_count, 2, QTableWidgetItem(file_folder))

                    add_to_queue_button = QPushButton('添加到队列', self.file_list)
                    self.file_list.setCellWidget(row_count, 3, add_to_queue_button)
                else:
                    QMessageBox.warning(self, '不支持的文件类型', f'文件类型不支持：{file}')
# 检查是否为支持音频格式
    def is_supported_audio(self, file):
        supported_formats = ['.mp3', '.wav']  # 支持的音频格式列表
        file_ext = os.path.splitext(file)[1].lower()
        return file_ext in supported_formats
# 获取音频时长
    def get_file_duration(self, file):
        audio = AudioSegment.from_file(file)
        duration = audio.duration_seconds
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        return f'{minutes:02d}:{seconds:02d}'

    # def add_to_queue(self):
    #     button = self.sender()
    #     row = self.file_list.indexAt(button.pos()).row()

    #     file_folder_item = self.file_list.item(row, 2)
    #     file_folder = file_folder_item.text()

    #     file_name_item = self.file_list.item(row, 0)
    #     file_name = file_name_item.text()

    #     file_path = os.path.join(file_folder, file_name)
    #     self.play_queue.append(file_path)
    #     print(f'添加到队列：{file_path}')
    #     print(self.play_queue)

    #     if self.current_song_index == -1:
    #         self.current_song_index = 0

    # def play_selected_song(self):
    #     selected_rows = self.file_list.selectionModel().selectedRows()
    #     if selected_rows:
    #         selected_row = selected_rows[0].row()
    #         file_path = self.play_queue[selected_row]  # 从播放队列中获取文件路径
    #         self.play_current_song(file_path)

    # def pause_song(self):
    #     self.player.pause()

    # def on_media_status_changed(self, status):
    #     if status == QMediaPlayer.EndOfMedia:  # 歌曲播放完毕
    #         self.current_song_index = -1  # 重置当前播放歌曲索引
    #         self.play_current_song()  # 播放下一首歌曲

    # def previous_song(self):
    #     if self.current_song_index > 0:
    #         self.current_song_index -= 1
    #         self.play_current_song()

    # def next_song(self):
    #     if self.current_song_index < len(self.play_queue) - 1:
    #         self.current_song_index += 1
    #         self.play_current_song()

    # def play_current_song(self):
    #     index = self.current_song_index
    #     print(index)
    #     print(self.file_list.item)
    #     file_name_item = self.file_list.item(index, 0)
    #     file_folder_item = self.file_list.item(index, 2)
    #     file_name = file_name_item.text()
    #     file_folder = file_folder_item.text()

    #     file_path = os.path.join(file_folder, file_name)
    #     print(file_path)
    #     media_content = QMediaContent(QUrl.fromLocalFile(file_path))
    #     self.player.setMedia(media_content)
    #     self.player.play()


# 主函数
if __name__ == '__main__':
    app = QApplication([])
    player = MusicPlayer()
    player.show()
    app.exec_()
