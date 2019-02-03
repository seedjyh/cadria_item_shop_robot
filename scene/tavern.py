#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
from pywindow import Position
from .scene import Scene


class Tavern(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(41, 33, "3885FE")
        self._append_rule(65, 33, "3885FE")

    def go_to_bank(self):
        self._window.left_click(Position(1123, 393))

    def exit(self):
        self._window.tap_letter("b")  # hotkey: go to Scene Shop


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    scene = Tavern(window_handle)
    if not scene.match():
        print("not tavern!")
        exit()
    scene.go_to_bank()
