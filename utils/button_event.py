import json
import time
import sys
from datetime import datetime
import random
import os
import logging

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.utils import save_config
from configs import default_setting

class btn_events():
    def __init__(self, main_window):
        self.main = main_window

    def btn_new_config(self):
        file_name = self.main.ui.edit_new_config.text()
        if file_name == '' or file_name in self.main.config_list:
            return
        self.main.new_config(file_name)

    def combo_config(self):
        config_name = self.main.ui.combo_config.currentText()
        self.main.change_config(config_name)

    def btn_save_config(self):
        global_enable = self.main.ui.cb_global.isChecked()
        global_key = self.main.ui.edit_global_enable_key.text()
        flask_key = take_text(self.main.ui.edit_flask_key)
        flask_time = take_text(self.main.ui.edit_flask_time)
        buff_key = take_text(self.main.ui.edit_buff_key)
        buff_time = take_text(self.main.ui.edit_buff_time)
        trigger = take_text(self.main.ui.edit_trigger_key)
        self.main.modfy_setting('global', 'enable', global_enable)
        self.main.modfy_setting('global', 'key', global_key)
        self.main.modfy_setting('flask', 'key', flask_key)
        self.main.modfy_setting('flask', 'time', flask_time)
        self.main.modfy_setting('buff', 'key', buff_key)
        self.main.modfy_setting('buff', 'time', buff_time)
        self.main.modfy_setting('trigger', 'key', trigger)
        save_config(f"./configs/{self.main.config_name}.ini", self.main.setting)


def take_text(edit_list):
    _list = []
    for edit in edit_list:
        _list.append(edit.text())
    return _list