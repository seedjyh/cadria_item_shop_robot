#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/12

from pywindow import Position
from .scene import Scene


class Activity(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(622, 75, "3F6081")
        self._append_rule(622, 81, "10244A")
        self._append_rule(978, 614, "B1CDE3")
        self._append_rule(978, 615, "46678E")
        self._append_rule(1143, 118, "0049FF")

    def exit(self):
        self._window.left_click(Position(1143, 118))


if __name__ == "__main__":
    pass
