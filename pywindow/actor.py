#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/3/1
from pykeyboard import PyKeyboard
from pymouse import PyMouse


class Actor():
    def __init__(self):
        self.__k = PyKeyboard()
        self.__m = PyMouse()

    def move_to(self, position):
        """
        move cursor to x, y, the position of the ENTIRE SCREEN.
        :param position: relative position from left-top of the window.
        :return:
        """
        self.__m.move(position.x, position.y)

    def left_click(self, position):
        """
        move to a position and click the left button of the mouse.
        :param position: absolute position from left-top of the ENTIRE SCREEN.
        :return:
        """
        self.__m.click(position.x, position.y)

    def tap_letter(self, key):
        """
        tap a letter on keyboard once
        :param word:
        :return: None
        """
        self.__k.tap_key(key)

    def tap_escape(self):
        self.__k.tap_key(k.escape_key)

    def scroll(self, vertical=None):
        """
        Scroll the mouse
        :param vertical: negative means scroll downward.
        :return: None
        """
        self.__m.scroll(vertical=vertical)


if __name__ == "__main__":
    pass
