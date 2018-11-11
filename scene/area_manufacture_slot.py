#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/10
from pywindow import Position
from scene.area import Area


class AreaManufactureSlot(Area):
    IDLE = 1
    WORKING = 2
    COMPLETED = 3

    def __init__(self, left_top):
        super().__init__(left_top)

    def get_state(self, window):
        key_pixel = Position(52, 100)  # key pixel position IN area.
        color = window.get_pixel_color(self.position(key_pixel))
        if color.similar_to("94DFFF", diff=5):
            return self.COMPLETED
        elif color.similar_to("475E69", diff=5):
            return self.IDLE
        else:
            return self.WORKING

    def center(self):
        return self.position(Position(50, 50))

    def left_click(self, window):
        window.move_to(self.center())
        window.left_click()


if __name__ == "__main__":
    slot = AreaManufactureSlot(left_top=Position(3, 4))
    print(slot.left_top)
