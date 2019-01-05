#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/8
import ctypes
import win32api
import win32gui
import time

import win32con
from pymouse import PyMouse

from pywindow import Position
from pywindow.colour import Colour
from pykeyboard import PyKeyboard
# TODO: use from pymouse import PyMouse

class WindowRect:
    def __init__(self, **kwargs):
        """
        :param kwargs: rect=(1,2,3,4) or left=1,top=2,right=3,bottom=4
        """
        self.left = 0
        self.top = 0
        self.right = 0
        self.bottom = 0
        for key, value in kwargs.items():
            if key == "rect":
                self.left = value[0]
                self.top = value[1]
                self.right = value[2]
                self.bottom = value[3]
            else:
                setattr(self, key, value)

    def width(self):
        return self.right - self.left

    def height(self):
        return self.bottom - self.top


class WindowHandle:
    """
    class to operate window in Windows OS.
    """
    def __init__(self, hwnd):
        self.hwnd = hwnd

    def left_top(self):
        rect = WindowRect(rect=win32gui.GetWindowRect(self.hwnd))
        return Position(rect.left, rect.top)

    def set_foreground(self):
        """
        Set the window to foreground.
        :return:
        """
        win32gui.SetForegroundWindow(self.hwnd)

    def get_pixel_color(self, position):
        """
        get color of pixel specified by x, y, the position IN the window.
        :param position: relative position from left-top of the window.
        :return: object for class Colour
        """
        hdc = ctypes.windll.user32.GetDC(None)
        screen_pixel = self.left_top().add(position)
        get_result = ctypes.windll.gdi32.GetPixel(hdc, screen_pixel.x, screen_pixel.y)
        return Colour(colour=get_result)

    def move_to(self, position):
        """
        move cursor to x, y, the position IN the window.
        :param position: relative position from left-top of the window.
        :return:
        """
        screen_pixel = self.left_top().add(position)
        win32api.SetCursorPos((screen_pixel.x, screen_pixel.y))

    def get_position(self):
        """
        get position of cursor
        :return: object of class Position
        """
        x, y = win32api.GetCursorPos()
        return Position(x, y).minus(self.left_top())

    @staticmethod
    def left_click():
        """
        click the left button of the mouse.
        :return:
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)

    @staticmethod
    def enter(word):
        """
        enter each character in word
        :param word:
        :return: None
        """
        word = str.lower(word)
        k = PyKeyboard()
        for key in word:
            k.tap_key(key)

    @staticmethod
    def scroll(vertical=None):
        """
        Scroll the mouse
        :param vertical: negative means scroll downward.
        :return: None
        """
        m = PyMouse()
        m.scroll(vertical=vertical)


def get_window_handle(title):
    """
    Search an enabled and valid window whose title contains parameter @title.
    Only the first window matched would be return if there're multiple results.
    :param title: Full or part of title
    :return: WindowHandle if found, or None if not.
    """
    hwnd_list = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_list)
    for hwnd in hwnd_list:
        if not win32gui.IsWindow(hwnd):
            continue
        if not win32gui.IsWindowEnabled(hwnd):
            continue
        if not win32gui.IsWindowVisible(hwnd):
            continue
        full_title = win32gui.GetWindowText(hwnd)
        if full_title.find(title) >= 0:
            return WindowHandle(hwnd)
    return None


if __name__ == "__main__":
    window_text = "微信开发者工具"
    x = 397
    y = 439
    handle = get_window_handle(window_text)
    handle.set_foreground()
    time.sleep(1)
    c = handle.get_pixel_color(Position(x, y))
    print(hex(c.red), hex(c.green), hex(c.blue))
