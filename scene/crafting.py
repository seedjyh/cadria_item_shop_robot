#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/7
from pywindow import Position
from .scene import Scene, MatchRule


class Item:
    def __init__(self, left_top):
        self.left_top = left_top

    def rules_for_valid(self):
        return [
            MatchRule(self.left_top.add(Position(255, 6)), "D6E7EF"),
        ]

    def click_point(self):
        return self.left_top.add(Position(255, 6))


class Crafting(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(99, 33, "EAF5F5")
        self._append_rule(225, 39, "639ED6")
        self._append_rule(99, 718, "5A92C6")
        self._items = []
        for row in range(3):
            for column in range(3):
                self._items.append(Item(Position(222 + column * 341, 223 + row * 206)))

    def choose_bookmark(self):
        self._window.left_click(Position(97, 479))
        self._wait_after_action()

    def choose_all_types(self):
        self._window.left_click(Position(267, 163))
        self._wait_after_action()

    def valid_item(self, row, column):
        if row < 0 or row >= 3 or column < 0 or column >=3:
            raise Exception("invalid row and column:", row, column)
        return self.match_with_rules(self._items[row * 3 + column].rules_for_valid())

    def choose_item(self, row, column):
        if row < 0 or row >= 3 or column < 0 or column >=3:
            raise Exception("invalid row and column:", row, column)
        self._window.left_click(self._items[row * 3 + column].click_point())
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
