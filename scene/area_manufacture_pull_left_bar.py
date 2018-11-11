#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
from pywindow import Position
from pywindow.colour import Colour
from scene import MatchRule
from scene.area import Area
from scene.area_manufacture_pull_left_slot import AreaManufacturePullLeftSlot


class AreaManufacturePullLeftBar(Area):
    HIDDEN = 1
    VISIBLE = 2

    def __init__(self, left_top):
        """
        :param left_top: left-top position when this area is VISIBLE.
        """
        super().__init__(left_top)
        self.__slot = [
            AreaManufacturePullLeftSlot(super().position(Position(51, 6))),
            AreaManufacturePullLeftSlot(super().position(Position(125, 6))),
            AreaManufacturePullLeftSlot(super().position(Position(198, 6))),
            AreaManufacturePullLeftSlot(super().position(Position(272, 6))),
            AreaManufacturePullLeftSlot(super().position(Position(346, 6))),
            AreaManufacturePullLeftSlot(super().position(Position(420, 6))),
        ]

    def get_state(self, window):
        """

        :param window:
        :return: HIDDEN or VISIBLE
        """
        key_pixel = Position(18, 48)  # key pixel position IN area.
        color = window.get_pixel_color(self.position(key_pixel))
        if color.similar_to("184072", diff=5):
            return self.VISIBLE
        else:
            return self.HIDDEN

    def center(self):
        """
        center position when this area is HIDDEN.
        :return:
        """
        return super().position(Position(22, 34))

    def pull_left(self, window):
        if self.get_state(window) == self.VISIBLE:
            print("Warning: this area is already visible.")
            return
        else:
            window.move_to(self.position(Position(475, 44)))
            window.left_click()

    def slot(self, index):
        """
        :param index: from 0 to 5
        :return: Area of the slot.
        """
        return self.__slot[index]


if __name__ == "__main__":
    pass
