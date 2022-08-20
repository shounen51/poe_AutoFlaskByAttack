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
    v1.5.2
        為了完美觸發將軍戰吼，T改為延遲觸發，T的CD時間強制為0.1，欄位空格填入延遲時間(引導施放時間)
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
import PyQt5.sip

from ui.A import A_form
from ui.floating_win import B_form
from utils.button_event import btn_events
from utils.input_listener import input_listener
from utils.poe_detector import poe_detector
from utils.check_versoin import check_version_thread
from utils.utils import load_config, save_config, load_ini, save_ini, list_ini, base2Qpixmap, display_image
from configs import default_setting
from src.icon_png import icon_png
from src.logo_update_png import logo_update_png

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        myicon = QIcon()
        myicon.addPixmap(base2Qpixmap(icon_png), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(myicon)
        self.PLAYING = False
        self.FLOATING = False
        self.detector = poe_detector(self)
        self.detector.playing_signal.connect(self.set_playing)
        self.SETTING = False
        self.is_setting = lambda: self.SETTING
        self.WORKING = False
        self.MOVEFLOWTING = False
        self.is_movingFloating = lambda: self.FLOATING and self.MOVEFLOWTING
        self.is_working = lambda: self.WORKING and self.detector.check_immediately()
        self.is_editOK = lambda: not self.WORKING
        self.config_list = list_ini('./configs')
        self.config_name = load_ini(self.config_list)
        self.now_config = lambda: self.config_name
        OK, self.setting = load_config(f"./configs/{self.config_name}.ini")
        self.event = btn_events(self)
        self.ui = A_form(self, self.event)
        self.floating_window = B_form(self)
        self.linstener = input_listener(self)
        self.linstener.start()
        self.detector.start()
        self.check_updata = check_version_thread()
        self.check_updata.update_signal.connect(self.need2update)
        self.check_updata.start()

    def showEvent(self, event):
        print('main show')
        self.detector.catch_self_hWnds()

    def setting_key(self, setting):
        self.SETTING=setting

    def setting_config_name(self, name):
        self.config_name = name
        save_ini(name)

    def switch_floating(self):
        self.FLOATING = not self.FLOATING
        if self.FLOATING:
            self.ui.btn_floating_win.setText('關閉懸浮')
            if self.detector.check_focus_self_or_poe():
                self.floating_window.show()
        else:
            self.ui.btn_floating_win.setText('開啟懸浮')
            self.floating_window.close()

    def start_move_floating(self, press=None):
        if press!=None:
            self.MOVEFLOWTING = press
        return self.MOVEFLOWTING

    def start_stop(self, setting={}):
        if not self.WORKING:
            self.linstener.load_and_start(setting)
            self.floating_window.set_working(True)
            if self.PLAYING:
                self.ui.btn_start.setStyleSheet('QPushButton {background-color: #20E620; color: #202020;}')
            else:
                self.ui.btn_start.setStyleSheet('QPushButton {background-color: #F6F620; color: #202020;}')
        else:
            self.floating_window.set_working(False)
            self.ui.btn_start.setStyleSheet('QPushButton {background-color: #E62020; color: #E6E6E6;}')
        self.WORKING = not self.WORKING

    def set_playing(self, play):
        self.PLAYING = play
        if self.WORKING:
            if self.PLAYING:
                self.ui.btn_start.setStyleSheet('QPushButton {background-color: #20E620; color: #202020;}')
            else:
                self.ui.btn_start.setStyleSheet('QPushButton {background-color: #F6F620; color: #202020;}')
        if self.FLOATING and self.detector.check_focus_self_or_poe():
            self.floating_window.show()
        else:
            self.floating_window.close()

    def need2update(self):
        display_image(self.ui.label_logo, logo_update_png)

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

if __name__ == "__main__":
    os.makedirs('./log', exist_ok=True)
    os.makedirs('./configs', exist_ok=True)
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