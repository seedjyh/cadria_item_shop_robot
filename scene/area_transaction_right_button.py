#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/16
from pywindow import Position
from pywindow.colour import Colour
from scene import MatchRule
from scene.area import Area


class AreaTransactionRightButton(Area):
    GREEN = 1
    YELLOW = 2
    GREY = 3

    def __init__(self):
        pass

    def get_state(self, window):
        rule_state = {
            MatchRule(Position(930, 480), Colour("23ABFF")): self.YELLOW,
            MatchRule(Position(930, 480), Colour("089952")): self.GREEN,
            MatchRule(Position(930, 480), Colour("044D29")): self.GREY,
        }
        for rule, state in rule_state.items():
            if window.get_pixel_color(rule.position).similar_to(rule.colour, 8):
                return state
        else:
            return None

    def left_click(self, window):
        window.move_to(Position(930, 480))
        window.left_click()


if __name__ == "__main__":
    pass
