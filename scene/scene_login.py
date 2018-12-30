#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/30
from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule


class SceneLogin(Scene):
    def __init__(self):
        pass

    def match_rules(self, window):
        return [
            MatchRule(Position(736, 638), Colour("357F5E")),
            MatchRule(Position(738, 638), Colour("FFFFFF")),
            MatchRule(Position(740, 638), Colour("287754")),
        ]

    def exit(self, window):
            window.move_to(Position(736, 638))
            window.left_click()


if __name__ == "__main__":
    pass
