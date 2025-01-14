# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrontEnd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(900, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(900, 600))
        Form.setMaximumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.music = QtWidgets.QWidget()
        self.music.setObjectName("music")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.music)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Button_insert = QtWidgets.QPushButton(self.music)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_insert.sizePolicy().hasHeightForWidth())
        self.Button_insert.setSizePolicy(sizePolicy)
        self.Button_insert.setMinimumSize(QtCore.QSize(91, 20))
        self.Button_insert.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_insert.setFont(font)
        self.Button_insert.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon = QtGui.QIcon.fromTheme("search")
        self.Button_insert.setIcon(icon)
        self.Button_insert.setObjectName("Button_insert")
        self.verticalLayout_5.addWidget(self.Button_insert)
        self.line = QtWidgets.QFrame(self.music)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.music_files = QtWidgets.QTableWidget(self.music)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music_files.sizePolicy().hasHeightForWidth())
        self.music_files.setSizePolicy(sizePolicy)
        self.music_files.setAutoFillBackground(False)
        self.music_files.setStyleSheet("border-color: rgb(133, 138, 161);\n"
"gridline-color: rgb(206, 206, 206);\n"
"border-right-color: rgb(0, 85, 127);\n"
"\n"
"border-top-color: rgb(0, 85, 127);")
        self.music_files.setFrameShape(QtWidgets.QFrame.Box)
        self.music_files.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.music_files.setLineWidth(1)
        self.music_files.setMidLineWidth(1)
        self.music_files.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.music_files.setAlternatingRowColors(False)
        self.music_files.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.music_files.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.music_files.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.music_files.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.music_files.setGridStyle(QtCore.Qt.SolidLine)
        self.music_files.setRowCount(5)
        self.music_files.setObjectName("music_files")
        self.music_files.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.music_files.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.music_files.setHorizontalHeaderItem(1, item)
        self.music_files.horizontalHeader().setCascadingSectionResizes(False)
        self.music_files.horizontalHeader().setDefaultSectionSize(500)
        self.music_files.horizontalHeader().setMinimumSectionSize(100)
        self.music_files.horizontalHeader().setSortIndicatorShown(False)
        self.music_files.horizontalHeader().setStretchLastSection(True)
        self.music_files.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout_5.addWidget(self.music_files)
        self.tabWidget.addTab(self.music, "")
        self.play = QtWidgets.QWidget()
        self.play.setObjectName("play")
        self.tabWidget.addTab(self.play, "")
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.HorizaontalLayout = QtWidgets.QHBoxLayout()
        self.HorizaontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.HorizaontalLayout.setSpacing(2)
        self.HorizaontalLayout.setObjectName("HorizaontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.HorizaontalLayout.addItem(spacerItem1)
        self.music_name = QtWidgets.QTextBrowser(Form)
        self.music_name.setMinimumSize(QtCore.QSize(0, 0))
        self.music_name.setMaximumSize(QtCore.QSize(90, 18))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.music_name.setFont(font)
        self.music_name.setStyleSheet("font: 10pt \"方正粗黑宋简体\";")
        self.music_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.music_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_name.setLineWidth(1)
        self.music_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.music_name.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.music_name.setObjectName("music_name")
        self.HorizaontalLayout.addWidget(self.music_name)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.HorizaontalLayout.addItem(spacerItem2)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setMaximumSize(QtCore.QSize(700, 8))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: #00557f;\n"
"    width: 20px;\n"
"}")
        self.progressBar.setProperty("value", 20)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.HorizaontalLayout.addWidget(self.progressBar)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.HorizaontalLayout.addItem(spacerItem3)
        self.file_duration = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_duration.sizePolicy().hasHeightForWidth())
        self.file_duration.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.file_duration.setFont(font)
        self.file_duration.setObjectName("file_duration")
        self.HorizaontalLayout.addWidget(self.file_duration)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.HorizaontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.HorizaontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(13, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.Button_like = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_like.sizePolicy().hasHeightForWidth())
        self.Button_like.setSizePolicy(sizePolicy)
        self.Button_like.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_like.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_1/喜欢.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_like.setIcon(icon)
        self.Button_like.setIconSize(QtCore.QSize(20, 20))
        self.Button_like.setObjectName("Button_like")
        self.horizontalLayout.addWidget(self.Button_like)
        self.Button_share = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_share.sizePolicy().hasHeightForWidth())
        self.Button_share.setSizePolicy(sizePolicy)
        self.Button_share.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_share.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon_1/分享 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_share.setIcon(icon1)
        self.Button_share.setIconSize(QtCore.QSize(20, 20))
        self.Button_share.setObjectName("Button_share")
        self.horizontalLayout.addWidget(self.Button_share)
        self.Button_download = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_download.sizePolicy().hasHeightForWidth())
        self.Button_download.setSizePolicy(sizePolicy)
        self.Button_download.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_download.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon_1/下载.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_download.setIcon(icon2)
        self.Button_download.setIconSize(QtCore.QSize(20, 20))
        self.Button_download.setObjectName("Button_download")
        self.horizontalLayout.addWidget(self.Button_download)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Button_loop = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_loop.sizePolicy().hasHeightForWidth())
        self.Button_loop.setSizePolicy(sizePolicy)
        self.Button_loop.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_loop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon_1/播放-循环播放.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_loop.setIcon(icon3)
        self.Button_loop.setIconSize(QtCore.QSize(20, 20))
        self.Button_loop.setAutoDefault(False)
        self.Button_loop.setObjectName("Button_loop")
        self.horizontalLayout_2.addWidget(self.Button_loop)
        self.Button_prior = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_prior.sizePolicy().hasHeightForWidth())
        self.Button_prior.setSizePolicy(sizePolicy)
        self.Button_prior.setAutoFillBackground(False)
        self.Button_prior.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_prior.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon_1/46第一页、首页、上一首.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_prior.setIcon(icon4)
        self.Button_prior.setIconSize(QtCore.QSize(40, 40))
        self.Button_prior.setCheckable(False)
        self.Button_prior.setAutoRepeat(False)
        self.Button_prior.setObjectName("Button_prior")
        self.horizontalLayout_2.addWidget(self.Button_prior)
        self.Button_play = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_play.sizePolicy().hasHeightForWidth())
        self.Button_play.setSizePolicy(sizePolicy)
        self.Button_play.setAutoFillBackground(False)
        self.Button_play.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_play.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon_1/播放 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_play.setIcon(icon5)
        self.Button_play.setIconSize(QtCore.QSize(40, 40))
        self.Button_play.setCheckable(False)
        self.Button_play.setAutoRepeat(False)
        self.Button_play.setObjectName("Button_play")
        self.horizontalLayout_2.addWidget(self.Button_play)
        self.Button_next = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_next.sizePolicy().hasHeightForWidth())
        self.Button_next.setSizePolicy(sizePolicy)
        self.Button_next.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Button_next.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon_1/47最后一页、末页、下一首.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_next.setIcon(icon6)
        self.Button_next.setIconSize(QtCore.QSize(40, 40))
        self.Button_next.setCheckable(False)
        self.Button_next.setAutoRepeat(False)
        self.Button_next.setObjectName("Button_next")
        self.horizontalLayout_2.addWidget(self.Button_next)
        spacerItem8 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.Button_volume = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_volume.sizePolicy().hasHeightForWidth())
        self.Button_volume.setSizePolicy(sizePolicy)
        self.Button_volume.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_volume.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon_1/音量小.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_volume.setIcon(icon7)
        self.Button_volume.setIconSize(QtCore.QSize(20, 20))
        self.Button_volume.setObjectName("Button_volume")
        self.horizontalLayout_2.addWidget(self.Button_volume)
        self.Slider_music = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_music.sizePolicy().hasHeightForWidth())
        self.Slider_music.setSizePolicy(sizePolicy)
        self.Slider_music.setMaximumSize(QtCore.QSize(210, 10))
        self.Slider_music.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_music.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Slider_music.setObjectName("Slider_music")
        self.horizontalLayout_2.addWidget(self.Slider_music)
        spacerItem9 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.yiyan_lable = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        self.yiyan_lable.setFont(font)
        self.yiyan_lable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.yiyan_lable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.yiyan_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.yiyan_lable.setIndent(1)
        self.yiyan_lable.setObjectName("yiyan_lable")
        self.verticalLayout.addWidget(self.yiyan_lable)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button_insert.setText(_translate("Form", "导入文件"))
        self.music_files.setSortingEnabled(False)
        item = self.music_files.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名称"))
        item = self.music_files.horizontalHeaderItem(1)
        item.setText(_translate("Form", "时长"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.music), _translate("Form", "音乐列表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.play), _translate("Form", "均衡器"))
        self.music_name.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'方正粗黑宋简体\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">音乐名称</span></p></body></html>"))
        self.file_duration.setText(_translate("Form", "00:00"))
        self.yiyan_lable.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">星光不负赶路人，时光不负有心人</span></p></body></html>"))
import demo_rc
