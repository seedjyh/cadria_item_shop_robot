#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/8
import time
from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule


class SceneIWantToPlay(Scene):

    def match(self, window):
        rules = [
            MatchRule(Position(220, 883), Colour("2AC6F8")),
            MatchRule(Position(221, 883), Colour("1A3FCB")),
            MatchRule(Position(223, 883), Colour("33D5E7")),
        ]
        for rule in rules:
            if window.get_pixel_color(rule.position).similar_to(rule.colour):
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    window_text = "微信开发者工具"
    handle = get_window_handle(window_text)
    handle.set_foreground()
    time.sleep(1)
    print("result:", SceneIWantToPlay().match(handle))
