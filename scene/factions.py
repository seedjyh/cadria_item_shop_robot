#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/5
from pywindow import Position
from .scene import Scene


class Factions(Scene):
    """
    Scene with 3 factions' icons, the left, the middle, the right.
    """
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(354, 152, "628DB3")
        self._append_rule(642, 152, "628DB3")
        self._append_rule(930, 152, "628DB3")

    def go_to_faction(self, index):
        print("from Factions, going to faction, index=", index)
        if index < 0 or index >= 3:
            raise Exception("index exceed boundary [0, 2]")
        self._actor.left_click(Position(354 + 288 * index, 160))
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
