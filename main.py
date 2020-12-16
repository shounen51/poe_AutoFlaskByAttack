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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.sip
import discord

from ui.A import A_form
from utils.button_event import btn_events
from utils.utils import load_ini, save_ini
from configs import default_setting

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        OK, self.setting = load_ini('./setting.ini')
        self.event = btn_events(self)
        self.ui = A_form(self, self.event)

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
        elif _type == 'int':
            value = int(value)
        return value

    def modfy_setting(self, major_key, detail_key, value):
        self.setting[major_key][detail_key] = str(value)

    def closeEvent(self, event):
        save_ini('./setting.ini', self.setting)

if __name__ == "__main__":
    if not os.path.isdir('./log'):
        os.mkdir('./log')
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('log/last.log', 'w', 'utf-8'), ])

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())