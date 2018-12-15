#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/4
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule


class SceneFactionWar(Scene):
    """
    a scene with a big green button *Join Combat* left-bottom.
    """
    def __init__(self):
        pass

    def match_rules(self, window):
        return [
            MatchRule(Position(607, 114), Colour("99AFC1")),
            MatchRule(Position(608, 114), Colour("003664")),
            MatchRule(Position(610, 114), Colour("8DA5BA")),
        ]

    def exit(self, window):
        window.move_to(Position(1146, 106))
        window.left_click()

    def join_combat(self, window):
        window.move_to(Position(345, 600))
        window.left_click()


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneFactionWar()
    if scene.match(window_handle):
        print("match!")
    else:
        print("NOT match!")
