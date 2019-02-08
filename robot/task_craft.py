#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/7
from pywindow.window import get_window_handle
from robot import setting
from robot.task import Task
from scene.blueprint_upgraded import BlueprintUpgraded
from scene.crafting import Crafting
from scene.crafting_one import CraftingOne
from scene.item_upgraded import ItemUpgraded
from scene.shop import Shop
from scene.utils import go_to_shop, assert_scene, exit_if_match


class TaskCraft(Task):
    def __init__(self):
        self._item_index = 0

    def do(self, window):
        go_to_shop(window)
        shop = assert_scene(Shop, window)
        for i in range(6):
            if shop.completed_craft_slot(i):
                print("slot %d COMPLETED" % i)
                shop.left_click_craft_slot(i)
                exit_if_match(ItemUpgraded, window)
                exit_if_match(BlueprintUpgraded, window)
            else:
                print("slot %d NOT completed" % i)
        for i in range(6):
            if shop.idle_craft_slot(i):
                print("slot %d is IDLE" % i)
                shop.left_click_craft_slot(i)
                print("slot %d clicked" % i)
                self.handle_crafting(window)
            else:
                print("slot %d is NOT idle" % i)

    def handle_crafting(self, window):
        crafting = assert_scene(Crafting, window)
        crafting.choose_bookmark()
        crafting.choose_all_types()
        row = int(self._item_index / 3)
        column = self._item_index % 3
        self._item_index = (self._item_index + 1) % 9
        if crafting.valid_item(row, column):
            crafting.choose_item(row, column)
            if CraftingOne(window).match():
                self.handle_craft_one(window)
        crafting.exit()

    def handle_craft_one(self, window):
        craft_one = assert_scene(CraftingOne, window)
        if craft_one.lack_of_resources():
            craft_one.exit()
        else:
            craft_one.craft()


if __name__ == "__main__":
    window = get_window_handle(setting.WINDOW_TITLE)
    window.set_foreground()
    TaskCraft().do(window)
