#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/12
from pywindow import Position
from pywindow.colour import Colour
from scene.area import Area


class AreaManufactureButton(Area):
    YELLOW = 1  # OK to manufacture
    GREY = 2
    DIAMOND = 3

    def __init__(self):
        pass

    def get_state(self, window):
        colour = window.get_pixel_color(Position(848, 616))
        if colour.similar_to(Colour("FECE80"), 5):
            return self.DIAMOND
        elif colour.similar_to(Colour("2AB0FF"), 5):
            return self.YELLOW
        else:
            return self.GREY

    def left_click(self, window):
        window.move_to(Position(848, 616))
        window.left_click()


if __name__ == "__main__":
    pass
