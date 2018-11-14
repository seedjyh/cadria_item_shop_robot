#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/12
from pywindow import Position
from pywindow.colour import Colour
from scene import MatchRule, Scene
from scene.area_manufacture_button import AreaManufactureButton
from scene.area_manufacture_mode import AreaManufactureMode


class SceneManufactureOneItem(Scene):
    def __init__(self):
        self.__mode = AreaManufactureMode()
        self.__manufacture_button = AreaManufactureButton()

    def match(self, window):
        rules = [
            MatchRule(Position(564, 529), Colour("245179")),
            MatchRule(Position(566, 529), Colour("8BB9D8")),
            MatchRule(Position(568, 529), Colour("CBE6F2")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour, 5):
                return False
        return True

    def mode(self):
        return self.__mode

    def manufacture_button(self):
        return self.__manufacture_button

    def exit(self, window):
        window.move_to(Position(1075, 117))
        window.left_click()


if __name__ == "__main__":
    pass
