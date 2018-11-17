#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/17
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.grid_exploration_slot import GridExplorationSlot


class SceneTavern(Scene):
    def __init__(self):
        self.__exploration_slots = [
            GridExplorationSlot(Position(424, 615)),
            GridExplorationSlot(Position(535, 615)),
            GridExplorationSlot(Position(646, 615)),
            GridExplorationSlot(Position(758, 615)),
            GridExplorationSlot(Position(869, 615)),
        ]

    def match(self, window):
        rules = [
            MatchRule(position=Position(153, 41), colour=Colour("4E69A7")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour):
                return False
        return True

    def exploration_slots(self):
        return self.__exploration_slots


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneTavern()
    if scene.match(window_handle):
        print("match!")
    else:
        print("NOT match!")
