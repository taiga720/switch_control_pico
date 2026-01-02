#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import os
from Commands import Sender
from Commands.Keys import KeyPress, Button, Hat, Stick, Direction
from serial.tools import list_ports

class DummyBoolVar:
    def __init__(key_press, value):
        key_press.value = value
    def get(key_press):
        return key_press.value

class SchoolWarsController:
    def __init__(key_press):
        # シリアルポートのリストを取得
        ports = list(list_ports.comports())

        # 探したいポート名
        target_port = "COM10"
        if not ports:
            print("利用可能なシリアルポートが見つかりません。")
            return

        print(f"ポート {target_port} を使用します。")

        # Senderを初期化
        is_show_serial = DummyBoolVar(False)
        sender = Sender.Sender(is_show_serial=is_show_serial)

        # シリアル接続を開く
        if not sender.openSerial(10, "", 9600):  # COM1 から始まるので +1
            print("シリアル接続に失敗しました。")
            return

        print("シリアル接続成功。")

        # KeyPressを初期化
        key_press = KeyPress(sender)

        print("学校最強大会を開始します。Ctrl+Cで停止。")
        try:
            while True:
                # A→A→A→Bを繰り返す
                for i in range(3):
                    key_press.input(Button.A)  # Aボタンを押す
                    time.sleep(0.5)  # 0.5秒間隔
                    key_press.inputEnd(Button.A)  # Aボタンを押す
                    time.sleep(0.5)  # 0.5秒休憩

                key_press.input(Button.B)  # Bボタンを押す
                time.sleep(0.5)  # 0.5秒間隔
                key_press.inputEnd(Button.B)  # Bボタンを押す

                time.sleep(0.5)  # 0.5秒休憩
        except KeyboardInterrupt:
            print("停止しました。")
        finally:
            sender.closeSerial()
            print("シリアル接続を閉じました。")        

if __name__ == "__main__":
    app = SchoolWarsController()