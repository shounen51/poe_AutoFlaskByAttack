import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal
import win32gui

class poe_detector(QThread):
    playing_signal = pyqtSignal(bool)
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.win = 0
        # self.game = '小算盤'
        self.game = 'Path of Exile'

    def start(self):
        self.t = threading.Thread(target=self.run,)
        self.t.setDaemon(True)
        self.t.start()

    def check_immediately(self):
        now_win = win32gui.GetForegroundWindow()
        return now_win == self.win

    def run(self):
        while 1:
            self.win = win32gui.FindWindow(None, self.game)
            if self.win == 0:
                self.main.set_playing(False)
                self.win = win32gui.FindWindow(None, self.game)
                time.sleep(0.05)
            if self.check_immediately():
                self.playing_signal.emit(True)
                # self.main.set_playing(True)
            else:
                self.playing_signal.emit(False)
                # self.main.set_playing(False)
            time.sleep(0.05)
