# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
from ui.my_widgets import *
from configs import default_setting

class A_form():
    def __init__(self, Form, event):
        self.main = Form
        Form.setObjectName("MainWindow")
        Form.resize(511, 700)
        Form.setStyleSheet('QMainWindow {background-color: #242424; color: #E6E6E6;}')
        Form.setMinimumSize(QtCore.QSize(511, 700))
        Form.setMaximumSize(QtCore.QSize(511, 700))
        self.font36 = QtGui.QFont('微軟正黑體', 36)
        self.font16 = QtGui.QFont('微軟正黑體', 16)
        self.font12 = QtGui.QFont('微軟正黑體', 12)
        self.font9 = QtGui.QFont('微軟正黑體', 9)

        """ main """
        self.label_main = QtWidgets.QLabel(Form)
        self.label_main.setGeometry(QtCore.QRect(30, 30, 215, 94))
        self.label_main.setStyleSheet('QLabel {background-image : url("./src/flask.png")}')
        self.label_main.setObjectName("label_main")

        self.label_logo = clickable_label(Form, event)
        self.label_logo.setGeometry(QtCore.QRect(440, 10, 60, 60))
        self.label_logo.setStyleSheet('QLabel {background-image : url("./src/51.png")}')
        self.label_logo.setObjectName("label_logo")

        self.btn_start = my_btn(Form)
        self.btn_start.setFont(self.font12)
        self.btn_start.setGeometry(QtCore.QRect(400, 90, 91, 31))
        self.btn_start.setObjectName("btn_start")

        self.gb_global = my_gb(Form)
        self.gb_global.setFont(self.font12)
        self.gb_global.setGeometry(QtCore.QRect(260, 30, 121, 94))

        self.edit_global_enable_key = focus_line_edit(self.gb_global, event)
        self.edit_global_enable_key.setFont(self.font9)
        self.edit_global_enable_key.setGeometry(QtCore.QRect(10, 30, 101, 51))
        self.edit_global_enable_key.setAlignment(Qt.AlignCenter)
        self.edit_global_enable_key.setReadOnly(True)

        self.edit_new_config = my_line_edit(Form)
        self.edit_new_config.setFont(self.font12)
        self.edit_new_config.setGeometry(QtCore.QRect(30, 140, 101, 31))
        self.edit_new_config.setAlignment(Qt.AlignCenter)

        self.btn_new_config = my_btn(Form)
        self.btn_new_config.setFont(self.font12)
        self.btn_new_config.setGeometry(QtCore.QRect(150, 140, 91, 31))
        self.btn_new_config.setObjectName("btn_new_config")

        self.combo_config = my_ComboBox(Form)
        self.combo_config.setFont(self.font12)
        self.combo_config.setGeometry(QtCore.QRect(260, 140, 121, 31))
        self.combo_config.setObjectName("combo_config")
        self.combo_config.setEditable(True)
        self.combo_config.lineEdit().setFont(self.font12)
        self.combo_config.lineEdit().setReadOnly(True)
        self.combo_config.lineEdit().setAlignment(Qt.AlignCenter)

        self.btn_save_config = my_btn(Form)
        self.btn_save_config.setFont(self.font12)
        self.btn_save_config.setGeometry(QtCore.QRect(400, 140, 91, 31))
        self.btn_save_config.setObjectName("btn_save_config")

        """ flask """
        self.gb_flask = my_gb(Form)
        self.gb_flask.setFont(self.font12)
        self.gb_flask.setGeometry(QtCore.QRect(40, 190, 431, 161))

        self.edit_flask_key = []
        for i in range(5):
            _edit = focus_line_edit(self.gb_flask, event)
            _edit.setFont(self.font36)
            _edit.setGeometry(QtCore.QRect(30 + 80*i, 30, 51, 71))
            _edit.setAlignment(Qt.AlignCenter)
            _edit.setReadOnly(True)
            self.edit_flask_key.append(_edit)

        self.edit_flask_time = []
        for i in range(5):
            _edit = my_line_edit(self.gb_flask)
            _edit.setFont(self.font16)
            _edit.setGeometry(QtCore.QRect(30 + 80*i, 110, 51, 31))
            _edit.setAlignment(Qt.AlignCenter)
            _edit.setValidator(QDoubleValidator())
            self.edit_flask_time.append(_edit)

        """ buff """
        self.gb_buff = my_gb(Form)
        self.gb_buff.setFont(self.font12)
        self.gb_buff.setGeometry(QtCore.QRect(40, 370, 431, 161))

        self.edit_buff_key = []
        for i in range(5):
            _edit = focus_line_edit(self.gb_buff, event)
            _edit.setFont(self.font36)
            _edit.setGeometry(QtCore.QRect(30 + 80*i, 30, 51, 71))
            _edit.setAlignment(Qt.AlignCenter)
            _edit.setReadOnly(True)
            self.edit_buff_key.append(_edit)

        self.edit_buff_time = []
        for i in range(5):
            _edit = my_line_edit(self.gb_buff)
            _edit.setFont(self.font16)
            _edit.setGeometry(QtCore.QRect(30 + 80*i, 110, 51, 31))
            _edit.setAlignment(Qt.AlignCenter)
            _edit.setValidator(QDoubleValidator())
            self.edit_buff_time.append(_edit)

        """ trigger """
        self.gb_trigger = my_gb(Form)
        self.gb_trigger.setFont(self.font12)
        self.gb_trigger.setGeometry(QtCore.QRect(40, 550, 431, 121))

        self.edit_trigger_key = []
        for i in range(3):
            _edit = focus_line_edit(self.gb_trigger, event)
            _edit.setFont(self.font16)
            _edit.setGeometry(QtCore.QRect(30 + 130*i, 30, 111, 71))
            _edit.setAlignment(Qt.AlignCenter)
            _edit.setReadOnly(True)
            self.edit_trigger_key.append(_edit)

        """ not ui """
        self.retranslateUi(Form)
        self.init_config_combobox()
        self.load_setting()
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.event_connect(event)

    def event_connect(self, event):
        self.btn_start.clicked.connect(event.btn_start)
        self.btn_new_config.clicked.connect(event.btn_new_config)
        self.edit_new_config.returnPressed.connect(lambda:self.btn_new_config.click())
        self.combo_config.currentIndexChanged.connect(event.combo_config)
        self.btn_save_config.clicked.connect(event.btn_save_config)
        # self.edit_channel.editingFinished.connect(event.edit_channel)
        # self.cb_optional.stateChanged.connect(event.cb_optional)
        # self.cb_on_top.stateChanged.connect(event.cb_on_top)
        # self.cb_avoid_crosshair.stateChanged.connect(event.cb_avoid_crosshair)
        # self.sli_alpha.valueChanged.connect(event.sli_alpha)
        # self.cb_show_name.stateChanged.connect(event.cb_show_name)
        # self.btn_re_exec.clicked.connect(event.btn_re_exec)

        # self.bot_login_signal.clicked.connect(self.main.login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "POE自動喝水 V1.0"))
        self.btn_start.setText(_translate("MainWindow", "啟動"))
        self.btn_new_config.setText(_translate("MainWindow", "新增設定"))
        self.btn_save_config.setText(_translate("MainWindow", "儲存設定"))
        self.gb_global.setTitle(_translate("MainWindow", "啟動快捷鍵"))
        self.edit_global_enable_key.setPlaceholderText(_translate("MainWindow", "shift"))
        self.edit_new_config.setPlaceholderText(_translate("MainWindow", "設定檔名稱"))

        self.gb_flask.setTitle(_translate("MainWindow", "藥水按鍵與持續時間"))
        self.edit_flask_key[0].setPlaceholderText(_translate("MainWindow", "1"))
        self.edit_flask_time[0].setPlaceholderText(_translate("MainWindow", "4.8"))

        self.gb_buff.setTitle(_translate("MainWindow", "增益按鍵與持續時間"))
        self.edit_buff_key[0].setPlaceholderText(_translate("MainWindow", "q"))
        self.edit_buff_time[0].setPlaceholderText(_translate("MainWindow", "8.7"))

        self.gb_trigger.setTitle(_translate("MainWindow", "觸發按鍵(無設定則自動使用)"))

    def init_config_combobox(self):
        self.combo_config.addItems(self.main.config_list)

    def enable_edit(self, enable, fonction='all'):
        if fonction.startswith('a') and enable == False:
            self.btn_start.setEnabled(enable)
            self.gb_global.setEnabled(enable)
            self.gb_flask.setEnabled(enable)
            self.gb_buff.setEnabled(enable)
            self.gb_trigger.setEnabled(enable)
        else:
            self.btn_start.setEnabled(enable)
            self.gb_global.setEnabled(not self.main.is_working())
            self.gb_flask.setEnabled(not self.main.is_working())
            self.gb_buff.setEnabled(not self.main.is_working())
            self.gb_trigger.setEnabled(not self.main.is_working())

    def new_config(self, config_name):
        self.edit_new_config.setText('')
        self.enable_edit(True)
        self.combo_config.addItem(config_name)

    def load_setting(self):
        config_name = self.main.config_name
        if config_name == '':
            self.enable_edit(False)
        else:
            global_enable_key = self.main.from_setting('global', 'key', 'str')
            flask_key_list = self.main.from_setting('flask', 'key', 'list')
            flask_time_list = self.main.from_setting('flask', 'time', 'list')
            buff_key_list = self.main.from_setting('buff', 'key', 'list')
            buff_time_list = self.main.from_setting('buff', 'time', 'list')
            trigger_key_list = self.main.from_setting('trigger', 'key', 'list')

            i = self.combo_config.findText(config_name)
            self.combo_config.setCurrentIndex(i)

            for i, key in enumerate(flask_key_list):
                self.edit_flask_key[i].setText(key)
            for i, Dtime in enumerate(flask_time_list):
                self.edit_flask_time[i].setText(Dtime)
            for i, key in enumerate(buff_key_list):
                self.edit_buff_key[i].setText(key)
            for i, Dtime in enumerate(buff_time_list):
                self.edit_buff_time[i].setText(Dtime)
            for i, key in enumerate(trigger_key_list):
                self.edit_trigger_key[i].setText(key)

            self.edit_global_enable_key.setText(global_enable_key)

            self.enable_edit(True, '')