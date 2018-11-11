#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.area_item_to_manufacture import AreaItemToManufacture
from scene.area_manufacture_left_button import AreaManufactureLeftButton
from scene.area_manufacture_top_button import AreaManufactureTopButton
from scene.area_manufacture_pull_left_bar import AreaManufacturePullLeftBar


class SceneManufacture(Scene):
    """
    This scene includes a table of all items to manufacture.
    """
    def __init__(self):
        self.__manufacture_pull_left_bar = AreaManufacturePullLeftBar(Position(789, 650))
        self.__left_button_favorite = AreaManufactureLeftButton(Position(25, 434))
        self.__top_button_all = AreaManufactureTopButton(Position(222, 141))
        self.__items = [
            AreaItemToManufacture(Position(222 + index % 3 * 341, 223 + int(index / 3) * 206)) for index in range(9)
        ]

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

    def left_button_favorite(self):
        return self.__left_button_favorite

    def top_button_all(self):
        return self.__top_button_all

    def left_click_item(self, index, window):
        self.__items[index].left_click(window)

    def exit(self, window):
        window.move_to(Position(68, 667))
        window.left_click()


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
