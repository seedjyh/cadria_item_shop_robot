#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/17
from pywindow import Position
from scene.grid import Grid


class GridExplorationSlot(Grid):
    IDLE = 1
    WORKING = 2
    COMPLETED = 3

    def __init__(self, left_top):
        super().__init__(left_top)

    def get_state(self, window):
        # 535, 615
        key_pixel = Position(17, 29)  # key pixel position IN area.
        color = window.get_pixel_color(self.position(key_pixel))
        if color.similar_to("A575A2", diff=5):
            return self.WORKING
        elif color.similar_to("0B9DFF", diff=5):
            return self.COMPLETED
        else:
            return self.IDLE

    def center(self):
        return self.position(Position(50, 50))

    def left_click(self, window):
        window.move_to(self.center())
        window.left_click()


if __name__ == "__main__":
    pass
