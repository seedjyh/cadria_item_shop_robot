#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/4
from pywindow import Position
from .scene import Scene


class FactionWar(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(240, 347, "CBE6F2")
        self._append_rule(240, 348, "5D839F")

    def go_to_contribute(self):
        self._actor.left_click(Position(344, 603))
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
