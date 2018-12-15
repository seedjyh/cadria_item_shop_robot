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

    def match_rules(self, window):
        return [
            MatchRule(position=Position(153, 41), colour=Colour("4E69A7")),
            MatchRule(position=Position(160, 52), colour=Colour("A6DEFE")),
        ]

    def exploration_slots(self):
        return self.__exploration_slots

    def exit(self, window):
        window.move_to(Position(1239, 688))
        window.left_click()

    def left_click_general_dialog(self, window):
        window.move_to(Position(545, 150))
        window.left_click()


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
