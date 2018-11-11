#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
import time

from pywindow.window import get_window_handle
from robot.task import Task
from scene.scene_manufacture import SceneManufacture
from scene.scene_store_normal import SceneStoreNormal


class TaskProcessManufacture(Task):
    """
    process primary manufacture bar.
    """
    def __init__(self):
        pass

    def reset(self):
        pass

    def do(self, window):
        scene = SceneStoreNormal()
        if scene.match(window):
            for i in range(6):
                slot = scene.manufacture_slots(i)
                if slot.get_state(window) == slot.COMPLETED:
                    slot.left_click(window)
                    return True
                elif slot.get_state(window) == slot.IDLE:
                    slot.left_click(window)
                    return True
                else:
                    continue
            return False
        scene = SceneManufacture()
        if scene.match(window):
            button = scene.left_button_favorite()
            if button.get_state(window) == button.OFF:
                button.left_click(window)
                return True
            button = scene.top_button_all()
            if button.get_state(window) == button.OFF:
                button.left_click(window)
                return True


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskProcessManufacture()
    task.do(window_handle)
