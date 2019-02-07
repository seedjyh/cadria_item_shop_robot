#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/7
from pywindow import Position
from .scene import Scene


class AdventureLocations(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(29, 40, "F7FFF0")
        self._append_rule(93, 40, "8FF7FF")
        self._append_rule(131, 40, "EFAF79")

    def go_to_regine_one(self):
        self._window.left_click(Position(84, 184))
        self._wait_after_action()

    def select_location(self, index):
        # scroll to most left
        self._window.move_to(Position(402, 365))
        self._window.scroll(vertical=-100)
        self._wait_after_action()
        # scroll to target
        print(">>>>>>>>>>>>>>>>>>>", index)
        for i in range(int(7.5 * index)):
            self._window.scroll(1)
            self._wait_after_action(0.3)
        if index <= 6:
            self._window.left_click(Position(402, 365))
        elif index == 7:  # right boundary for scroll
            self._window.left_click(Position(697, 365))
        elif index == 8:  # right boundary for scroll
            self._window.left_click(Position(1036, 365))
        else:
            print("invalid exploration location %d, should be 0~8" % index)
        self._wait_after_action(2)

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()

if __name__ == "__main__":
    pass
