#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
from pywindow import Position
from pywindow.colour import Colour
from scene import MatchRule
from scene.area import Area


class AreaManufactureLeftButton(Area):
    OFF = 1
    ON = 2

    def __init__(self):
        pass

    def get_state(self, window):
        rule = MatchRule(Position(25, 434), Colour("6BB7D5"))
        if window.get_pixel_color(rule.position).similar_to(rule.colour, 5):
            return self.ON
        else:
            return self.OFF

    def center(self):
        return Position(98, 490)

    def left_click(self, window):
        window.move_to(self.center())
        window.left_click()


if __name__ == "__main__":
    pass
