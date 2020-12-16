# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.sip
from ui.my_widgets import *
from configs import default_setting

class A_form():
    def __init__(self, Form, event):
        self.main = Form
        Form.setObjectName("MainWindow")
        Form.resize(400, 600)
        Form.setStyleSheet('QMainWindow {background-color: #242424; color: #E6E6E6;}')
        Form.setMinimumSize(QtCore.QSize(400, 600))
        Form.setMaximumSize(QtCore.QSize(700, 600))
        self.font24 = QtGui.QFont('微軟正黑體', 24)
        self.font16 = QtGui.QFont('微軟正黑體', 16)
        self.font12 = QtGui.QFont('微軟正黑體', 12)
        self.font9 = QtGui.QFont('微軟正黑體', 9)

        """main"""
        self.label_main = QtWidgets.QLabel(Form)
        self.label_main.setGeometry(QtCore.QRect(10, 10, 380, 280))
        # self.label_main.setStyleSheet('QLabel {background-image : url("./src/waiting.png")}')
        self.label_main.setObjectName("label_main")

        self.combo_platform = my_ComboBox(Form)
        self.combo_platform.setFont(self.font16)
        self.combo_platform.setGeometry(QtCore.QRect(50, 300, 300, 40))
        self.combo_platform.setObjectName("combo_platform")
        self.combo_platform.setEditable(True)
        self.combo_platform.lineEdit().setFont(self.font16)
        self.combo_platform.lineEdit().setReadOnly(True)
        self.combo_platform.lineEdit().setAlignment(Qt.AlignCenter)

        self.edit_channel = my_line_edit(Form)
        self.edit_channel.setFont(self.font16)
        self.edit_channel.setGeometry(QtCore.QRect(50, 350, 300, 40))
        self.edit_channel.setAlignment(Qt.AlignCenter)

        self.btn_login = my_btn(Form)
        self.btn_login.setFont(self.font24)
        self.btn_login.setGeometry(QtCore.QRect(125, 400, 150, 40))
        self.btn_login.setObjectName("btn_login")

        self.name_label = my_label(Form)
        self.name_label.setGeometry(QtCore.QRect(5, 580, 100, 20))
        self.name_label.setObjectName("name_label")

        self.cb_optional = my_cb(Form)
        self.cb_optional.setGeometry(QtCore.QRect(295, 580, 105, 20))
        self.cb_optional.setObjectName("cb_optional")

        """option"""
        self.btn_save = my_btn(Form)
        self.btn_save.setFont(self.font12)
        self.btn_save.setGeometry(QtCore.QRect(590, 534, 100, 23))
        self.btn_save.setObjectName("btn_save")

        self.btn_re_exec = my_btn(Form)
        self.btn_re_exec.setFont(self.font12)
        self.btn_re_exec.setGeometry(QtCore.QRect(590, 567, 100, 23))
        self.btn_re_exec.setObjectName("btn_font")

        """ canvas """
        self.gb_canvas = my_gb(Form)
        self.gb_canvas.setFont(self.font12)
        self.gb_canvas.setGeometry(QtCore.QRect(420, 20, 260, 100))

        self.cb_on_top = my_cb(self.gb_canvas)
        self.cb_on_top.setFont(self.font12)
        self.cb_on_top.setGeometry(QtCore.QRect(30, 30, 215, 20))
        self.cb_on_top.setObjectName("cb_optional")
        self.cb_on_top.setChecked(True)

        self.cb_avoid_crosshair = my_cb(self.gb_canvas)
        self.cb_avoid_crosshair.setFont(self.font12)
        self.cb_avoid_crosshair.setGeometry(QtCore.QRect(30, 60, 215, 20))
        self.cb_avoid_crosshair.setObjectName("cb_avoid_crosshair")
        self.cb_avoid_crosshair.setChecked(True)

        """ barrage """
        self.gb_barrage = my_gb(Form)
        self.gb_barrage.setFont(self.font12)
        self.gb_barrage.setGeometry(QtCore.QRect(420, 140, 260, 181))

        self.cb_show_name = my_cb(self.gb_barrage)
        self.cb_show_name.setFont(self.font12)
        self.cb_show_name.setGeometry(QtCore.QRect(30, 30, 191, 21))
        self.cb_show_name.setObjectName("cb_show_name")

        self.label_size = my_label(self.gb_barrage)
        self.label_size.setFont(self.font12)
        self.label_size.setGeometry(QtCore.QRect(15, 60, 76, 21))
        self.label_size.setObjectName("label_size")
        self.label_size.setAlignment(Qt.AlignCenter)

        self.edit_size = my_line_edit(self.gb_barrage)
        self.edit_size.setFont(self.font12)
        self.edit_size.setGeometry(QtCore.QRect(100, 60, 121, 21))
        self.edit_size.setAlignment(Qt.AlignCenter)
        self.edit_size.setValidator(QIntValidator())

        self.label_time = my_label(self.gb_barrage)
        self.label_time.setFont(self.font12)
        self.label_time.setGeometry(QtCore.QRect(15, 90, 76, 21))
        self.label_time.setObjectName("label_time")
        self.label_time.setAlignment(Qt.AlignCenter)

        self.edit_time = my_line_edit(self.gb_barrage)
        self.edit_time.setFont(self.font12)
        self.edit_time.setGeometry(QtCore.QRect(100, 90, 121, 21))
        self.edit_time.setAlignment(Qt.AlignCenter)
        self.edit_time.setValidator(QIntValidator())

        self.label_alpha = my_label(self.gb_barrage)
        self.label_alpha.setFont(self.font12)
        self.label_alpha.setGeometry(QtCore.QRect(30, 120, 61, 21))
        self.label_alpha.setObjectName("label_alpha")
        self.label_alpha.setAlignment(Qt.AlignCenter)

        self.sli_alpha = my_slider(Qt.Horizontal, self.gb_barrage)
        self.sli_alpha.setGeometry(QtCore.QRect(100, 120, 121, 22))
        self.sli_alpha.setObjectName("sli_alpha")

        self.label_font = my_label(self.gb_barrage)
        self.label_font.setFont(self.font9)
        self.label_font.setGeometry(QtCore.QRect(20, 150, 230, 23))
        self.label_font.setObjectName("label_font")

        """ Twitch """
        self.gb_twitch = my_gb(Form)
        self.gb_twitch.setFont(self.font12)
        self.gb_twitch.setGeometry(QtCore.QRect(420, 340, 260, 90))

        self.label_twitch_id = my_label(self.gb_twitch)
        self.label_twitch_id.setFont(self.font12)
        self.label_twitch_id.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.label_twitch_id.setObjectName("label_twitch_id")
        self.label_twitch_id.setAlignment(Qt.AlignCenter)

        self.edit_twitch_id = my_line_edit(self.gb_twitch)
        self.edit_twitch_id.setFont(self.font12)
        self.edit_twitch_id.setGeometry(QtCore.QRect(100, 30, 121, 21))
        self.edit_twitch_id.setAlignment(Qt.AlignCenter)
        self.edit_twitch_id.setValidator(QIntValidator())

        self.label_twitch_thanks = my_label(self.gb_twitch)
        self.label_twitch_thanks.setFont(self.font9)
        self.label_twitch_thanks.setGeometry(QtCore.QRect(20, 60, 231, 21))
        self.label_twitch_thanks.setObjectName("label_twitch_thanks")

        """ not ui """
        self.bot_login_signal = my_btn(Form)
        self.bot_login_signal.setVisible(False)

        self.retranslateUi(Form)
        self.init_platform_combobox()
        self.load_setting()

        QtCore.QMetaObject.connectSlotsByName(Form)
        self.event_connect(event)

    def event_connect(self, event):
        self.edit_channel.returnPressed.connect(lambda:self.btn_login.click())
        self.edit_channel.editingFinished.connect(event.edit_channel)
        self.btn_login.clicked.connect(event.btn_login)
        self.btn_save.clicked.connect(event.btn_save)
        self.combo_platform.currentIndexChanged.connect(event.combo_platform)
        self.cb_optional.stateChanged.connect(event.cb_optional)
        self.cb_on_top.stateChanged.connect(event.cb_on_top)
        self.cb_avoid_crosshair.stateChanged.connect(event.cb_avoid_crosshair)
        self.sli_alpha.valueChanged.connect(event.sli_alpha)
        self.cb_show_name.stateChanged.connect(event.cb_show_name)
        self.btn_re_exec.clicked.connect(event.btn_re_exec)

        self.bot_login_signal.clicked.connect(self.main.login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "彈幕機器人 V1.0"))
        self.btn_login.setText(_translate("MainWindow", "登入頻道"))
        self.edit_channel.setPlaceholderText(_translate("MainWindow", "channel"))
        self.name_label.setText(_translate("MainWindow", "by shounen51"))
        self.cb_optional.setText(_translate("MainWindow", "開啟設定選單→"))

        self.gb_canvas.setTitle(_translate("MainWindow", "彈幕畫布設定"))
        self.cb_on_top.setText(_translate("MainWindow", "彈幕視窗置於頂部"))
        self.cb_avoid_crosshair.setText(_translate("MainWindow", "彈幕避開遊戲準心"))

        self.gb_barrage.setTitle(_translate("MainWindow", "彈幕設定"))
        self.label_size.setText(_translate("MainWindow", "※字體大小"))
        self.label_time.setText(_translate("MainWindow", "※顯示時間"))
        self.label_alpha.setText(_translate("MainWindow", "字體透明"))
        self.cb_show_name.setText(_translate("MainWindow", "顯示觀眾名稱"))
        self.label_font.setText(_translate("MainWindow", "※部分功能需要重新啟動程式後生效"))
        
        self.gb_twitch.setTitle(_translate("MainWindow", "Twitch專屬表情符號"))
        self.label_twitch_id.setText(_translate("MainWindow", "頻道ID"))
        self.label_twitch_thanks.setText(_translate("MainWindow", "※感謝https://twitchemotes.com/提供API"))

        self.btn_save.setText(_translate("MainWindow", "儲存設定"))
        self.btn_re_exec.setText(_translate("MainWindow", "重新開啟"))
        

    def init_platform_combobox(self):
        self.combo_platform.addItems(platform_list)

    def load_setting(self):
        platform = self.main.from_setting('connect', 'platform', 'str')
        channel = self.main.from_setting(platform, 'channel', 'str')
        cover = self.main.from_setting('canvas', 'cover', 'bool')
        avoid_crosshair = self.main.from_setting('canvas', 'avoid_crosshair', 'bool')
        # font = self.main.from_setting('barrage', 'font', 'str')
        size = self.main.from_setting('barrage', 'size', 'str')
        alpha = self.main.from_setting('barrage', 'alpha', 'int')
        show_name = self.main.from_setting('barrage', 'name', 'bool')
        alive_time = self.main.from_setting('barrage', 'alive_time', 'str')
        twitch_channel_id = self.main.from_setting('twitch', 'channel_id', 'str')

        i = self.combo_platform.findText(platform)
        self.combo_platform.setCurrentIndex(i)
        self.edit_channel.setText(channel)
        # self.edit_font.setText(font)
        self.edit_size.setText(size)
        self.edit_time.setText(alive_time)
        self.sli_alpha.setValue(alpha)
        self.cb_avoid_crosshair.setChecked(avoid_crosshair)
        self.cb_on_top.setChecked(cover)
        self.cb_show_name.setChecked(show_name)
        self.edit_twitch_id.setText(twitch_channel_id)