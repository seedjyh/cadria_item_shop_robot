#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/3
from pywindow import Position
from scene.grid import Grid


class GridExplorationHeroSlot(Grid):
    IDLE = 1
    HERO = 2

    def __init__(self, left_top):
        super().__init__(left_top)

    def center(self):
        return self.position(Position(22, 22))

    def get_state(self, window):
        if window.get_pixel_color(self.position(Position(22, 21))).similar_to("18B27B", diff=16):
            return self.IDLE
        else:
            return self.HERO

    def left_click(self, window):
        window.move_to(self.center())
        window.left_click()


if __name__ == "__main__":
    pass
