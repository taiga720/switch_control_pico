#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand
import time
import os

class ShinyHunting(ImageProcPythonCommand):
    NAME = '色違い厳選'

    def __init__(self, cam):
        super().__init__(cam)

    def do(self):
        while True:
            # ポケモンと遭遇
            self.encounter()

            # Shinyかどうかをチェック
            # if self.is_shiny():
            #     print("Shiny found!")
            #     self.notify("Shiny found!")
            #     break
            # else:
                # リセット
            while self.isContainTemplate('original/ShinyHunting/rugia.png', threshold=0.999, use_gray=False, show_value=True):
                self.reset()

    # 遭遇処理
    def encounter(self):
        # 仮に、Aボタンを押して進む
        self.press(Button.A, wait=1.0)
        # 歩いて遭遇するまで待つ
        # self.wait(2.0)  # 適宜調整

    # 色違いかどうか判定
    def is_shiny(self):
        # 戦闘画面でShinyをチェック
        # ポケモンのスプライトが輝いているかを検出
        # フレーム差分で輝きを検出
        frame = self.camera.readFrame()
        if frame is None or frame.size == 0:
            print("Error: Could not capture frame from camera")
            return False

        # 輝き検出ロジック (簡易版)
        # 実際にはImageProcessingの関数を使って差分を取る
        # ここでは仮にテンプレートマッチングを使う
        try:
            if self.isContainTemplate('Samples/shiny_mark.png', threshold=0.8):
                return True
        except Exception as e:
            print(f"Error in isContainTemplate: {e}")
            return False
        return False

    # ゲームをリセット
    def reset(self):
        # ABXY同時押しでソフトリセット
        self.hold(Button.A)
        self.hold(Button.B)
        self.hold(Button.X)
        self.hold(Button.Y)
        self.holdEnd(Button.A)
        self.holdEnd(Button.B)
        self.holdEnd(Button.X)
        self.holdEnd(Button.Y)

        # タイトル画面まで待つ
        # while not self.isContainTemplate('original/ShinyHunting/title.png', 0.7):
        #     self.wait(0.5)
        
        # 続きから始める
        # continue_template = self.get_filespec('original/ShinyHunting/continue.png', mode='t')
        # if not os.path.exists(continue_template):
        #     raise FileNotFoundError(f"Template file not found: {continue_template}")

        # while not self.isContainTemplate('original/ShinyHunting/continue.png', threshold=0.6, use_gray=False, show_value=True):
        #     self.press(Button.A, wait=0.6)
        #     self.wait(2.0)
        
        # ゲーム画面まで6回Aボタンを押す
        # for _ in range(6):
        #     self.press(Button.A, wait=0.5)