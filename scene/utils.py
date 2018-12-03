#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/16
import time

from scene.scene_drawing_advanced import SceneDrawingAdvanced
from scene.scene_equipment_repairment import SceneEquipmentRepairment
from scene.scene_exploration_finished import SceneExplorationFinished
from scene.scene_exploration_hero_selection import SceneExplorationHeroSelection
from scene.scene_exploration_location_list import SceneExplorationLocationList
from scene.scene_item_level_up import SceneItemLevelUp
from scene.scene_manufacture import SceneManufacture
from scene.scene_manufacture_one_item import SceneManufactureOneItem
from scene.scene_store_normal import SceneStoreNormal
from scene.scene_tavern import SceneTavern
from scene.scene_transaction import SceneTransaction


def go_to_scene(window, target=SceneStoreNormal()):
    print("enter go_to_scene")
    scene_list = [
        SceneDrawingAdvanced(),
        SceneEquipmentRepairment(),
        SceneExplorationFinished(),
        SceneItemLevelUp(),
        SceneManufacture(),
        SceneManufactureOneItem(),
        SceneStoreNormal(),
        SceneTavern(),
        SceneTransaction(),
        SceneExplorationLocationList(),
        SceneExplorationHeroSelection(),
    ]
    # go back to SceneStoreNormal
    while True:
        if SceneStoreNormal().match(window):
            break
        if target.match(window):
            return True
        for test_scene in scene_list:
            if test_scene.match(window):
                test_scene.exit(window)
    # go from SceneStoreNormal to target
    return SceneStoreNormal().go_to_scene(window, target)


if __name__ == "__main__":
    pass
