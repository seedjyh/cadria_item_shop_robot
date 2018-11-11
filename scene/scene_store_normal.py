#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/10
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.area_manufacture_slot import AreaManufactureSlot


class SceneStoreNormal(Scene):
    def __init__(self):
        self.__manufacture_slots = [
            AreaManufactureSlot(Position(315, 615)),
            AreaManufactureSlot(Position(425, 615)),
            AreaManufactureSlot(Position(535, 615)),
            AreaManufactureSlot(Position(646, 615)),
            AreaManufactureSlot(Position(756, 615)),
            AreaManufactureSlot(Position(867, 615)),
        ]  # a list of Area of manufacture slots in the bottom of this scene.

    def match(self, window):
        rules = [
            MatchRule(Position(153, 41), Colour("B9E5FE")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour):
                return False
        return True

    def manufacture_slots(self):
        """
        get a copy of list of Area of manufacture slot list.
        :return: list of AreaManufactureSlot
        """
        return [slot for slot in self.__manufacture_slots]


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneStoreNormal()
    if scene.match(window_handle):
        print("match!")
        for slot in SceneStoreNormal().manufacture_slots():
            print("state of slot:", slot.get_state(window_handle))
    else:
        print("NOT match!")
