#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
import time

from pywindow.window import get_window_handle
from robot.task import Task
from scene.scene_manufacture import SceneManufacture
from scene.scene_manufacture_one_item import SceneManufactureOneItem
from scene.scene_store_normal import SceneStoreNormal


class TaskProcessManufacture(Task):
    """
    process primary manufacture bar.
    """
    def __init__(self):
        self.__item_index = 0  # index in item table

    def reset(self):
        pass

    def do(self, window):
        scene = SceneStoreNormal()
        if scene.match(window):
            for slot in scene.manufacture_slots():
                if slot.get_state(window) == slot.COMPLETED:
                    slot.left_click(window)
                    return True
                elif slot.get_state(window) == slot.IDLE:
                    slot.left_click(window)
                    return True
            else:
                return False
        scene = SceneManufacture()
        if scene.match(window):
            bar = scene.manufacture_pull_left_bar()
            if bar.get_state(window) == bar.HIDDEN:
                bar.pull_left(window)
                return True
            if bar.all_busy(window):
                scene.exit(window)
                return True
            button = scene.left_button_favorite()
            if button.get_state(window) == button.OFF:
                button.left_click(window)
                return True
            button = scene.top_button_all()
            if button.get_state(window) == button.OFF:
                button.left_click(window)
                return True
            scene.left_click_item(self.__item_index, window)
            self.__item_index = self.__item_index + 1
            return True
        scene = SceneManufactureOneItem()
        if scene.match(window):
            print("match! SceneManufactureOneItem")
            mode = scene.mode()
            if mode.get_state(window) == mode.NORMAL:
                mode.switch_to_advanced(window)
                return True
            button = scene.manufacture_button()
            if button.get_state(window) == button.GREY:
                scene.exit(window)
                return True
            if button.get_state(window) == button.DIAMOND:
                scene.exit(window)
                return True
            button.left_click(window)
            return True
        # other scene....


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskProcessManufacture()
    for i in range(10):
        task.do(window_handle)
        time.sleep(1)
