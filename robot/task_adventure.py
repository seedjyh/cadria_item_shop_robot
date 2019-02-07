#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/7
from pywindow.window import get_window_handle
from robot import setting
from robot.task import Task
from scene.adventure_choose_hero import AdventureChooseHero
from scene.adventure_locations import AdventureLocations
from scene.combat_returned import CombatReturned
from scene.shop import Shop
from scene.tavern import Tavern
from scene.utils import go_to_shop, assert_scene
from scene.adventure_locations import AdventureLocations


class TaskAdventure(Task):
    def __init__(self):
        self._location_index = 0

    def do(self, window):
        go_to_shop(window)
        assert_scene(Shop, window).go_to_tavern()
        tavern = assert_scene(Tavern, window)
        for i in range(6):
            if tavern.adventure_slot_completed(i):
                tavern.left_click_adventure_slot(i)
                self.handle_adventure_result(window)
            if tavern.adventure_slot_idle(i):
                tavern.left_click_adventure_slot(i)
                self.try_start_adventure(window)

    def handle_adventure_result(self, window):
        now = assert_scene(CombatReturned, window)
        now.exit()

    def try_start_adventure(self, window):
        now = assert_scene(AdventureLocations, window)
        now.go_to_regine_one()
        now.select_location(self._location_index)
        self._location_index = (self._location_index + 1) % 9
        self.try_to_go(window)

    def try_to_go(self, window):
        now = assert_scene(AdventureChooseHero, window)
        required_count = now.required_heroes_count()
        if now.banner_is_hidden():
            if required_count == 0:
                now.go_combat()
                return True
            now.show_banner()
        # banner is shown
        now.move_to_banner()
        now.scroll_banner_most_left()
        for i in range(50):
            if required_count <= 0:
                now.hide_banner()
                now.go_combat()
                return True
            required_count -= now.select_free_heroes(required_count)
            now.scroll_right_one_step()
        return False


if __name__ == "__main__":
    window = get_window_handle(setting.WINDOW_TITLE)
    window.set_foreground()
    TaskAdventure().do(window)
