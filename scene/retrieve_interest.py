#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/4
from pywindow import Position
from .scene import Scene


class RetrieveInterest(Scene):
    """
    Scene appears after withdraw money from bank.
    """
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(640, 290, "47659F")
        self._append_rule(640, 335, "60FFFF")

    def exit(self):
        self._window.left_click(Position(630, 150))
        self._wait_after_action()


if __name__ == "__main__":
    pass
