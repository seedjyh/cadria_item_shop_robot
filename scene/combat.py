#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/6
from pywindow import Position
from .scene import Scene, MatchRule


class Combat(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(165, 253, "135285")
        self._append_rule(474, 245, "668EB2")
        self._append_rule(474, 248, "73AECE")

    def squad_is_back(self):
        rules = [
            MatchRule(Position(741, 323), "7BEFFF")
        ]
        return self.match_with_rules(rules)

    def check_out_squad(self):
        print("checking out squad")
        self._actor.left_click(Position(474, 400))
        self._wait_after_action()

    def idle(self):
        rules = [
            MatchRule(Position(709, 392), "7AAAC6")
        ]
        return self.match_with_rules(rules)

    def left_click_nightmare(self):
        self._actor.left_click(Position(635, 389))
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
