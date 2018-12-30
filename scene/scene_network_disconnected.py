#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/30
from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule


class SceneNetworkDisconnected(Scene):
    def __init__(self):
        pass

    def match_rules(self, window):
        return [
            MatchRule(Position(640, 565), Colour("E5EEEA")),
            MatchRule(Position(642, 565), Colour("037241")),
            MatchRule(Position(643, 565), Colour("0BA965")),
        ]

    def exit(self, window):
            window.move_to(Position(640, 565))
            window.left_click()


if __name__ == "__main__":
    pass
