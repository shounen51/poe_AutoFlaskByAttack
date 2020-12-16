import json
import os
import time
import random
import logging

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.sip

from configs import *

def load_ini(path):
    settting={}
    try:
        with open(path, encoding="utf-8") as file:
            lines = file.read().split('\n')
            lines = [x.rstrip().lstrip() for x in lines]
            lines = [x for x in lines if x and not x.startswith('#') and not x == ""]
        major_key = ""
        for line in lines:
            if line.startswith('['):
                line = line.replace('[', "").replace(']', "")
                settting[line] = {}
                major_key = line
            else:
                detail_key, value = line.split('=')
                settting[major_key][detail_key] = value
        logging.info(settting)
        return True, settting
    except:
        logging.warning("Load setting fail. Load default setting")
        logging.info(default_setting)
        return False, default_setting

def save_ini(path, settting):
    try:
        lines = []
        for major_key in settting.keys():
            lines.append('[' + major_key + ']\n')
            for detail_key in settting[major_key].keys():
                lines.append(detail_key + '=' + settting[major_key][detail_key] + '\n')
            lines.append('\n')
        with open(path, "w", encoding="utf-8") as file:
            file.writelines(lines)
        logging.info('Save setting.')
        return True
    except:
        logging.warning('Save setting failed.')
        return False
