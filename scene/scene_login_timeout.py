#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/30
from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule


class SceneLoginTimeout(Scene):
    def __init__(self):
        pass

    def match_rules(self, window):
        return [
            MatchRule(Position(658, 326), Colour("A9B5CC")),
            MatchRule(Position(658, 327), Colour("E9ECF2")),
            MatchRule(Position(658, 329), Colour("92A0BF")),
        ]

    def exit(self, window):
            window.move_to(Position(634, 563))
            window.left_click()


if __name__ == "__main__":
    pass
