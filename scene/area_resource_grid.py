#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
from pywindow import Position
from scene.area import Area


class AreaResourceGrid(Area):
    def __init__(self, left_top):
        super().__init__(left_top)

    def get_state(self, window):
        pass

    def center(self):
        return super().position(Position(15, 15))


if __name__ == "__main__":
    pass
