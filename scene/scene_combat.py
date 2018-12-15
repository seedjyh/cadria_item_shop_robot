#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/4
from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule
from scene.grid_combat_level import GridCombatLevel


class SceneCombat(Scene):
    """
    Select difficulty level of combat.
    """
    LEVEL_NORMAL = 0
    LEVEL_EXAM = 1
    LEVEL_NIGHTMARE = 2

    STATE_FREE = 0
    STATE_COMBATING = 1
    STATE_RETURNED = 2

    def __init__(self):
        self.__levels = [
            GridCombatLevel(Position(253, 298)),
            GridCombatLevel(Position(412, 298)),
            GridCombatLevel(Position(570, 298)),
        ]

    def match_rules(self, window):
        return [
            MatchRule(Position(122, 70), Colour("0B218E")),
            MatchRule(Position(122, 72), Colour("2D2F4F")),
            MatchRule(Position(122, 74), Colour("D9D8DF")),
        ]

    def exit(self, window):
        window.move_to(Position(79, 638))
        window.left_click()

    def get_state(self, window):
        if self.__is_free(window):
            return self.STATE_FREE
        elif self.__is_retuend(window):
            return self.STATE_RETURNED
        else:
            return self.STATE_COMBATING

    def select_level(self, window, level):
        if 0 <= level < len(self.__levels):
            self.__levels[level].left_click(window)

    def __is_free(self, window):
        rules = [
            MatchRule(Position(609, 403), Colour("315BD3")),
            MatchRule(Position(611, 403), Colour("89E5F7")),
            MatchRule(Position(613, 403), Colour("477FBD")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour, 8):
                return False
        return True

    def __is_retuend(self, window):
        rules = [
            MatchRule(Position(385, 503), Colour("244893")),
            MatchRule(Position(387, 503), Colour("91C8E7")),
            MatchRule(Position(389, 503), Colour("244894")),
        ]
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour, 8):
                return False
        return True

    def welcome_back(self, window):
        window.move_to(Position(600, 400))
        window.left_click()

if __name__ == "__main__":
    pass
