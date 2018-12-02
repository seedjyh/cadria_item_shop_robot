#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/2
from pywindow import Position
from scene.grid import Grid


class GridExplorationLocationZone(Grid):
    SELECTED = 1
    UNSELECTED = 2

    def __init__(self, left_top):
        super().__init__(left_top)

    def center(self):
        return self.position(Position(67, 50))

    def get_state(self, window):
        if window.get_pixel_color(self.position(Position(67, 50))).similar_to("8ADEFF", diff=5):
            return self.SELECTED
        else:
            return self.UNSELECTED

    def left_click(self, window):
        window.move_to(self.center())
        window.left_click()


if __name__ == "__main__":
    pass
