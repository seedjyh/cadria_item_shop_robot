#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/2
import logging
import time
from pywindow.window import get_window_handle
from robot.task import Task
from scene import utils as scene_utils
from scene.scene_equipment_repairment import SceneEquipmentRepairment
from scene.scene_exploration_finished import SceneExplorationFinished
from scene.scene_exploration_hero_selection import SceneExplorationHeroSelection
from scene.scene_exploration_location_list import SceneExplorationLocationList
from scene.scene_tavern import SceneTavern

logger = logging.getLogger("TaskProcessExploration")

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
        exploration_hero_selection_scene = SceneExplorationHeroSelection()
        exploration_finished_scene = SceneExplorationFinished()
        repair_scene = SceneEquipmentRepairment()
        while True:
            logger.debug("enter while====================")
            time.sleep(1)
            if tavern_scene.match(window):
                for slot in tavern_scene.exploration_slots():
                    if slot.get_state(window) == slot.IDLE:
                        slot.left_click(window)
                        break  # break "for".
                    elif slot.get_state(window) == slot.COMPLETED:
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
                self.__location_index = (self.__location_index + 1) % 9
            elif exploration_hero_selection_scene.match(window):
                idle_slot_list = []
                for hero_slot in exploration_hero_selection_scene.hero_slot_list():
                    if hero_slot.get_state(window) == hero_slot.IDLE:
                        idle_slot_list.append(hero_slot)
                logger.debug("length of idle hero slots list: %d" % len(idle_slot_list))
                if len(idle_slot_list) == 0:
                    logger.debug("Go!")
                    window.enter("G")
                    return True
                else:
                    if exploration_hero_selection_scene.is_hero_banner_shown(window):
                        if not exploration_hero_selection_scene.select_heroes(window, len(idle_slot_list)):
                            return False
                    else:
                        logger.debug("hero banner is NOT shown. Show it.")
                        idle_slot_list[0].left_click(window)
            elif exploration_finished_scene.match(window):
                exploration_finished_scene.exit(window)
            elif repair_scene.match(window):
                repair_scene.exit(window)
            else:
                logger.debug("Unknown scene")
                return False


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskProcessExploration()
    while True:
        print("result:", task.do(window_handle))
