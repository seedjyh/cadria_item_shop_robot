#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/2
import time

from pywindow import Position
from pywindow.colour import Colour
from pywindow.window import get_window_handle
from scene import Scene, MatchRule
from scene.grid_exploration_hero_slot import GridExplorationHeroSlot


class SceneExplorationHeroSelection(Scene):
    def __init__(self):
        self.__hero_slots = [
            GridExplorationHeroSlot(Position(285, 471)),
            GridExplorationHeroSlot(Position(453, 471)),
            GridExplorationHeroSlot(Position(621, 471)),
            GridExplorationHeroSlot(Position(789, 471)),
        ]

    def match(self, window):
        rules = [
            MatchRule(Position(1167, 719), Colour("3DFFA4")),
            MatchRule(Position(1168, 720), Colour("3DFEA3")),
            MatchRule(Position(1169, 721), Colour("32D78A")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour, 8):
                return False
        return True

    def exit(self, window):
        if self.is_hero_banner_shown(window):
            window.move_to(Position(398, 483))
            window.left_click()
        else:
            window.move_to(Position(1207, 117))
            window.left_click()

    def hero_slot_list(self):
        return self.__hero_slots

    def is_hero_banner_shown(self, window):
        return window.get_pixel_color(Position(392, 27)).similar_to("1D2632", diff=16)

    def select_heroes(self, window, required=0):
        """

        :param window:
        :param require: number of heroes required to select.
        :return: True if found enough heroes.
        """
        print("enter select_heroes, require", required)
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
    scene = SceneExplorationHeroSelection()
    if scene.match(window_handle):
        print("match!")
        print("hero banner: ", scene.is_hero_banner_shown(window_handle))
        for i in range(4):
            print("index=%d, state=%d" % (i, scene.hero_slot_list()[i].get_state(window_handle)))
        scene.exit(window_handle)
    else:
        print("NOT match!")
