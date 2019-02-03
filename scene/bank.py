#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
from pywindow import Position
from .scene import Scene, MatchRule


class Bank(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(758, 194, "6F95B4")
        self._append_rule(758, 220, "6F95B4")

    def is_maturity(self):
        """
        deposit maturity, time to withdraw.
        :return:
        """
        rules = [
            MatchRule(Position(591, 353), "39A273"),
            MatchRule(Position(591, 355), "39C792"),
        ]
        return self.match_with_rules(rules)

    def is_idle(self):
        """
        no deposit. do save some money.
        :return:
        """
        rules = [
            MatchRule(Position(591, 395), "4D7494"),
        ]
        return self.match_with_rules(rules)

    def withdraw(self):
        self._window.left_click(Position(755, 577))

    def deposit(self):
        self._window.left_click(Position(755, 577))

    def exit(self):
        # press ESCape
        self._window.tap_escape()


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    scene = Bank(window_handle)
    if not scene.match():
        print("not bank!")
        exit()
    print("is bank!")
    if scene.is_idle():
        print("idle!")
        scene.deposit()
    elif scene.is_maturity():
        print("maturity!")
        scene.withdraw()
    else:
        print("shall wait for longer time!")
