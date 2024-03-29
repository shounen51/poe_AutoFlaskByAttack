# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets

from ui.my_widgets import *
from configs import default_setting
from src.logo_png import logo_png
from src.flask_png import flask_png
from utils.utils import display_image, now_version

class A_form():
    def __init__(self, Form, event):
        self.main = Form
        Form.setObjectName("MainWindow")
        Form.resize(511, 760)
        Form.setStyleSheet('QMainWindow {background-color: #242424; color: #E6E6E6;}')
        Form.setMinimumSize(QtCore.QSize(511, 760))
        Form.setMaximumSize(QtCore.QSize(511, 760))
        self.font36 = QtGui.QFont('微軟正黑體', 36)
        self.font16 = QtGui.QFont('微軟正黑體', 16)
        self.font12 = QtGui.QFont('微軟正黑體', 12)
        self.font9 = QtGui.QFont('微軟正黑體', 9)

        """ main """
        self.label_main = flask_label(Form, event)
        self.label_main.setGeometry(QtCore.QRect(30, 30, 215, 94))
        display_image(self.label_main, flask_png)
        # self.label_main.setStyleSheet('QLabel {background-image : url("./src/flask.png")}')
        self.label_main.setObjectName("label_main")

        self.label_ver = my_label(Form)
        self.label_ver.setGeometry(QtCore.QRect(10, 5, 150, 20))
        self.label_ver.setFont(self.font9)
        self.label_ver.setObjectName("label_ver")

        self.label_logo = clickable_label(Form, event)
        self.label_logo.setGeometry(QtCore.QRect(440, 10, 60, 60))
        display_image(self.label_logo, logo_png)
        self.label_logo.setObjectName("label_logo")

        self.btn_start = my_btn(Form)
        self.btn_start.setFont(self.font12)
        self.btn_start.setGeometry(QtCore.QRect(390, 90, 91, 31))
        self.btn_start.setObjectName("btn_start")

        self.gb_global = my_gb(Form)
        self.gb_global.setFont(self.font12)
        self.gb_global.setGeometry(QtCore.QRect(260, 30, 121, 94))

        self.edit_global_enable_key = focus_line_edit(self.gb_global, event, 'global', 0)
        self.edit_global_enable_key.setFont(self.font12)
        self.edit_global_enable_key.setGeometry(QtCore.QRect(10, 30, 101, 51))
        self.edit_global_enable_key.setAlignment(Qt.AlignCenter)
        self.edit_global_enable_key.setReadOnly(True)

        self.sets_index_labels = []
        for i in range(5):
            _label = my_label(Form)
            _label.setGeometry(QtCore.QRect(54 + 38*i, 120, 20, 20))
            _label.setFont(self.font9)
            _label.setText("")
            self.sets_index_labels.append(_label)

        self.edit_new_config = my_line_edit(Form)
        self.edit_new_config.setFont(self.font12)
        self.edit_new_config.setGeometry(QtCore.QRect(30, 140, 251, 31))
        self.edit_new_config.setAlignment(Qt.AlignCenter)

        self.btn_new_config = my_btn(Form)
        self.btn_new_config.setFont(self.font12)
        self.btn_new_config.setGeometry(QtCore.QRect(290, 140, 91, 31))
        self.btn_new_config.setObjectName("btn_new_config")

        self.btn_rename_config = my_btn(Form)
        self.btn_rename_config.setFont(self.font12)
        self.btn_rename_config.setGeometry(QtCore.QRect(390, 140, 91, 31))
        self.btn_rename_config.setObjectName("btn_rename_config")

        self.combo_config = my_ComboBox(Form)
        self.combo_config.setFont(self.font12)
        self.combo_config.setGeometry(QtCore.QRect(30, 180, 351, 31))
        self.combo_config.setObjectName("combo_config")
        self.combo_config.setEditable(True)
        self.combo_config.lineEdit().setFont(self.font12)
        self.combo_config.lineEdit().setReadOnly(True)
        self.combo_config.lineEdit().setAlignment(Qt.AlignCenter)

        # self.combo_line_edit = my_line_edit(Form)
        # self.combo_line_edit.setFont(self.font12)
        # self.combo_line_edit.setAlignment(Qt.AlignCenter)
        # self.combo_config.setLineEdit(self.combo_line_edit)

        self.btn_save_config = my_btn(Form)
        self.btn_save_config.setFont(self.font12)
        self.btn_save_config.setGeometry(QtCore.QRect(390, 180, 91, 31))
        self.btn_save_config.setObjectName("btn_save_config")

        self.btn_del_config = my_btn(Form)
        self.btn_del_config.setFont(self.font12)
        self.btn_del_config.setGeometry(QtCore.QRect(390, 720, 91, 31))
        self.btn_del_config.setObjectName("btn_del_config")

        self.btn_floating_win = my_btn(Form)
        self.btn_floating_win.setFont(self.font12)
        self.btn_floating_win.setGeometry(QtCore.QRect(30, 720, 91, 31))
        self.btn_floating_win.setObjectName("btn_floating_win")

        """ flask """
        self.gb_flask = my_gb(Form)
        self.gb_flask.setFont(self.font12)
        self.gb_flask.setGeometry(QtCore.QRect(40, 230, 431, 161))

        self.edit_flask_key = []
        for i in range(5):
            _edit = focus_line_edit(self.gb_flask, event, 'flask', i)
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
        self.gb_buff.setGeometry(QtCore.QRect(40, 410, 431, 161))

        self.edit_buff_key = []
        for i in range(5):
            _edit = focus_line_edit(self.gb_buff, event, 'buff', i)
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
        self.gb_trigger.setGeometry(QtCore.QRect(40, 590, 431, 121))

        self.edit_trigger_key = []
        for i in range(3):
            _edit = focus_line_edit(self.gb_trigger, event, 'trigger', i)
            _edit.setFont(self.font16)
            _edit.setGeometry(QtCore.QRect(30 + 130*i, 30, 111, 71))
            _edit.setAlignment(Qt.AlignCenter)
            _edit.setReadOnly(True)
            self.edit_trigger_key.append(_edit)

        """ not ui """
        self.retranslateUi(Form)
        self.init_config_combobox()
        self.load_setting(event)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.event_connect(event)
        self.choose_set(0)

    def event_connect(self, event):
        self.btn_start.clicked.connect(event.btn_start)
        self.btn_new_config.clicked.connect(event.btn_new_config)
        self.edit_new_config.returnPressed.connect(lambda:self.btn_new_config.click())
        self.combo_config.currentIndexChanged.connect(event.combo_config)
        self.btn_rename_config.clicked.connect(event.btn_rename_config)
        self.btn_save_config.clicked.connect(event.btn_save_config)
        self.btn_del_config.clicked.connect(event.btn_del_config)
        self.btn_floating_win.clicked.connect(event.btn_floating_win)
        
        self.edit_flask_time[0].editingFinished.connect(lambda:event.time_edited(self.edit_flask_time[0]))
        self.edit_flask_time[1].editingFinished.connect(lambda:event.time_edited(self.edit_flask_time[1]))
        self.edit_flask_time[2].editingFinished.connect(lambda:event.time_edited(self.edit_flask_time[2]))
        self.edit_flask_time[3].editingFinished.connect(lambda:event.time_edited(self.edit_flask_time[3]))
        self.edit_flask_time[4].editingFinished.connect(lambda:event.time_edited(self.edit_flask_time[4]))
        self.edit_buff_time[0].editingFinished.connect(lambda:event.time_edited(self.edit_buff_time[0]))
        self.edit_buff_time[1].editingFinished.connect(lambda:event.time_edited(self.edit_buff_time[1]))
        self.edit_buff_time[2].editingFinished.connect(lambda:event.time_edited(self.edit_buff_time[2]))
        self.edit_buff_time[3].editingFinished.connect(lambda:event.time_edited(self.edit_buff_time[3]))
        self.edit_buff_time[4].editingFinished.connect(lambda:event.time_edited(self.edit_buff_time[4]))
        # self.cb_optional.stateChanged.connect(event.cb_optional)
        # self.cb_on_top.stateChanged.connect(event.cb_on_top)
        # self.cb_avoid_crosshair.stateChanged.connect(event.cb_avoid_crosshair)
        # self.sli_alpha.valueChanged.connect(event.sli_alpha)
        # self.cb_show_name.stateChanged.connect(event.cb_show_name)
        # self.btn_re_exec.clicked.connect(event.btn_re_exec)

        # self.bot_login_signal.clicked.connect(self.main.login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "POE自動喝水"))
        self.label_ver.setText(_translate("MainWindow", now_version()))
        self.btn_start.setText(_translate("MainWindow", "啟動"))
        self.btn_new_config.setText(_translate("MainWindow", "新增設定"))
        self.btn_rename_config.setText(_translate("MainWindow", "修改名稱"))
        self.btn_save_config.setText(_translate("MainWindow", "儲存設定"))
        self.btn_del_config.setText(_translate("MainWindow", "刪除設定"))
        self.btn_floating_win.setText(_translate("MainWindow", "關閉懸浮"))
        self.gb_global.setTitle(_translate("MainWindow", "啟動快捷鍵"))
        # self.edit_global_enable_key.setPlaceholderText(_translate("MainWindow", "f2"))
        self.edit_new_config.setPlaceholderText(_translate("MainWindow", "設定檔名稱"))

        self.gb_flask.setTitle(_translate("MainWindow", "藥水按鍵與持續時間"))
        # self.edit_flask_key[0].setPlaceholderText(_translate("MainWindow", "1"))
        # self.edit_flask_time[0].setPlaceholderText(_translate("MainWindow", "4.8"))

        self.gb_buff.setTitle(_translate("MainWindow", "增益按鍵與持續時間"))
        # self.edit_buff_key[0].setPlaceholderText(_translate("MainWindow", "q"))
        # self.edit_buff_time[0].setPlaceholderText(_translate("MainWindow", "8.7"))

        self.gb_trigger.setTitle(_translate("MainWindow", "觸發按鍵(無設定則自動使用)"))

    def init_config_combobox(self):
        self.combo_config.addItems(self.main.config_list)

    def enable_edit(self, enable, fonction='all'):
        if fonction.startswith('a') and enable == False:
            self.btn_start.setEnabled(enable)
            # self.btn_new_config.setEnabled(enable)
            self.combo_config.setEnabled(enable)
            self.gb_global.setEnabled(enable)
            self.gb_flask.setEnabled(enable)
            self.gb_buff.setEnabled(enable)
            self.gb_trigger.setEnabled(enable)
            self.btn_rename_config.setEnabled(enable)
            self.btn_del_config.setEnabled(enable)
            self.btn_save_config.setEnabled(enable)
        else:
            self.btn_start.setEnabled(enable)
            # self.btn_new_config.setEnabled(self.main.is_editOK())
            self.btn_rename_config.setEnabled(self.main.is_editOK())
            self.btn_del_config.setEnabled(self.main.is_editOK())
            self.btn_save_config.setEnabled(self.main.is_editOK())
            self.combo_config.setEnabled(self.main.is_editOK())
            self.gb_global.setEnabled(self.main.is_editOK())
            self.gb_flask.setEnabled(self.main.is_editOK())
            self.gb_buff.setEnabled(self.main.is_editOK())
            self.gb_trigger.setEnabled(self.main.is_editOK())

    def choose_set(self, index):
        for i in range(5):
            self.sets_index_labels[i].setStyleSheet('QLabel {background-color: #242424; color: #E6E6E6;}')
            self.sets_index_labels[i].setText("^" if self.main.set_enabel_status[i] else "")
        self.sets_index_labels[index].setText("^")
        self.sets_index_labels[index].setStyleSheet('QLabel {background-color: #242424; color: #20E620;}')        

    def new_config(self, config_name):
        self.edit_new_config.setText('')
        self.enable_edit(True)
        self.combo_config.addItem(config_name)

    def load_setting(self, event):
        config_name = self.main.config_name
        if config_name == '':
            self.enable_edit(False)
        else:
            set_index = event.current_set_index 
            global_enable_key = self.main.from_setting('global', 'key', 'str')
            flask_key_list = self.main.from_setting('flask', f'key{set_index}', 'list')
            flask_time_list = self.main.from_setting('flask', f'time{set_index}', 'list')
            buff_key_list = self.main.from_setting('buff', f'key{set_index}', 'list')
            buff_time_list = self.main.from_setting('buff', f'time{set_index}', 'list')
            trigger_key_list = self.main.from_setting('trigger', f'key{set_index}', 'list')

            i = self.combo_config.findText(config_name)
            self.combo_config.setCurrentIndex(i)

            for i, key in enumerate(flask_key_list):
                self.edit_flask_key[i].setText(key)
                if key == '':
                    self.edit_flask_time[i].setEnabled(False)
                else:
                    self.edit_flask_time[i].setEnabled(True)
            for i, Dtime in enumerate(flask_time_list):
                self.edit_flask_time[i].setText(Dtime)
            for i, key in enumerate(buff_key_list):
                self.edit_buff_key[i].setText(key)
                if key == '':
                    self.edit_buff_time[i].setEnabled(False)
                else:
                    self.edit_buff_time[i].setEnabled(True)
            for i, Dtime in enumerate(buff_time_list):
                self.edit_buff_time[i].setText(Dtime)
            for i, key in enumerate(trigger_key_list):
                self.edit_trigger_key[i].setText(key)

            self.edit_global_enable_key.setText(global_enable_key)

            self.enable_edit(True, '')