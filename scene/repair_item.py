#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/6
from pywindow import Position
from .scene import Scene


class RepairItem(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(641, 520, "0071DE")
        self._append_rule(527, 543, "070AA3")
        self._append_rule(748, 543, "017337")

    def exit(self):
        self._actor.left_click(Position(755, 576))
        self._wait_after_action()


if __name__ == "__main__":
    pass
