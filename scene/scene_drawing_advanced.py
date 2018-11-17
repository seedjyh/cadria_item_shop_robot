#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/17
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule


class SceneDrawingAdvanced(Scene):
    def __init__(self):
        pass

    def match(self, window):
        rules = [
            MatchRule(position=Position(634, 107), colour=Colour("A3EBF6")),
            MatchRule(position=Position(634, 661), colour=Colour("20D293")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour):
                return False
        return True

    def exit(self, window):
        window.move_to(Position(638, 673))
        window.left_click()


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneDrawingAdvanced()
    if scene.match(window_handle):
        print("match!")
        scene.exit(window_handle)
    else:
        print("NOT match!")
