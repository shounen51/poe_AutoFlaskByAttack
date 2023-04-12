import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            print("Infinite loop")
            time.sleep(10)

    def stop(self):
        self._stop_event.set()

# 建立並啟動 MyThread
t = MyThread()
t.start()

# 等待 5 秒後停止 MyThread
time.sleep(2)
t._stop_event = threading.Event()
t._stop_event.set()
# t.join()
print(t.is_alive())