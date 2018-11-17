#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/15
import time

from pywindow.window import get_window_handle
from robot.task import Task
from scene.scene_store_normal import SceneStoreNormal
from scene import utils as scene_utils


class TaskCleanCompletedPrimaryManufactureSlot(Task):
    """
    if there's any completed primary manufacture slot, left-click it to take the item.
    handle with level-up of item if necessary.
    """
    def __init__(self):
        pass

    def do(self, window):
        scene = SceneStoreNormal()
        scene_utils.go_to_scene(window, scene)
        for slot in scene.manufacture_slots():
            if slot.get_state(window) == slot.COMPLETED:
                slot.left_click(window)
                time.sleep(1)
                if not scene.match(window):
                    return False
        else:
            return True


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskCleanCompletedPrimaryManufactureSlot()
    for i in range(10):
        print("result:", task.do(window_handle))
