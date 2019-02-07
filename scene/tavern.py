#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
from pywindow import Position
from .scene import Scene, MatchRule


class AdventureSlot:
    def __init__(self, left_top):
        self.left_top = left_top

    def rules_for_idle(self):
        return [MatchRule(self.left_top.add(Position(20, 0)), "002039"),]

    def rule_for_completed(self):
        return [MatchRule(self.left_top.add(Position(20, 0)), "0061CE"),]

    def center(self):
        return self.left_top.add(Position(50, 50))


class Tavern(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(41, 33, "3885FE")
        self._append_rule(65, 33, "3885FE")
        self._adventure_slots = [
            AdventureSlot(Position(312, 615)),
            AdventureSlot(Position(424, 615)),
            AdventureSlot(Position(535, 615)),
            AdventureSlot(Position(646, 615)),
            AdventureSlot(Position(758, 615)),
            AdventureSlot(Position(869, 615)),
        ]

    def go_to_factions(self):
        self._window.left_click(Position(300, 100))
        self._wait_after_action()

    def go_to_bank(self):
        self._window.left_click(Position(1123, 393))
        self._wait_after_action()

    def go_to_faction_war(self):
        self._window.left_click(Position(550, 157))
        self._wait_after_action()

    def adventure_slot_idle(self, index):
        if index < 0 or index >= len(self._adventure_slots):
            raise Exception("Invalid index for adventure in tavern, index=%d" % index)
        return self.match_with_rules(self._adventure_slots[index].rules_for_idle())

    def adventure_slot_completed(self, index):
        if index < 0 or index >= len(self._adventure_slots):
            raise Exception("Invalid index for adventure in tavern, index=%d" % index)
        return self.match_with_rules(self._adventure_slots[index].rule_for_completed())

    def left_click_adventure_slot(self, index):
        if index < 0 or index >= len(self._adventure_slots):
            raise Exception("Invalid index for adventure in tavern, index=%d" % index)
        self._window.left_click(self._adventure_slots[index].center())
        self._wait_after_action()

    def exit(self):
        self._window.tap_letter("b")  # hotkey: go to Scene Shop
        self._wait_after_action()


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    scene = Tavern(window_handle)
    if not scene.match():
        print("not tavern!")
        exit()
    scene.go_to_bank()
