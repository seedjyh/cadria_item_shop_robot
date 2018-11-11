#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.area_manufacture_category import AreaManufactureCategory
from scene.area_manufacture_pull_left_bar import AreaManufacturePullLeftBar


class SceneManufacture(Scene):
    def __init__(self):
        self.__manufacture_pull_left_bar = AreaManufacturePullLeftBar(Position(789, 650))
        self.__favorite_button = AreaManufactureCategory(Position(25, 434))

    def match(self, window):
        rules = [
            MatchRule(Position(95, 81), Colour("C7C1C0")),
            MatchRule(Position(97, 81), Colour("313031")),
            MatchRule(Position(99, 81), Colour("D6D1D3")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour, 5):
                return False
        return True

    def manufacture_pull_left_bar(self):
        return self.__manufacture_pull_left_bar

    def favorite_button(self):
        return self.__favorite_button


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneManufacture()
    if scene.match(window_handle):
        print("match!")
    else:
        print("NOT match!")
    if scene.manufacture_pull_left_bar().get_state(window_handle) == AreaManufacturePullLeftBar.HIDDEN:
        print("pull left bar is hidden")
        scene.manufacture_pull_left_bar().pull_left(window_handle)
    else:
        print("pull left bar is visible")
        for i in range(6):
            slot = scene.manufacture_pull_left_bar().slot(i)
