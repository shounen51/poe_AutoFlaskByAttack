import json
import time
import sys
from datetime import datetime
import random
import os
import logging

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.sip

from utils.utils import save_ini

class btn_events():
    def __init__(self, main_window):
        self.main = main_window
