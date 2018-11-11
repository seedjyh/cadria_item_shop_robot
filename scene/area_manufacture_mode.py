#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/12
from pywindow import Position
from pywindow.colour import Colour
from scene import MatchRule
from scene.area import Area


class AreaManufactureMode(Area):
    NORMAL = 1
    ADVANCED = 2

    def __init__(self, left_top):
        super().__init__(left_top)

    def center(self):
        return super().position(Position(0, 0))

    def get_state(self, window):
        rule = MatchRule(Position(101, 22), Colour("63A6DE"))
        if window.get_pixel_color(super().position(rule.position)).similar_to(rule.colour, 5):
            return self.ADVANCED
        else:
            return self.NORMAL

    def switch_to_advanced(self, window):
        window.move_to(super().position(Position(101, 22)))
        window.left_click()


if __name__ == "__main__":
    pass
