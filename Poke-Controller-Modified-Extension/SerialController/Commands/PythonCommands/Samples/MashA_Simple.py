#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button
from Commands.PythonCommandBase import PythonCommand


# Simple program to mash A button repeatedly
# Aボタンのみを連射する単純なプログラム
class Mash_A_Simple(PythonCommand):
    NAME = 'A連射シンプル'

    def __init__(self):
        super().__init__()

    def do(self):
        print("Aボタンの連射を開始します。停止するにはプログラムを中断してください。")
        while True:
            self.wait(0.5)  # 0.5秒待機
            self.press(Button.A)  # Aボタンを押す