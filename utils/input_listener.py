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
            return True, self.cdt
        else:
            return False, self.cdt - (trigger_time - self.trigger_time)

    def press(self):
        return self.key

class input_listener():
    def __init__(self, main):
        self.start_move_floating = main.start_move_floating
        self.start_stop = main.event.btn_start
        self.is_working = getattr(main, 'is_working')
        self.is_setting = getattr(main, 'is_setting')
        self.ui = getattr(main, 'ui')

        self.con = threading.Condition()
        self.btn_signal = trigger_move_button(main)
        self.btn_signal.setGeometry(QRect(0, 0, 0, 0))
        self.btn_signal.clicked.connect(main.event.change_floating_border)

        self.keyboard = keyboard.Controller()
        self.mouse_listener = mouse.Listener(on_move = self.mouse_on_move, on_click = self.mouse_on_click, on_scroll = self.mouse_on_scroll)
        self.keyboard_listener = keyboard.Listener(on_press = self.keyboard_on_press, on_release = self.keyboard_on_release)

        self.MOUSE_MAIN_SCREEN = True
        self.last_button = ''
        self.switch_button = ''
        self.sets = [{"trigger_button":[], "buff":[]} for _ in range(5)]
        self.trigger_set_index = [] # for notify loop thread which set is triggered
        self.auto_sets = []
        self.t_auto = threading.Thread(target=self.run_auto,)

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
        flasks = setting['flask_key']
        flask_times = setting['flask_time']
        buffs = setting['buff_key']
        buff_times = setting['buff_time']
        triggers = setting['trigger_key']
        self.switch_button = switch
        self.auto_sets.clear()
        if self.t_auto.is_alive():
            self.t_auto._stop_event = threading.Event()
            self.t_auto._stop_event.set()
        for set_index, set in enumerate(self.sets):
            set["buff"].clear()
            set["trigger_button"].clear()
            # set["buff"] = [flaskbuff(key, float(flask_times[set_index][f_index])) for f_index, key in enumerate(flasks[set_index]) if flask_times[set_index][f_index] != '']
            for f_index, key in enumerate(flasks[set_index]):
                if flask_times[set_index][f_index] != '':
                    set["buff"].append(flaskbuff(key, float(flask_times[set_index][f_index])))
            for b_index, key in enumerate(buffs[set_index]):
                if buff_times[set_index][b_index] != '':
                    set["buff"].append(flaskbuff(key, float(buff_times[set_index][b_index])))
            for t_index, key in enumerate(triggers[set_index]):
                if key != '':
                    set["trigger_button"].append(key)
            if len(set["trigger_button"]) == 0 and len(set["buff"]) > 0: self.auto_sets.append(set)
        if len(self.auto_sets) > 0:
            self.t_auto = threading.Thread(target=self.run_auto,)
            self.t_auto.setDaemon(True)
            self.t_auto.start()

    def mouse_on_move(self, x, y):
        pass
        # if x > 1920:
        #     self.MOUSE_MAIN_SCREEN = False
        # else:
        #     self.MOUSE_MAIN_SCREEN = True


    def mouse_on_click(self, x, y , button, pressed):
        button = self.button_regularization(button)
        trigger_buttons = [btn for set in self.sets for btn in set["trigger_button"]]
        if self.is_setting():
            self.last_button = button
        elif button == trigger_buttons and pressed:
            self.start_stop()
        elif not self.is_working():
            return
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        # print(button)
        elif button in trigger_buttons:
            if pressed:
                self.trigger_set_index = [i for i ,set in enumerate(self.sets) for btn in set["trigger_button"] if btn == button]
                with self.con:
                    self.con.notify()

    def mouse_on_scroll(self, x, y ,dx, dy):
        pass
        # print('scrolled {0} at {1}'.format(qw
        #     'down' if dy < 0 else 'up',
        #     (x, y)))

    def keyboard_on_press(self, button):
        button = self.button_regularization(button)
        trigger_buttons = [btn for set in self.sets for btn in set["trigger_button"]]
        if button in ['up', 'down', 'left', 'right']:
            return
        elif button == 'alt_l':
            self.start_move_floating(True)
            self.btn_signal.click()
        elif self.is_setting():
            self.last_button = button
        elif button == self.switch_button:
            self.start_stop()
        elif not self.is_working():
            return
        elif button in trigger_buttons:
            self.trigger_set_index = [i for i ,set in enumerate(self.sets) for btn in set["trigger_button"] if btn == button]
            with self.con:
                self.con.notify()

    def keyboard_on_release(self, button):
        button = self.button_regularization(button)
        if button == 'alt_l':
            self.start_move_floating(False)
            self.btn_signal.click()
        if not self.is_working():
            return

    def start(self):
        self.t = threading.Thread(target=self.run,)
        self.t.setDaemon(True)
        self.t.start()

    def run(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()
        while True:
            self.con.acquire()
            self.con.wait()
            for set_index in self.trigger_set_index:
                for buff in self.sets[set_index]["buff"]:
                    if self.is_working():
                        if buff.trigger()[0]:
                            self.keyboard.press(self.button_unregularization(buff.press()))
                            self.keyboard.release(self.button_unregularization(buff.press()))

    def run_auto(self):
        while True:
            sleep_min = 1
            for auto_set in self.auto_sets:
                for buff in auto_set["buff"]:
                    if self.is_working():
                        TRIGGER, sleep_time = buff.trigger()
                        if sleep_time < sleep_min: sleep_min = sleep_time
                        if TRIGGER:
                            self.keyboard.press(self.button_unregularization(buff.press()))
                            self.keyboard.release(self.button_unregularization(buff.press()))
            time.sleep(sleep_min)

    def join(self):
        self.t.join()