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

from utils.utils import save_config, display_image
from configs import default_setting
from src.floating_win_on import floating_win_on
from src.floating_win_off import floating_win_off
from src.moving_floating_on import moving_floating_on
from src.moving_floating_off import moving_floating_off

class btn_events():
    def __init__(self, main_window):
        self.Bottled_Faith = [3,3,3,3,3]
        self.main = main_window
        self.browser = webbrowser.get('windows-default')

    """ 懸浮視窗事件 """
    def change_floating_border(self):
        press = self.main.start_move_floating()
        if press:
            if self.main.WORKING:
                display_image(self.main.floating_window.label_icon, moving_floating_on)
            else:
                display_image(self.main.floating_window.label_icon, moving_floating_off)
        else:
            if self.main.WORKING:
                display_image(self.main.floating_window.label_icon, floating_win_on)
            else:
                display_image(self.main.floating_window.label_icon, floating_win_off)

    """ 設定按鍵事件 """
    def focus_out(self, edit):
        edit.setStyleSheet('QLineEdit {background-color: #000000; color: #E6E6E6;}')
        self.main.setting_key(False)

    def input_in(self, edit):
        if self.main.is_working():
            return
        elif self.main.is_setting():
            key = self.main.linstener.get_last()
            if key == 'delete':
                edit.setText('')
                if edit.type.startswith('f'): # flask
                    self.main.ui.edit_flask_time[edit.index].setText('')
                    self.main.ui.edit_flask_time[edit.index].setEnabled(False)
                elif edit.type.startswith('b'): # buff
                    self.main.ui.edit_buff_time[edit.index].setText('')
                    self.main.ui.edit_buff_time[edit.index].setEnabled(False)
            elif key != 'esc':
                if edit.type.startswith('f'):
                    if len(key) == 1:
                        self.main.ui.edit_flask_time[edit.index].setEnabled(True)
                    else:
                        return
                elif edit.type.startswith('b'):
                    if len(key) == 1:
                        self.main.ui.edit_buff_time[edit.index].setEnabled(True)
                    else:
                        return
                edit.setText(key)
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
            self.main.ui.edit_new_config.setText('')
            return
        for c in file_name:
            if c in ['/','\\',':','*','?','"','<','>','|']:
                self.main.ui.edit_new_config.setText('')
                return
        self.main.new_config(file_name)

    def combo_config(self):
        config_name = self.main.ui.combo_config.currentText()
        if config_name == '':
            return
        self.main.change_config(config_name)

    def btn_rename_config(self):
        cb = self.main.ui.combo_config
        config_name = self.main.ui.edit_new_config.text()
        for c in config_name:
            if c in ['/','\\',':','*','?','"','<','>','|']:
                self.main.ui.edit_new_config.setText('')
                return
        if config_name == self.main.now_config() or config_name == '':
            self.main.ui.edit_new_config.setText('')
            return
        try:
            self.main.ui.edit_new_config.setText('')
            old_name = os.path.join('./configs', self.main.now_config() + '.ini')
            new_name = os.path.join('./configs', config_name + '.ini')
            os.rename(old_name, new_name)
            self.main.setting_config_name(config_name)
            cb.setItemText(cb.currentIndex(), config_name)
        except:
            pass

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

    def btn_del_config(self):
        cb = self.main.ui.combo_config
        if cb.count() <= 1:
            return
        config_name = self.main.now_config()
        del_name = os.path.join('./configs', config_name + '.ini')
        try:
            cb.removeItem(cb.currentIndex())
            os.remove(del_name)
        except:
            pass

    def btn_floating_win(self):
        poe_running, rect = self.main.detector.get_poe_rect()
        if poe_running:
            x1, y1, x2, y2 = rect
            w = x2-x1
            h = y2-y1
            fx = int(w*0.328125+x1)
            fy = int(h*0.877777+y1)
            fw = int(100*(w/1920))
            fh = int(100*(h/1080))
            self.main.floating_window.set_rect(fx, fy, fw, fh)
        self.main.switch_floating()

    def time_edited(self, edit):
        if float(edit.text()) < 0.1:
            edit.setText('0.1')

    def logo_click(self):
        self.browser.open_new_tab('https://github.com/shounen51/poe_AutoFlaskByAttack')

    """ 喝水 """
    def drink_Bottled_Faith(self, index):
        pass

def take_text(edit_list):
    _list = []
    for edit in edit_list:
        _list.append(edit.text())
    return _list