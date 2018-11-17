#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/17
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule


class SceneExplorationFinished(Scene):
    def __init__(self):
        pass

    def match(self, window):
        rules = [
            MatchRule(position=Position(454, 36), colour=Colour("D6E3CE")),
            MatchRule(position=Position(636, 36), colour=Colour("9FEAFF")),
            MatchRule(position=Position(824, 36), colour=Colour("D6E3CE")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour):
                return False
        return True


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneExplorationFinished()
    if scene.match(window_handle):
        print("match!")
    else:
        print("NOT match!")
