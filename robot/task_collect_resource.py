#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/5
from robot.task import Task
from scene.shop import Shop
from scene.utils import go_to_shop, assert_scene


class TaskCollectResource(Task):
    def __init__(self):
        pass

    def do(self, window):
        go_to_shop(window)
        assert_scene(Shop, window).touch_resources()


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    task = TaskCollectResource()
    task.do(window_handle)
