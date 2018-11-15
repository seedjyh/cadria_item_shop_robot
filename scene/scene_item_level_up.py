#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/16
from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule


class SceneItemLevelUp(Scene):
    def __init__(self):
        pass

    def match(self, window):
        rules = [
            MatchRule(Position(601, 638), Colour("5275F7")),
            MatchRule(Position(687, 638), Colour("1BCB8F")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour, 8):
                return False
        return True

    def exit(self, window):
        window.move_to(Position(601, 638))
        window.left_click()


if __name__ == "__main__":
    pass
