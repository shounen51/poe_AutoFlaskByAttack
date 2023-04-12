from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class flask_label(QLabel):
    def __init__(self, parent, event):
        QLabel.__init__(self, parent)
        self.event = event
        self.setStyleSheet('QLabel {background-color: #000000; color: #000000;}')
    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            x = e.x()
            index = 0 if x < 50 else 1 if x < 88 else 2 if x < 127 else 3 if x < 167 else 4
            self.event.drink_Bottled_Faith(index)

class clickable_label(QLabel):
    def __init__(self, parent, event):
        QLabel.__init__(self, parent)
        self.event = event
        self.setStyleSheet('QLabel {background-color: #000000; color: #E6E6E6;}')
    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            self.event.logo_click()

class focus_line_edit(QLineEdit):
    def __init__(self, parent, event, _type, index):
        QLineEdit.__init__(self, parent)
        self.type = _type
        self.index = index
        self.event = event
        self.setStyleSheet('QLineEdit {background-color: #000000; color: #E6E6E6;}')
        self.setFocusPolicy(Qt.ClickFocus)
        self.setContextMenuPolicy(Qt.NoContextMenu)

    def focusOutEvent(self, e):
        self.event.focus_out(self)
        self.event.check_set_enable_status()

    def keyPressEvent(self,e):
        if e.key() in [16777234, 16777235, 16777236, 16777237, 16777251]:
            return
        self.event.input_in(self)
    def mousePressEvent(self, e):
        self.event.input_in(self)

class my_ComboBox(QComboBox):
    def __init__(self, parent):
        QComboBox.__init__(self, parent)
        self.parent = parent
        self.setStyleSheet('QComboBox {background-color: #424242; color: #E6E6E6;}')

class my_btn(QPushButton):
    def __init__(self, parent):
        QPushButton.__init__(self, parent)
        self.setStyleSheet('QPushButton {background-color: #424242; color: #E6E6E6;}')

class my_list(QListWidget):
    def __init__(self, parent):
        QListWidget.__init__(self, parent)
        self.setStyleSheet('QListWidget {background-color: #000000; color: #E6E6E6;}')

class my_edit(QTextEdit):
    def __init__(self, parent):
        QTextEdit.__init__(self, parent)
        self.setStyleSheet('QTextEdit {background-color: #000000; color: #E6E6E6;}')

class my_line_edit(QLineEdit):
    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        self.setStyleSheet('QLineEdit {background-color: #000000; color: #E6E6E6;}')
        self.setFocusPolicy(Qt.ClickFocus)
        self.setContextMenuPolicy(Qt.NoContextMenu)

class my_label(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.setStyleSheet('QLabel {background-color: #242424; color: #E6E6E6;}')

class my_rdo(QRadioButton):
    def __init__(self, parent):
        QRadioButton.__init__(self, parent)
        self.setStyleSheet('QRadioButton {color: #E6E6E6;}')

class my_cb(QCheckBox):
    def __init__(self, parent):
        QCheckBox.__init__(self, parent)
        self.setStyleSheet('QCheckBox {background-color: #242424; color: #E6E6E6;}')

class my_widget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setStyleSheet('QWidget {background-color: #FFFFFF; color: #FFFFFF;}')

class my_gb(QGroupBox):
    def __init__(self, parent):
        QGroupBox.__init__(self, parent)
        self.setStyleSheet("QGroupBox{color: #E6E6E6 ;border-color: #242424;}")

class my_slider(QSlider):
    def __init__(self, direction, parent):
        QSlider.__init__(self, direction, parent)
        # self.setStyleSheet("QSlider{color: #E6E6E6 ;border-color: #242424;}")
