#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/4
from pywindow import Position
from .scene import Scene


class ItemUpgraded(Scene):
    """
    Item upgraded when retrieving crafted item
    """
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(638, 397, "FFFFFF")
        self._append_rule(541, 628, "7EA6FF")
        self._append_rule(748, 678, "0CD079")

    def exit(self):
        self._window.left_click(Position(540, 640))
        self._wait_after_action(times=3)


if __name__ == "__main__":
    pass
