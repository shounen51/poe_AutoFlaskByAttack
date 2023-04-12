import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal
import win32gui

class poe_detector(QThread):
    playing_signal = pyqtSignal(bool)
    def __init__(self, main):
        super().__init__()
        self.main = main
        # self.game = '小算盤' # for debug
        self.game = 'Path of Exile'
        self.this_app = 'POE自動喝水'
        self.float_win = '懸浮視窗'
        self.poe_hWnd = 0
        self.this_hWnd = 0
        self.float_hWnd = 0
        self.this_hWnds = [self.this_hWnd, self.float_hWnd]

    def start(self):
        self.t = threading.Thread(target=self.run,)
        self.t.setDaemon(True)
        self.t.start()

    def catch_self_hWnds(self):
        self.this_hWnd = win32gui.FindWindow(None, self.this_app)
        self.float_hWnd = win32gui.FindWindow(None, self.float_win)
        self.this_hWnds = [self.this_hWnd, self.float_hWnd, self.poe_hWnd]
        print(self.this_hWnds)

    def check_immediately(self):
        now_win = win32gui.GetForegroundWindow()
        return now_win == self.poe_hWnd

    def check_focus_self_or_poe(self):
        now_win = win32gui.GetForegroundWindow()
        return now_win in self.this_hWnds

    def get_poe_rect(self):
        try:
            rect = win32gui.GetWindowRect(self.poe_hWnd)
            return True, rect
        except:
            return False, (0,0,0,0)

    def run(self):
        while 1:
            self.poe_hWnd = win32gui.FindWindow(None, self.game)
            self.this_hWnds = [self.this_hWnd, self.float_hWnd, self.poe_hWnd]
            if self.check_immediately():
                self.playing_signal.emit(True)
            else:
                self.playing_signal.emit(False)
            time.sleep(0.5)
