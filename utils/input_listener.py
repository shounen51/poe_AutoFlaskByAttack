import threading
import time

from pynput import mouse
from pynput import keyboard
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class trigger_move_button(QPushButton):
    def __init__(self, parent):
        QPushButton.__init__(self, parent)

class flaskbuff():
    def __init__(self, key, cdt):
        self.key = key
        self.cdt = cdt
        self.trigger_time = 0

    def trigger(self):
        trigger_time = time.time()
        if trigger_time - self.trigger_time > self.cdt: # not using
            self.trigger_time = trigger_time
            return True
        else:
            return False

    def press(self):
        return self.key

class input_listener():
    def __init__(self, main):
        self.start_move_floating = main.start_move_floating
        self.start_stop = main.event.btn_start
        self.is_working = getattr(main, 'is_working')
        self.is_setting = getattr(main, 'is_setting')
        self.ui = getattr(main, 'ui')

        self.btn_signal = trigger_move_button(main)
        self.btn_signal.setGeometry(QRect(0, 0, 0, 0))
        self.btn_signal.clicked.connect(main.event.change_floating_border)

        self.keyboard = keyboard.Controller()
        self.mouse_listener = mouse.Listener(on_move = self.mouse_on_move, on_click = self.mouse_on_click, on_scroll = self.mouse_on_scroll)
        self.keyboard_listener = keyboard.Listener(on_press = self.keyboard_on_press, on_release = self.keyboard_on_release)

        self.AUTO = False
        self.MOUSE_MAIN_SCREEN = True
        self.TRIGGER_FLAG = False
        self.last_button = ''
        self.switch_button = ''
        self.trigger_button = []
        self.buff = []

    def button_regularization(self, btn):
        return str(btn).split('.')[-1].replace("'",'')

    def button_unregularization(self, btn):
        if len(btn) > 1:
            if btn in ['left', 'right', 'x1', 'x2', 'middle']:
                return 'Button.' + btn
            else:
                return 'Key.' + btn
        else:
            return btn

    def get_last(self):
        _temp = self.last_button
        self.last_button = ''
        return _temp

    def load_and_start(self, setting):
        switch = setting['switch']
        flask = setting['flask_key']
        flask_time = setting['flask_time']
        buff = setting['buff_key']
        buff_time = setting['buff_time']
        trigger = setting['trigger_key']
        self.buff.clear()
        self.switch_button = switch
        for i, key in enumerate(flask):
            if flask_time[i] != '':
                self.buff.append(flaskbuff(key, float(flask_time[i])))
        for i, key in enumerate(buff):
            if buff_time[i] != '':
                self.buff.append(flaskbuff(key, float(buff_time[i])))
        self.trigger_button = trigger
        if trigger == ['','','']:
            self.AUTO = True
        else:
            self.AUTO = False

    def mouse_on_move(self, x, y):
        pass
        # if x > 1920:
        #     self.MOUSE_MAIN_SCREEN = False
        # else:
        #     self.MOUSE_MAIN_SCREEN = True


    def mouse_on_click(self, x, y , button, pressed):
        button = self.button_regularization(button)
        if self.is_setting():
            self.last_button = button
        elif button == self.trigger_button and pressed:
            self.TRIGGER_FLAG = False
            self.start_stop()
        elif not self.is_working():
            return
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        # print(button)
        elif button in self.trigger_button:
            if pressed:
                self.TRIGGER_FLAG = True
            else:
                self.TRIGGER_FLAG = False

    def mouse_on_scroll(self, x, y ,dx, dy):
        pass
        # print('scrolled {0} at {1}'.format(qw
        #     'down' if dy < 0 else 'up',
        #     (x, y)))

    def keyboard_on_press(self, button):
        button = self.button_regularization(button)
        if button in ['up', 'down', 'left', 'right']:
            return
        elif button == 'alt_l':
            self.start_move_floating(True)
            self.btn_signal.click()
        elif self.is_setting():
            self.last_button = button
        elif button == self.switch_button:
            self.TRIGGER_FLAG = False
            self.start_stop()
        elif not self.is_working():
            return
        elif button in self.trigger_button:
            self.TRIGGER_FLAG = True

    def keyboard_on_release(self, button):
        button = self.button_regularization(button)
        if button == 'alt_l':
            self.start_move_floating(False)
            self.btn_signal.click()
        if not self.is_working():
            return
        elif button in self.trigger_button:
            self.TRIGGER_FLAG = False

    def start(self):
        self.t = threading.Thread(target=self.run,)
        self.t.setDaemon(True)
        self.t.start()

    def run(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()
        while True:
            if (self.TRIGGER_FLAG or self.AUTO) and self.is_working():
                for buff in self.buff:
                    if buff.trigger():
                        self.keyboard.press(self.button_unregularization(buff.press()))
                        self.keyboard.release(self.button_unregularization(buff.press()))
            time.sleep(0.05)

    def join(self):
        self.t.join()