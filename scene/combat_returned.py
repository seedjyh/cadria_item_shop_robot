#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/6
from pywindow import Position
from scene.repair_item import RepairItem
from scene.utils import exit_if_match
from .scene import Scene


class CombatReturned(Scene):
    """
    The result of combat such as Success or Fail.
    press 'F' to repair items of heroes if necessary.
    """
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(453, 103, "FEFFF6")
        self._append_rule(823, 103, "FEFFF6")
        self._append_rule(1130, 103, "008DFF")

    def exit(self):
        self._window.tap_letter("f")
        self._wait_after_action()
        exit_if_match(RepairItem, self._window)
        self._window.left_click(Position(1146, 115))
        self._wait_after_action()


if __name__ == "__main__":
    pass
