#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/16
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule


class SceneItemLevelUp(Scene):
    def __init__(self):
        pass

    def match_rules(self, window):
        return [
            MatchRule(Position(601, 638), Colour("5275F7")),
            MatchRule(Position(687, 638), Colour("1BCB8F")),
        ]

    def exit(self, window):
        window.move_to(Position(601, 638))
        window.left_click()


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneItemLevelUp()
    if scene.match(window_handle):
        print("match!")
        scene.exit(window_handle)
    else:
        print("NOT match!")
