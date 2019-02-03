#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3

from robot.task import Task
from scene.utils import identify_scene
from scene.shop import Shop
from scene.tavern import Tavern
from scene.bank import Bank


class TaskHandleBank(Task):
    def __init__(self):
        pass

    def do(self, window):
        while True:
            scene = identify_scene(window)
            if isinstance(scene, Shop):
                scene.go_to_tavern()
            elif isinstance(scene, Tavern):
                scene.go_to_bank()
            elif isinstance(scene, Bank):
                if scene.is_maturity():
                    scene.withdraw()
                elif scene.is_idle():
                    scene.deposit()
                    return True
                else:
                    return True
            else:
                scene.exit()


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    task = TaskHandleBank()
    task.do(window_handle)
