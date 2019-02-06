#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/4
from pywindow import Position
from robot.task import Task
from scene.combat import Combat
from scene.combat_choose_hero import CombatChooseHero
from scene.crafting_one import CraftingOne
from scene.faction_war import FactionWar
from scene.item_upgraded import ItemUpgraded
from scene.preparation import Preparation
from scene.shop import Shop
from scene.submit_confirm import SubmitConfirm
from scene.tavern import Tavern
from scene.utils import go_to_shop, assert_scene, exit_if_match
from scene import combat_returned, repair_item


class TaskHandleFactionWar(Task):
    def __init__(self):
        pass

    def do(self, window):
        go_to_shop(window)
        assert_scene(Shop, window).go_to_tavern()
        assert_scene(Tavern, window).go_to_faction_war()
        assert_scene(FactionWar, window).go_to_contribute()
        if Preparation(window).match():
            self.do_preparation(window)
        elif Combat(window).match():
            self.do_combat(window)

    def do_preparation(self, window):
        now = assert_scene(Preparation, window)
        while now.enough_items():
            now.submit_items()
            SubmitConfirm(window).submit_if_match()
        if now.is_slot_list_hide():
            now.show_slot_list()
        for i in range(6):
            if now.is_slot_done(i):
                now.left_click_slot(i)
                exit_if_match(ItemUpgraded, window)
        while now.some_slot_is_idle():
            now.craft()
            craft_scene = CraftingOne(window)
            if not craft_scene.match():
                return False
            if craft_scene.lack_of_resources():
                return False
            craft_scene.craft()

    def do_combat(self, window):
        now = assert_scene(Combat, window)
        if now.squad_is_back():
            now.check_out_squad()
        elif now.idle():
            now.left_click_nightmare()
            self.try_to_go(window)

    def try_to_go(self, window):
        now = assert_scene(CombatChooseHero, window)
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
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    task = TaskHandleFactionWar()
    task.do(window_handle)
