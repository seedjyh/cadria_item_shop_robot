#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
import time

from pywindow import Position
from .scene import Scene, MatchRule


class CraftSlot:
    def __init__(self, left_top):
        self.left_top = left_top

    def rule_for_idle(self):
        rules = [
            MatchRule(self.left_top.add(Position(23, 112)), "152540"),
            MatchRule(self.left_top.add(Position(23, 115)), "94FFFF"),
        ]
        return rules

    def rule_for_completed(self):
        rules = [
            MatchRule(self.left_top.add(Position(20, 112)), "8EF3FD"),
            MatchRule(self.left_top.add(Position(20, 121)), "81F7FF"),
        ]
        return rules

    def center(self):
        return self.left_top.add(Position(50, 50))


class Shop(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(153, 41, "B9E5FE")
        self.__resource_grids = [Position(1230, 102 + 40 * i) for i in range(12)]
        self.__craft_slots = [
            CraftSlot(Position(315, 624)),
            CraftSlot(Position(425, 624)),
            CraftSlot(Position(535, 624)),
            CraftSlot(Position(646, 624)),
            CraftSlot(Position(756, 624)),
            CraftSlot(Position(867, 624)),
        ]

    def go_to_tavern(self):
        self._window.tap_letter("i")
        self._wait_after_action(times=3)

    def touch_resources(self):
        for grid in self.__resource_grids:
            self._window.move_to(grid.add(Position(20, 20)))
            self._wait_after_action()

    def customer_points(self):
        """
        generate 12 * 6 points around center of rect window.
        :return: generator of Point
        """
        top = 180
        bottom = 600
        height = bottom - top
        left = 330
        right = 1030
        width = right - left
        for i in range(12):
            for j in range(6):
                yield (Position(int(left + i * width / 12), int(top + j * height / 6)))

    def completed_craft_slot(self, index):
        if index < 0 or index >= 6:
            raise Exception("invalid slot index", index)
        print("rules", index, self.__craft_slots[index].rule_for_completed()[0])
        print("rules", index, self.__craft_slots[index].rule_for_completed()[1])
        return self.match_with_rules(self.__craft_slots[index].rule_for_completed())

    def idle_craft_slot(self, index):
        if index < 0 or index >= 6:
            raise Exception("invalid slot index", index)
        return self.match_with_rules(self.__craft_slots[index].rule_for_idle())

    def left_click_craft_slot(self, index):
        if index < 0 or index >= 6:
            raise Exception("invalid slot index", index)
        self._window.left_click(self.__craft_slots[index].center())
        self._wait_after_action(times=3)



if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    scene = Shop(window_handle)
    if not scene.match():
        print("not shop!")
        exit()
    scene.touch_resources()
