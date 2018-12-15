#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/4
import logging
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.grid_combat_hero_slot import GridCombatHeroSlot

logger = logging.getLogger("SceneCombatHeroSelection")


class SceneCombatHeroSelection(Scene):
    """
    a scene for selecting heroes free to go to combat.
    """
    def __init__(self):
        self.__hero_slots = [
            GridCombatHeroSlot(Position(333, 471)),
            GridCombatHeroSlot(Position(477, 471)),
            GridCombatHeroSlot(Position(621, 471)),
            GridCombatHeroSlot(Position(765, 471)),
        ]

    def match_rules(self, window):
           return [
            MatchRule(Position(614, 360), Colour("66BEE2")),
            MatchRule(Position(617, 360), Colour("2951D6")),
        ]

    def exit(self, window):
        if self.is_hero_banner_shown(window):
            window.move_to(Position(427, 476))
            window.left_click()
        else:
            window.move_to(Position(1207, 117))
            window.left_click()

    def hero_slot_list(self):
        return self.__hero_slots

    def idle_hero_slots(self, window):
        idle_slots = []
        for slot in self.__hero_slots:
            if slot.get_state(window) == slot.IDLE:
                idle_slots.append(slot)
        return idle_slots

    def is_hero_banner_shown(self, window):
        return window.get_pixel_color(Position(392, 27)).similar_to("151B23", diff=16)

    def select_heroes(self, window, required=0):
        """
        :param window:
        :param required: number of heroes required to select.
        :return: True if found enough heroes.
        """
        logging.debug("enter select_heroes, require %d" % required)
        window.move_to(Position(135, 125))
        # scroll to most left
        window.scroll(vertical=-100)
        # try all heroes... 30 is the number of hero, except most right several
        selected = 0
        for i in range(50):
            window.scroll(vertical=1)  # range between hero avatar
            time.sleep(0.5)
            avatar_test_positions = [Position(24 + 147 * avatar_index, 209) for avatar_index in range(8)]
            for test_position in avatar_test_positions:
                if window.get_pixel_color(test_position).similar_to("E7F3F7", diff=16):
                    window.move_to(test_position)
                    window.left_click()
                    selected = selected + 1
                    if selected >= required:
                        return True
                    time.sleep(1)
                    break


if __name__ == "__main__":
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    scene = SceneCombatHeroSelection()
    if scene.match(window_handle):
        print("match!")
        print("hero banner: ", scene.is_hero_banner_shown(window_handle))
        idle_slots = scene.idle_hero_slots(window_handle)
        if len(idle_slots) == 0:
            print("all slot has heroes.")
        else:
            scene.select_heroes(window_handle, len(idle_slots))
    else:
        print("NOT match!")
