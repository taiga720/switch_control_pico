#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import os

from Commands import Sender
from Commands.Keys import KeyPress, Button, Hat, Stick, Direction
from Commands.PythonCommandBase import PythonCommand
from serial.tools import list_ports

class SchoolWarsController(PythonCommand):
    NAME = '学校最強大会周回'

    def __init__(self):
        super().__init__()

    def do(self):
        print("学校最強大会を開始します。")

        while True:
            # A→A→A→Bを繰り返す

            for i in range(3):
                self.press(Button.A)  # Aボタンを押す
                time.sleep(0.5)  # 0.5秒間隔
                self.press(Button.A)  # Aボタンを押す
                time.sleep(0.5)  # 0.5秒休憩

            self.press(Button.B)  # Bボタンを押す
            time.sleep(0.5)  # 0.5秒間隔
            self.press(Button.B)  # Bボタンを押す

            time.sleep(0.5)  # 0.5秒休憩