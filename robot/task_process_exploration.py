#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/2
import time

from pywindow import Position
from pywindow.window import get_window_handle
from robot.task import Task
from scene import utils as scene_utils
from scene.scene_exploration_location_list import SceneExplorationLocationList
from scene.scene_tavern import SceneTavern


class TaskProcessExploration(Task):
    """
    Enter the tavern and start an exploration if there's an empty exploration slot.
    """
    def __init__(self):
        self.__location_index = 0  # 0 ~ 8, include boundary

    def do(self, window):
        """
        If there's no enough free heroes, return True.
        If there's no empty exploration slot, return True.
        If a new exploration started, return True.
        :param window:
        :return:
        """
        scene_utils.go_to_scene(window, SceneTavern())
        tavern_scene = SceneTavern()
        exploration_location_list_scene = SceneExplorationLocationList()
        while True:
            print("enter while")
            time.sleep(1)
            if tavern_scene.match(window):
                for slot in tavern_scene.exploration_slots():
                    if slot.get_state(window) == slot.IDLE:
                        slot.left_click(window)
                        break  # break "for".
                else:
                    return True  # no idle exploration slot.
            elif exploration_location_list_scene.match(window):
                zone_list = exploration_location_list_scene.zone_list()
                if zone_list[0].get_state(window) == zone_list[0].UNSELECTED:
                    zone_list[0].left_click(window)
                    continue  # continue "while"
                exploration_location_list_scene.select_location(window, self.__location_index)
            else:
                print("Unknown scene")
                return False



if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskProcessExploration()
    print("result:", task.do(window_handle))
