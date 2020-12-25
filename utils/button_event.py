import json
import time
import sys
from datetime import datetime
import random
import os
import logging
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.utils import save_config
from configs import default_setting

class btn_events():
    def __init__(self, main_window):
        self.main = main_window
        self.browser = webbrowser.get('windows-default')

    """ 設置按鈕 """
    def focus_out(self, edit):
        edit.setStyleSheet('QLineEdit {background-color: #000000; color: #E6E6E6;}')
        self.main.setting_key(False)

    def input_in(self, edit):
        if self.main.is_working():
            return
        elif self.main.is_setting():
            key = self.main.linstener.get_last()
            if key != 'esc':
                edit.setText(str(key))
            edit.clearFocus()
        else:
            edit.setStyleSheet('QLineEdit {background-color: #600000; color: #E6E6E6;}')
            self.main.setting_key(True)

    """ 物件事件 """
    def btn_start(self):
        if not self.main.WORKING:
            self.btn_save_config()
            switch = self.main.from_setting('global', 'key', 'str')
            flask_key = self.main.from_setting('flask', 'key', 'list')
            flask_time = self.main.from_setting('flask', 'time', 'list')
            buff_key = self.main.from_setting('buff', 'key', 'list')
            buff_time = self.main.from_setting('buff', 'time', 'list')
            trigger_key = self.main.from_setting('trigger', 'key', 'list')
            setting = {
                'switch':switch,
                'flask_key':flask_key,
                'flask_time':flask_time,
                'buff_key':buff_key,
                'buff_time':buff_time,
                'trigger_key':trigger_key
            }
            self.main.start_stop(setting)
        else:
            self.main.start_stop()
        self.main.ui.enable_edit(True ,'global')

    def btn_new_config(self):
        file_name = self.main.ui.edit_new_config.text()
        if file_name == '' or file_name in self.main.config_list:
            return
        self.main.new_config(file_name)

    def combo_config(self):
        config_name = self.main.ui.combo_config.currentText()
        self.main.change_config(config_name)

    def btn_save_config(self):
        global_key = self.main.ui.edit_global_enable_key.text()
        flask_key = take_text(self.main.ui.edit_flask_key)
        flask_time = take_text(self.main.ui.edit_flask_time)
        buff_key = take_text(self.main.ui.edit_buff_key)
        buff_time = take_text(self.main.ui.edit_buff_time)
        trigger = take_text(self.main.ui.edit_trigger_key)
        self.main.modfy_setting('global', 'key', global_key)
        self.main.modfy_setting('flask', 'key', flask_key)
        self.main.modfy_setting('flask', 'time', flask_time)
        self.main.modfy_setting('buff', 'key', buff_key)
        self.main.modfy_setting('buff', 'time', buff_time)
        self.main.modfy_setting('trigger', 'key', trigger)
        save_config(f"./configs/{self.main.config_name}.ini", self.main.setting)

    def logo_click(self):
        self.browser.open_new_tab('https://github.com/shounen51/poe_AutoFlaskByAttack')

def take_text(edit_list):
    _list = []
    for edit in edit_list:
        _list.append(edit.text())
    return _list