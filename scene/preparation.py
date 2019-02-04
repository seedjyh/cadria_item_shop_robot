#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/4
from pywindow import Position
from .scene import Scene, MatchRule


class Slot:
    def __init__(self, left_top):
        self._left_top = left_top

    def rules_for_done(self):
        return [
            MatchRule(self._left_top.add(Position(20, 75)), "5291B0"),
            MatchRule(self._left_top.add(Position(20, 76)), "88D9F0"),
        ]

    def rules_for_idle(self):
        return [
            MatchRule(self._left_top.add(Position(20, 75)), "1A3050"),
            MatchRule(self._left_top.add(Position(20, 76)), "4C97C2")
        ]

    def center(self):
        return self._left_top.add(Position(32, 50))


class Preparation(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(165, 161, "135285")
        self._append_rule(166, 161, "88DEF3")
        self._append_rule(474, 248, "73AECE")
        self._append_rule(474, 245, "668EB2")
        self._slots = [
            Slot(Position(840, 656)),
            Slot(Position(914, 656)),
            Slot(Position(987, 656)),
            Slot(Position(1061, 656)),
            Slot(Position(1135, 656)),
            Slot(Position(1209, 656)),
        ]

    def is_slot_list_hide(self):
        rules = [
            MatchRule(Position(1265, 673), "AAE8FC")
        ]
        return self.match_with_rules(rules)

    def show_slot_list(self):
        self._window.left_click(Position(1265, 673))
        self._wait_after_action()

    def enough_items(self):
        rules = [
            MatchRule(Position(607, 250), "078C4F")
        ]
        return self.match_with_rules(rules)

    def submit_items(self):
        self._window.left_click(Position(611, 264))
        self._wait_after_action()

    def is_slot_done(self, index):
        rules = self._slots[index].rules_for_done()
        return self.match_with_rules(rules)

    def some_slot_is_idle(self):
        for i in range(len(self._slots)):
            rules = self._slots[i].rules_for_idle()
            if self.match_with_rules(rules):
                return True
        else:
            return False

    def left_click_slot(self, index):
        self._window.left_click(self._slots[index].center())
        self._wait_after_action()

    def craft(self):
        self._window.left_click(Position(611, 264))
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
