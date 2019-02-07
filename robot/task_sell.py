#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/7
import time

from pywindow.window import get_window_handle
from robot import setting
from robot.task import Task
from scene.customer import Customer
from scene.shop import Shop
from scene.utils import go_to_shop, assert_scene

CLICK_COUNT = 100


class ColourChangeTester:
    def __init__(self, point):
        self.point = point
        self.origin_color = None
        self.new_color = None

    def set_oringin_color(self, color):
        self.origin_color = color

    def set_new_color(self, color):
        self.new_color = color

    def same_color(self):
        return self.origin_color.similar_to(self.new_color, diff=0)


class TaskSell(Task):
    def __init__(self):
        pass

    def do(self, window):
        go_to_shop(window)
        shop = assert_scene(Shop, window)
        for point in self.get_color_changed_point(shop):
            window.left_click(point)
            time.sleep(1)
            if Customer(window).match():
                Customer(window).surcharge()
                Customer(window).sell()
            if Customer(window).match():
                Customer(window).refuse()

    def get_color_changed_point(self, shop):
        testers = [ColourChangeTester(p) for p in shop.customer_points()]
        for t in testers:
            t.set_oringin_color(window.get_pixel_color(t.point))
        time.sleep(1)
        for t in testers:
            t.set_new_color(window.get_pixel_color(t.point))
        for t in testers:
            if not t.same_color():
                yield t.point


if __name__ == "__main__":
    window = get_window_handle(setting.WINDOW_TITLE)
    window.set_foreground()
    TaskSell().do(window)
