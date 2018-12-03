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
from scene.utils import go_to_scene


class TaskProcessManufacture(Task):
    """
    process primary manufacture bar.
    """
    def __init__(self):
        self.__item_index = 0  # index in item table

    def do(self, window):
        scene_store_normal = SceneStoreNormal()
        scene_manufacture = SceneManufacture()
        scene_manufacture_one_item = SceneManufactureOneItem()
        go_to_scene(window, scene_store_normal)
        # click idle manufacture slot
        for slot in scene_store_normal.manufacture_slots():
            if slot.get_state(window) == slot.IDLE:
                slot.left_click(window)
                break
        else:
            return True
        # manufacture one item
        print("start manufacture...")
        while True:
            time.sleep(1)
            if scene_manufacture.match(window):
                bar = scene_manufacture.manufacture_pull_left_bar()
                if bar.get_state(window) == bar.HIDDEN:
                    bar.pull_left(window)
                    continue
                if bar.all_busy(window):
                    scene_manufacture.exit(window)
                    return True
                button = scene_manufacture.left_button_favorite()
                if button.get_state(window) == button.OFF:
                    button.left_click(window)
                    continue
                button = scene_manufacture.top_button_all()
                if button.get_state(window) == button.OFF:
                    button.left_click(window)
                    continue
                scene_manufacture.left_click_item(self.__item_index, window)
                self.__item_index = (self.__item_index + 1) % 8
            elif scene_manufacture_one_item.match(window):
                mode = scene_manufacture_one_item.mode()
                if mode.get_state(window) == mode.NORMAL:
                    mode.switch_to_advanced(window)
                    continue
                button = scene_manufacture_one_item.manufacture_button()
                if button.get_state(window) == button.GREY:
                    scene_manufacture_one_item.exit(window)
                    continue
                if button.get_state(window) == button.DIAMOND:
                    scene_manufacture_one_item.exit(window)
                    continue
                button.left_click(window)
                return True
            else:
                print("unknown scene")
                return False


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskProcessManufacture()
    task.do(window_handle)
