from PyQt5.QtCore import QThread, pyqtSignal
from utils.utils import now_version, HTTP_request

class check_version_thread(QThread):
    update_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.url = 'https://raw.githubusercontent.com/shounen51/poe_AutoFlaskByAttack/main/version.ini'

    def run(self):
        now_v = now_version()
        ok, newest_v = HTTP_request(self.url, 'get')
        print(newest_v)
        if ok and now_v != newest_v:
            self.update_signal.emit()
        else:
            print('ok')
