#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/9
from abc import ABCMeta, abstractmethod

from pywindow import Position


class Area:
    __metaclass__ = ABCMeta

    def __init__(self, left_top):
        """
        :param left_top: the position of left-top point in screen (not in window, but the screen).
        """
        self.__left_top = left_top

    def screen_point(self, point):
        """
        calculate the position of point(x, y) in the screen.
        :param point:
        :return:
        """
        return Position(self.__left_top.x + point.x, self.__left_top.y + point.y)

    def position(self, offset):
        """
        get the position of pixel
        :param offset: offset from left-top to the of center of this area.
        :return: Position of actual position of this pixel.
        """
        return self.__left_top.add(offset)

    @abstractmethod
    def center(self):
        """
        get the position of center of this area
        :return:
        """
        pass

    @abstractmethod
    def get_state(self):
        pass


if __name__ == "__main__":
    pass
