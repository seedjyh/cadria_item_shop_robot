#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
from pywindow import Position
from scene.area import Area
from scene.grid_manufacture_pull_left_slot import GridManufacturePullLeftSlot


class AreaManufacturePullLeftBar(Area):
    HIDDEN = 1
    VISIBLE = 2

    def __init__(self):
        """
        :param left_top: left-top position when this area is VISIBLE.
        """
        self.__slot = [
            GridManufacturePullLeftSlot(Position(840, 656)),
            GridManufacturePullLeftSlot(Position(914, 656)),
            GridManufacturePullLeftSlot(Position(987, 656)),
            GridManufacturePullLeftSlot(Position(1061, 656)),
            GridManufacturePullLeftSlot(Position(1135, 656)),
            GridManufacturePullLeftSlot(Position(1209, 656)),
        ]

    def get_state(self, window):
        """

        :param window:
        :return: HIDDEN or VISIBLE
        """
        color = window.get_pixel_color(Position(807, 698))
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
            window.move_to(Position(1264, 694))
            window.left_click()

    def slot(self, index):
        """
        :param index: from 0 to 5
        :return: Area of the slot.
        """
        return self.__slot[index]

    def all_busy(self, window):
        for slot in self.__slot:
            if slot.get_state(window) != slot.BUSY:
                return False
        return True

if __name__ == "__main__":
    pass
