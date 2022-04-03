#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/5
from pywindow import Position
from .scene import Scene


class FactionSubmit(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(642, 375, "39558C")
        self._append_rule(642, 376, "ADDFFF")
        self._append_rule(560, 541, "141FB3")
        self._append_rule(720, 541, "047E41")

    def submit(self):
        self._actor.left_click(Position(750, 570))
        self._wait_after_action(times=3)  # wait disappear of banner

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
