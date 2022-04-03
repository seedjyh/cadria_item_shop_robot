#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/8
from pywindow import Position
from scene.scene import Scene, MatchRule

from .scene import Scene


class ShopOrder(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(510, 148, "10264A")
        self._append_rule(510, 246, "7392B5")
        self._append_rule(1068, 239, "21456B")
        self._append_rule(1143, 118, "0049FF")

    def rules_as_offer(self):
        rules = [
            MatchRule(Position(850, 585), "00009C"),
            MatchRule(Position(1000, 585), "006D31")
        ]
        return rules

    def accept(self):
        self._actor.left_click(Position(1000, 600))
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
