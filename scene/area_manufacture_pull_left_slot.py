#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
from pywindow import Position
from pywindow.colour import Colour
from scene import MatchRule
from scene.area import Area


class AreaManufacturePullLeftSlot(Area):
    IDLE = 1
    BUSY = 2  # working or completed

    def __init__(self, left_top):
        super().__init__(left_top)

    def get_state(self, window):
        idle_rule = [
            MatchRule(Position(26, 77), Colour("7DEAFF")),
            MatchRule(Position(27, 77), Colour("7CE9FF")),
            MatchRule(Position(28, 77), Colour("77E5FC")),
            MatchRule(Position(29, 77), Colour("77E5FC")),
        ]
        match = True
        for rule in idle_rule:
            match = match and window.get_pixel_color(super().position(rule.position)).similar_to(rule.colour, diff=8)
        if match:
            return self.IDLE
        return self.BUSY

    def center(self):
        return self.position(Position(34, 38))


if __name__ == "__main__":
    pass
