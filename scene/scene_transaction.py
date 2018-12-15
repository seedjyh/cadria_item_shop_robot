#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/16
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.area_transaction_right_button import AreaTransactionRightButton


class SceneTransaction(Scene):
    def __init__(self):
        self.__right_button = AreaTransactionRightButton()
        pass

    def match_rules(self, window):
        return [
            MatchRule(Position(1064, 515), Colour("B2D6F7")),
        ]

    def exit(self, window):
        window.move_to(Position(1192, 117))
        window.left_click()

    def tradable(self, window):
        return self.__right_button.get_state(window) == self.__right_button.GREEN

    def trade(self, window):
        self.__right_button.left_click(window)

    def refuse(self, window):
        window.move_to(Position(800, 480))
        window.left_click()


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneTransaction()
    while True:
        if scene.match(window_handle):
            now_position = window_handle.get_position()
            if scene.tradable(window_handle):
                scene.trade(window_handle)
            else:
                scene.refuse(window_handle)
            time.sleep(0.1)
            window_handle.move_to(now_position)
        time.sleep(0.1)
