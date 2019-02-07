#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
import time

from pywindow import Position
from .scene import Scene


class Shop(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(153, 41, "B9E5FE")
        self.__resource_grids = [Position(1230, 102 + 40 * i) for i in range(12)]

    def go_to_tavern(self):
        self._window.tap_letter("i")
        self._wait_after_action(times=3)

    def touch_resources(self):
        for grid in self.__resource_grids:
            self._window.move_to(grid.add(Position(20, 20)))
            self._wait_after_action()

    def customer_points(self):
        """
        generate 12 * 6 points around center of rect window.
        :return: generator of Point
        """
        rect = self._window.get_rect()
        top = rect.top + (rect.bottom - rect.top) / 4
        bottom = rect.top + (rect.bottom - rect.top) * 3 / 4
        height = bottom - top
        left = rect.left + (rect.right - rect.left) / 4
        right = rect.left + (rect.right - rect.left) * 3 / 4
        width = right - left
        for i in range(12):
            for j in range(6):
                yield (Position(int(left + i * width / 12), int(top + j * height / 6)))


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    scene = Shop(window_handle)
    if not scene.match():
        print("not shop!")
        exit()
    scene.touch_resources()
