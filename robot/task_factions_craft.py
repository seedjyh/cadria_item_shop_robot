#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/5
import logging
import time

from robot.task import Task
from scene.blueprint_upgraded import BlueprintUpgraded
from scene.crafting_one import CraftingOne
from scene.faction_submit import FactionSubmit
from scene.factions import Factions
from scene.item_upgraded import ItemUpgraded
from scene.no_blueprint import NoBlueprint
from scene.one_faction import OneFaction
from scene.order_completed import OrderCompleted
from scene.shop import Shop
from scene.submit_confirm import SubmitConfirm
from scene.tavern import Tavern
from scene.utils import go_to_shop, assert_scene, exit_if_match


class TaskFactionsCraft(Task):
    def __init__(self):
        pass

    def do(self, window):
        go_to_shop(window)
        assert_scene(Shop, window).go_to_tavern()
        assert_scene(Tavern, window).go_to_factions()
        for i in range(3):
            assert_scene(Factions, window).go_to_faction(i)
            self.handle_faction(window)

    def handle_faction(self, window):
        faction = assert_scene(OneFaction, window)
        if faction.new_order():
            faction.accept_order()
        # handle "done" slot
        if faction.is_slot_list_hide():
            faction.show_slot_list()
        for i in range(6):
            if faction.is_slot_done(i):
                faction.left_click_slot(i)
                exit_if_match(ItemUpgraded, window)
                exit_if_match(BlueprintUpgraded, window)
        time.sleep(3)
        # submit items if possible
        for i in range(4):
            if faction.chunk_is_ready(i):
                faction.left_click_chunk(i)
                assert_scene(FactionSubmit, window).submit()
                SubmitConfirm(window).submit_if_match()
                exit_if_match(OrderCompleted, window)
        # craft items if possible
        faction = assert_scene(OneFaction, window)
        for i in range(4):
            if faction.some_slot_is_idle() and faction.chunk_is_idle(i):
                faction.left_click_chunk(i)
                if NoBlueprint(window).match():
                    NoBlueprint(window).exit()
                else:
                    self.handle_craft(window)
        faction.exit()

    def handle_craft(self, window):
        craft = assert_scene(CraftingOne, window)
        if craft.lack_of_resources():
            craft.exit()
        else:
            craft.craft()


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    #task = TaskFactionsCraft()
    #task.do(window_handle)
    assert_scene(OneFaction, window_handle)
