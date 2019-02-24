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
from scene.shop_order import ShopOrder
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
        for point in shop.customer_points():
            window.left_click(point)
            time.sleep(1)
            # shop order
            shop_order = ShopOrder(window)
            if shop_order.match():
                if shop_order.match_with_rules(shop_order.rules_as_offer()):
                    shop_order.accept()
                else:
                    shop_order.exit()
                continue
            # customer
            if Customer(window).match():
                Customer(window).surcharge()
                Customer(window).buy()
            if Customer(window).match():
                Customer(window).surcharge()
                Customer(window).sell()
            if Customer(window).match():
                Customer(window).refuse()


if __name__ == "__main__":
    window = get_window_handle(setting.WINDOW_TITLE)
    window.set_foreground()
    TaskSell().do(window)
