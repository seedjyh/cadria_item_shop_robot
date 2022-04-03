#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/8
import win32gui
import time

from PIL import ImageGrab

from pywindow import Position
from pywindow.actor import Actor


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

    def __str__(self):
        return "top=%d,bottom=%d,left=%d,right=%d" % (self.top, self.bottom, self.left, self.right)


class WindowHandle:
    """
    class to operate window in Windows OS.
    """
    def __init__(self, hwnd):
        self.__hwnd = hwnd

    def set_foreground(self):
        """
        Set the window to foreground.
        :return:
        """
        print("setting foreground")
        win32gui.SetForegroundWindow(self.__hwnd)
        time.sleep(1)

    def get_window_image(self):
        """
        Get colour for each pixel in the window, including title bar
        :return:
        """
        window_rect = self.get_rect()
        image = ImageGrab.grab()
        window_image = image.crop((window_rect.left, window_rect.top, window_rect.right, window_rect.bottom))
        return window_image.load()

    def get_rect(self):
        return WindowRect(rect=win32gui.GetWindowRect(self.__hwnd))


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
    window_text = "Cadria Item Shop"
    handle = get_window_handle(window_text)
    handle.set_foreground()
    rect = handle.get_rect()
    actor = Actor()
    for i in range(100):
        time.sleep(2)
        actor.move_to(Position(rect.left, rect.top))
        time.sleep(2)
        actor.left_click(Position(rect.left + 40, rect.top + 40))
