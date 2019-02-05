#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/5
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


class Chunk:
    def __init__(self, left_top):
        self._left_top = left_top

    def rules_for_ready(self):
        return [
            MatchRule(self._left_top.add(Position(0, 19)), "007539"),
        ]

    def rules_for_idle(self):
        return [
            MatchRule(self._left_top.add(Position(0, 19)), "054D88"),
        ]

    def center(self):
        return self._left_top.add(Position(60, 20))


class OneFaction(Scene):
    """
    Scene with 4 types of items to craft.
    """
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(98, 124, "A7F0F7")
        self._append_rule(442, 158, "5A86AD")
        self._chunks = [
            Chunk(Position(1060, 221)),
            Chunk(Position(1060, 289)),
            Chunk(Position(1060, 356)),
            Chunk(Position(1060, 423)),
        ]
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

    def chunk_is_ready(self, index):
        if index < 0 or index >= len(self._chunks):
            raise Exception("index out of boundarys [0, 3]")
        return self.match_with_rules(self._chunks[index].rules_for_ready())

    def chunk_is_idle(self, index):
        if index < 0 or index >= len(self._chunks):
            raise Exception("index out of boundarys [0, 3]")
        return self.match_with_rules(self._chunks[index].rules_for_idle())

    def left_click_chunk(self, index):
        if index < 0 or index >= len(self._chunks):
            raise Exception("index out of boundarys [0, 3]")
        self._window.left_click(self._chunks[index].center())
        self._wait_after_action()

    def exit(self):
        self._window.left_click(Position(70, 660))
        self._wait_after_action()


if __name__ == "__main__":
    pass
