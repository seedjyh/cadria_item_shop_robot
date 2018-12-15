#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/17
from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule


class SceneEquipmentRepairment(Scene):
    def __init__(self):
        pass

    def match_rules(self, window):
        return [
            MatchRule(position=Position(631, 34), colour=Colour("121A1C")),
            MatchRule(position=Position(579, 571), colour=Colour("4261EF")),
            MatchRule(position=Position(709, 571), colour=Colour("18BD7E")),
        ]

    def exit(self, window):
        window.move_to(Position(709, 571))
        window.left_click()


if __name__ == "__main__":
    pass
