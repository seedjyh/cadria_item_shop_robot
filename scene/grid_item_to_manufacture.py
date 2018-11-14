#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/12
from pywindow import Position
from scene.grid import Grid


class GridItemToManufacture(Grid):
    def __init__(self, left_top):
        super().__init__(left_top)

    def center(self):
        return super().position(Position(100, 10))

    def get_state(self):
        pass

    def left_click(self, window):
        window.move_to(self.center())
        window.left_click()


if __name__ == "__main__":
    pass
