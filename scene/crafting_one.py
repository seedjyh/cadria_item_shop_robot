#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/5
from pywindow import Position
from .scene import Scene, MatchRule


class CraftingOne(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(600, 156, "10244A")
        self._append_rule(600, 157, "7DB3CE")
        self._append_rule(1077, 116, "004BFF")

    def lack_of_resources(self):
        rules = [
            MatchRule(Position(846, 603), "6B4100"),
        ]
        return self.match_with_rules(rules)

    def craft(self):
        self._window.left_click(Position(846, 603))
        self._wait_after_action(times=3)

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
