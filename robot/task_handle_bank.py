#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
import time

from robot.task import Task
from scene.retrieve_interest import RetrieveInterest
from scene.utils import go_to_shop, assert_scene
from scene.shop import Shop
from scene.tavern import Tavern
from scene.bank import Bank


class TaskHandleBank(Task):
    def __init__(self):
        pass

    @staticmethod
    def do(window):
        go_to_shop(window)
        assert_scene(Shop, window).go_to_tavern()
        assert_scene(Tavern, window).go_to_bank()
        now = assert_scene(Bank, window)
        if now.is_maturity():
            now.withdraw()
            assert_scene(RetrieveInterest, window).exit()
        now = assert_scene(Bank, window)
        if now.match() and now.is_idle():
            now.deposit()


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    task = TaskHandleBank()
    task.do(window_handle)
