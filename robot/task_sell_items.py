#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/19
import random
import time

from pywindow import Position
from pywindow.window import get_window_handle
from robot.task import Task
from scene import utils
from scene.scene_store_normal import SceneStoreNormal
from scene.scene_transaction import SceneTransaction


class TaskSellItems(Task):
    def __init__(self):
        self.__try_count = 100  # try click so many times randomly.

    def do(self, window):
        scene_store_normal = SceneStoreNormal()
        scene_transaction = SceneTransaction()
        utils.go_to_scene(window, scene_store_normal)
        time.sleep(1)
        clicked_count = 0
        while clicked_count < self.__try_count:
            window.move_to(self.rand_position(window))
            window.left_click()
            clicked_count += 1
            time.sleep(1)
            if scene_store_normal.match(window):  # clicked the ground, but not customer
                continue
            elif scene_transaction.match(window): # clicked customer
                if scene_transaction.tradable(window):
                    scene_transaction.trade(window)
                else:
                    # TODO: recommand
                    scene_transaction.refuse(window)
            else:  # unknown scene
                return False

    def rand_position(self, window):
        window_rect = window.get_rect()
        left = window_rect.left + window_rect.width() / 4
        right = window_rect.right - window_rect.width() / 4
        top = window_rect.top + window_rect.height() / 4
        bottom = window_rect.bottom - window_rect.height() / 4
        return Position(
            int(left + random.random() * (right - left)),
            int(top + random.random() * (bottom - top)),
        )



if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskSellItems()
    task.do(window_handle)
