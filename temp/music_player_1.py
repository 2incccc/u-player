import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSlider, QTableWidget, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt, QFileInfo


class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setGeometry(100, 100, 600, 400)

        # 创建文件列表
        self.file_list = QTableWidget(self)
        self.file_list.setGeometry(50, 50, 500, 250)
        self.file_list.setColumnCount(4)
        self.file_list.setHorizontalHeaderLabels(['名称', '时长', '所在文件夹', ''])
        self.file_list.setColumnWidth(3, 100)  # 设置按钮列的宽度

        # 创建上一首按钮
        self.previous_button = QPushButton('上一首', self)
        self.previous_button.setGeometry(50, 320, 80, 30)
        self.previous_button.clicked.connect(self.previous_song)

        # 创建下一首按钮
        self.next_button = QPushButton('下一首', self)
        self.next_button.setGeometry(150, 320, 80, 30)
        self.next_button.clicked.connect(self.next_song)

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
        self.import_button = QPushButton('导入', self)
        self.import_button.setGeometry(50, 360, 80, 30)
        self.import_button.clicked.connect(self.import_files)

        # 播放队列
        self.play_queue = []

    def import_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles | QFileDialog.Directory)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                if self.is_supported_audio(file):
                    file_info = QFileInfo(file)
                    file_name = file_info.fileName()
                    file_duration = self.get_file_duration(file)
                    file_folder = file_info.dir().dirName()

                    row_count = self.file_list.rowCount()
                    self.file_list.insertRow(row_count)
                    self.file_list.setItem(row_count, 0, QTableWidgetItem(file_name))
                    self.file_list.setItem(row_count, 1, QTableWidgetItem(file_duration))
                    self.file_list.setItem(row_count, 2, QTableWidgetItem(file_folder))

                    # 创建添加到队列按钮
                    add_to_queue_button = QPushButton('添加到队列', self.file_list)
                    add_to_queue_button.clicked.connect(self.add_to_queue)
                    self.file_list.setCellWidget(row_count, 3, add_to_queue_button)
                else:
                    QMessageBox.warning(self, '不支持的文件类型', f'文件类型不支持：{file}')

    def is_supported_audio(self, file):
        supported_formats = ['.mp3', '.wav']  # 支持的音频格式列表
        file_ext = os.path.splitext(file)[1].lower()
        return file_ext in supported_formats

    def get_file_duration(self, file):
        # 获取文件时长的逻辑，这里仅返回示例字符串
        return '00:00'

    def previous_song(self):
        # 上一首功能的实现逻辑
        pass

    def next_song(self):
        # 下一首功能的实现逻辑
        pass

    def add_to_queue(self):
        # 将歌曲添加到播放队列的逻辑
        button = self.sender()
        row = self.file_list.indexAt(button.pos()).row()
        self.play_queue.append(row)
        print(f'添加到队列：{row}')

if __name__ == '__main__':
    app = QApplication([])
    player = MusicPlayer()
    player.show()
    app.exec_()
