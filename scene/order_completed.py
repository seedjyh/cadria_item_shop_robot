#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/6
from pywindow import Position
from .scene import Scene


class OrderCompleted(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(357, 254, "FFFFFF")
        self._append_rule(928, 254, "FFFFFF")
        self._append_rule(645, 394, "FFFFFF")
        self._append_rule(645, 617, "047F42")

    def exit(self):
        self._actor.left_click(Position(643, 652))
        self._wait_after_action()


if __name__ == "__main__":
    pass
