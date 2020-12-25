'''
⠄⠄⠈⣿⠄⠄⠄⢙⢞⢿⣿⢹⢿⣦⢏⣱⢿⠘⣿⣝⠹⢿⣿⡽⣿⣿⣏⣆⢿⣿⡞⠁
⠄⠄⠄⢻⡀⠄⠄⠈⣾⡸⡏⢸⡾⣴⣿⣿⣶⣼⣎⢵⢀⡛⣿⣷⡙⡻⢻⡴⠨⠨⠖⠃
⠄⠄⠄⠈⣧⢀⡴⠊⢹⠁⡇⠈⢣⣿⣿⣿⣿⣦⣿⣷⣜⡳⣝⢧⢃⢣⣼⢁⠘⠆⠄⠄
⠄⠄⠄⠄⢹⡇⠄⣠⠔⠚⣅⠄⢰⣶⣦⣭⣿⣿⣿⡿⠟⠿⣷⡧⠄⣘⣟⣸⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢷⠎⠄⠄⠄⣼⣦⠻⣿⣿⡟⠛⠻⢿⣿⣿⣿⡾⢱⣿⡏⠸⡏⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠸⡄⠄⡄⠄⣿⢧⢗⠌⠻⣇⠿⠿⣸⣿⣿⡟⡐⣿⠟⢰⣇⠇⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣠⡆⠄⠃⢠⠏⣤⢀⢢⡰⣭⣛⡉⠩⠭⡅⣾⢳⡴⡀⢸⣿⡆⠄⠄⠄⠄
⠄⠄⠄⢀⣶⡟⣽⠼⢀⡕⢀⠘⠸⢮⡳⡻⡍⡷⡆⠤⠤⠭⢸⢳⣷⢸⡟⣷⠄⠄⠄⠄
'''
"""[summary]
    V1.0
"""

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("poe_autoflask")
import os
import sys
import time
import logging
import traceback

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.A import A_form
from utils.button_event import btn_events
from utils.input_listener import input_listener
from utils.utils import load_config, save_config, load_ini, save_ini, list_ini
from configs import default_setting

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.SETTING = False
        self.is_setting = lambda: self.SETTING
        self.WORKING = False
        self.is_working = lambda: self.WORKING
        self.config_list = list_ini('./configs')
        self.config_name = load_ini(self.config_list)
        OK, self.setting = load_config(f"./configs/{self.config_name}.ini")
        self.event = btn_events(self)
        self.ui = A_form(self, self.event)
        self.linstener = input_listener(self)
        self.linstener.start()

    def setting_key(self, setting):
        self.SETTING=setting

    def start_stop(self, setting={}):
        if not self.WORKING:
            self.linstener.load_and_start(setting)
            self.ui.btn_start.setStyleSheet('QPushButton {background-color: #20E620; color: #202020;}')
        else:
            self.ui.btn_start.setStyleSheet('QPushButton {background-color: #E62020; color: #E6E6E6;}')
        self.WORKING = not self.WORKING

    def new_config(self, config_name):
        save_config(f"./configs/{config_name}.ini", default_setting)
        self.ui.new_config(config_name)
        self.config_list.append(config_name)
        self.change_config(config_name)

    def change_config(self, config_name):
        self.config_name = config_name
        save_ini(config_name)
        OK, self.setting = load_config(f"./configs/{self.config_name}.ini")
        self.ui.load_setting()

    def from_setting(self, major_key, detail_key, _type='str'):
        try:
            value = self.setting[major_key][detail_key]
        except:
            if major_key in self.setting:
                self.setting[major_key][detail_key] = default_setting[major_key][detail_key]
            else:
                self.setting[major_key] = default_setting[major_key]
            value = self.setting[major_key][detail_key]
        """type"""
        if _type == 'str' or _type == 'string':
            pass
        elif _type == 'bool' or _type == 'boolean':
            if value.startswith('T') or value.startswith('t'):
                value = True
            else:
                value = False
        elif _type == 'list':
            value = value[1:-1]
            value = value.split(',')
        elif _type == 'int':
            value = int(value)
        return value

    def modfy_setting(self, major_key, detail_key, value):
        if type(value) == list:
            v = '['
            v += ','.join(value)
            v += ']'
            self.setting[major_key][detail_key] = v
        else:
            self.setting[major_key][detail_key] = str(value)

    def closeEvent(self, event):
        pass
        # save_config('./setting.ini', self.setting)

if __name__ == "__main__":
    if not os.path.isdir('./log'):
        os.mkdir('./log')
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('log/last.log', 'w', 'utf-8'), ])
    try:
        app = QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())
    except Exception as e:
        error_class = e.__class__.__name__ #取得錯誤類型
        detail = e.args[0] #取得詳細內容
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
        fileName = lastCallStack[0] #取得發生的檔案名稱
        lineNum = lastCallStack[1] #取得發生的行號
        funcName = lastCallStack[2] #取得發生的函數名稱
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
        logging.error(errMsg)