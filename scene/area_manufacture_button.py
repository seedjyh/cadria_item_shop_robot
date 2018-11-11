#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/12
from pywindow import Position
from pywindow.colour import Colour
from scene.area import Area


class AreaManufactureButton(Area):
    GREEN = 1
    GREY = 2
    DIAMOND = 3

    def __init__(self, left_top):
        super().__init__(left_top)

    def center(self):
        return super().position(Position(65, 27))

    def get_state(self, window):
        # 850, 620
        colour = window.get_pixel_color(super().position(Position(37, 30)))
        if colour.similar_to(Colour("FCAE7B"), 5):
            return self.DIAMOND
        elif colour.similar_to(Colour("707070"), 5):
            return self.GREY
        else:
            return self.GREEN

    def left_click(self, window):
        window.move_to(self.center())
        window.left_click()


if __name__ == "__main__":
    pass
