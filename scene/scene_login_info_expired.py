#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/30
from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule


class SceneLoginInfoExpired(Scene):
    def __init__(self):
        pass

    def match_rules(self, window):
        return [
            MatchRule(Position(651, 322), Colour("697DA7")),
            MatchRule(Position(653, 322), Colour("FFFFFF")),
            MatchRule(Position(655, 322), Colour("8596B7")),
            MatchRule(Position(643, 561), Colour("17BA7D")),
        ]

    def exit(self, window):
            window.move_to(Position(643, 561))
            window.left_click()


if __name__ == "__main__":
    pass
