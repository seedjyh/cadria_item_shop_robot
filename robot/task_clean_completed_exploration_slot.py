#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/17
import time

from pywindow.window import get_window_handle
from robot.task import Task
from scene import utils as scene_utils
from scene.scene_equipment_repairment import SceneEquipmentRepairment
from scene.scene_exploration_finished import SceneExplorationFinished
from scene.scene_tavern import SceneTavern


class TaskCleanCompletedExplorationSlot(Task):
    """
    if there's any completed exploration slot, clean it.
    repair broken equipments if necessary.
    """
    def __init__(self):
        pass

    def do(self, window):
        scene_utils.go_to_scene(window, SceneTavern())
        tavern_scene = SceneTavern()
        exploration_finished_scene = SceneExplorationFinished()
        repair_scene = SceneEquipmentRepairment()
        slot_index = 0
        while True:
            time.sleep(1)
            if exploration_finished_scene.match(window):
                exploration_finished_scene.exit(window)
            elif repair_scene.match(window):
                repair_scene.exit(window)
            elif tavern_scene.match(window):
                slot_list = tavern_scene.exploration_slots()
                if slot_index >= len(slot_list):
                    return True
                slot = slot_list[slot_index]
                slot_index = slot_index + 1
                if slot.get_state(window) == slot.COMPLETED:
                    slot.left_click(window)
            else:
                return False


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskCleanCompletedExplorationSlot()
    print("result:", task.do(window_handle))
