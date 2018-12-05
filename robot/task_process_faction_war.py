#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/4
import time

from pywindow.window import get_window_handle
from robot.task import Task
from scene.scene_combat import SceneCombat
from scene.scene_combat_hero_selection import SceneCombatHeroSelection
from scene.scene_faction_war import SceneFactionWar
from scene.scene_tavern import SceneTavern
from scene import utils as scene_utils


class TaskProcessFactionWar(Task):

    def __init__(self):
        pass

    def do(self, window):
        """
        send a team for faction war or welcome their returning.
        :param window: handle of game window
        :return: True if something was done
        """
        tavern_scene = SceneTavern()
        faction_war_scene = SceneFactionWar()
        combat_scene = SceneCombat()
        combat_hero_selection_scene = SceneCombatHeroSelection()
        # step 1 - go to tarven
        scene_utils.go_to_scene(window, SceneTavern())
        while True:
            time.sleep(1)
            if tavern_scene.match(window):
                tavern_scene.left_click_general_dialog(window)
            elif faction_war_scene.match(window):
                faction_war_scene.join_combat(window)
            elif combat_scene.match(window):
                scene_state = combat_scene.get_state(window)
                if scene_state == combat_scene.STATE_FREE:
                    combat_scene.select_level(window, combat_scene.LEVEL_NIGHTMARE)
                elif scene_state == combat_scene.STATE_COMBATING:
                    return True
                else:
                    combat_scene.welcome_back(window)
            elif combat_hero_selection_scene.match(window):
                idle_slots = combat_hero_selection_scene.idle_hero_slots(window)
                if len(idle_slots) == 0:
                    window.enter("G")
                    return True
                else:
                    if combat_hero_selection_scene.is_hero_banner_shown(window):
                        combat_hero_selection_scene.select_heroes(window, len(idle_slots))
                    else:
                        idle_slots[0].left_click(window)
            else:
                print("Unknown scene")
                return False


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    task = TaskProcessFactionWar()
    for i in range(1000000):
        print("result:", task.do(window_handle))
