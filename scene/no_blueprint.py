#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/8
from pywindow import Position
from .scene import Scene


class NoBlueprint(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(628, 179, "BDD7E7")
        self._append_rule(628, 181, "93BDE5")
        self._append_rule(628, 538, "96FEE4")

    def exit(self):
        self._actor.left_click(Position(628, 569))
        self._wait_after_action()


if __name__ == "__main__":
    pass
