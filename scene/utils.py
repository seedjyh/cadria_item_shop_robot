#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3
from .import shop, unknown, tavern, login
from .scene import Scene


def identify_scene(window_image):
    for now_scene in Scene.__subclasses__():
        obj = now_scene()
        if obj.match(window_image):
            print("match scene!", obj)
            return obj
    else:
        print("unmatch any scene!")
        return unknown.Unknown()


def go_to_shop(window):
    for i in range(10):
        scene = identify_scene(window)
        if isinstance(scene, shop.Shop):
            break
        else:
            scene.exit()
    else:
        raise Exception("failed to reach shop scene in limited steps")


def assert_scene(scene_class, window):
    """
    create an object of Scene class, return the object is match.
    raise exception if NOT.
    :param scene_class: subclass of class Scene
    :param window: window handle.
    :return: object of the scene_class.
    """
    scene = scene_class(window)
    if not scene.match():
        errmsg = "UNEXPECTED SCENE! expected %s" % scene_class.__name__
        print(errmsg)
        raise Exception(errmsg)
    return scene


def exit_if_match(scene, window):
    now = scene(window)
    if now.match():
        print("It's ", scene, ", exiting...")
        now.exit()
    else:
        print("It's NOT ", scene, ", no need to exit")


if __name__ == "__main__":
    from pywindow.window import get_window_handle
    from robot import setting
    window_handle = get_window_handle(setting.WINDOW_TITLE)
    window_handle.set_foreground()
    print(identify_scene(window_handle))
