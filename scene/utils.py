#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
from . import shop, tavern, unknown
from .scene import Scene


def identify_scene(window):
    for now_scene in Scene.__subclasses__():
        obj = now_scene(window)
        print("now obj:", obj)
        if obj.match():
            return obj
    else:
        return unknown.Unknown(window)


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    print(identify_scene(window_handle))
