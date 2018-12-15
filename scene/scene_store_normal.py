#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/10
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.grid_manufacture_slot import GridManufactureSlot
from scene.grid_resource import GridResource
from scene.scene_tavern import SceneTavern


class SceneStoreNormal(Scene):
    def __init__(self):
        self.__manufacture_slots = [
            GridManufactureSlot(Position(315, 615)),
            GridManufactureSlot(Position(425, 615)),
            GridManufactureSlot(Position(535, 615)),
            GridManufactureSlot(Position(646, 615)),
            GridManufactureSlot(Position(756, 615)),
            GridManufactureSlot(Position(867, 615)),
        ]  # a list of Area of manufacture slots in the bottom of this scene.
        self.__resource_grids = [GridResource(Position(1230, 102 + 40 * i)) for i in range(12)]

    def match_rules(self, window):
        return [
            MatchRule(Position(153, 41), Colour("B9E5FE")),
        ]

    def touch_all_resource_grids(self, window):
        for grid in self.__resource_grids:
            window.move_to(grid.center())
            time.sleep(0.1)

    def manufacture_slots(self):
        return self.__manufacture_slots

    def go_to_tavern(self, window):
        window.move_to(Position(1233, 667))
        window.left_click()

    def go_to_scene(self, window, target):
        """
        Go from this scene to target scene...
        :param window:
        :param target:  the target scene, must be unique (not in some kind of slot) and reachable at anytime.
        :return: True means arrived.
        """
        if target.__class__ == SceneTavern:
            self.go_to_tavern(window)
            return True
        else:
            return False

    def exit(self, window):
        pass


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneStoreNormal()
    if scene.match(window_handle):
        print("match!")
    else:
        print("NOT match!")
    scene.touch_all_resource_grids(window_handle)
    scene.left_click_not_busy_manufacture_slot(window_handle)
