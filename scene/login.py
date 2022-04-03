#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/12

from pywindow import Position
from .scene import Scene


class Login(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(592, 489, "356399")
        self._append_rule(592, 490, "63B0DF")
        self._append_rule(592, 602, "080CA8")
        self._append_rule(690, 602, "017437")

    def exit(self):
        self._actor.left_click(Position(722, 631))


if __name__ == "__main__":
    pass
