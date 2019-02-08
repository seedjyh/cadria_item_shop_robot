#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/7
from pywindow import Position
from .scene import Scene


class BlueprintUpgraded(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(590, 201, "A3C6EC")
        self._append_rule(590, 260, "7FC8FA")
        self._append_rule(590, 643, "40FBC4")

    def exit(self):
        self._window.left_click(Position(636, 674))
        self._wait_after_action()


if __name__ == "__main__":
    pass
