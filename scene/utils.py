#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/16
import time

from scene.scene_item_level_up import SceneItemLevelUp
from scene.scene_manufacture import SceneManufacture
from scene.scene_store_normal import SceneStoreNormal


def go_to_scene_store_normal(window):
    """
    keep click until arrive the scene "Store Normal"
    :param window:
    :return: None
    """
    scene_list = [
        SceneStoreNormal(),
        SceneManufacture(),
        SceneItemLevelUp()
    ]
    for scene in scene_list:
        if scene.match(window):
            if scene.__class__ == SceneStoreNormal:
                return
            else:
                scene.exit(window)
                time.sleep(1)
    else:
        print("unknown scene...")


if __name__ == "__main__":
    pass
