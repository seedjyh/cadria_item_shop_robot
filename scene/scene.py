#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3

"""
This package contains descriptions of all kinds of scene.
"""
import time
from abc import ABCMeta, abstractmethod

from pywindow import Position
from pywindow.actor import Actor
from pywindow.colour import Colour
from robot.setting import SLEEP_AFTER_ACTION


class MatchRule:
    def __init__(self, position, colour):
        self.position = position
        self.colour = colour

    def __str__(self):
        return "Position:{}, Colour:{}".format(self.position, self.colour)


class Scene:
    """
    description of the entire window.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Initialize the object.
        """
        self._scene_rules = []

    def _append_rule(self, x, y, colour):
        """
        use this method in __init__ of child class.
        :param x: x index in window rect
        :param y: y index in window rect
        :param colour: colour in hex form, such as "A1B2C3"
        :return: None
        """
        self._scene_rules.append(MatchRule(Position(x, y), colour))

    def match(self, window_image):
        """
        Identify if the type of current scene of game is this type
        :param window_image: An object of class from PIL.Image.Image::load() contains window part.
        :return: True means current scene matches the current class.
        """
        return self.match_with_rules(self._scene_rules, window_image)

    def match_with_rules(self, rules, window_image):
        """
        match each rule in parameter rules
        :param rules: list of MatchRule objects.
        :return: True for matching all rules in parameter.
        """
        if len(rules) == 0:
            return False
        for rule in rules:
            pos = rule.position
            actual_color_str = "".join(["%02X" % c for c in window_image[pos.x, pos.y]][::-1])
            actual_color = Colour(actual_color_str)
            if not actual_color.similar_to(rule.colour, 16):
                # print("It's NOT scene:", type(self), "unmatch rule:", rule, ", actual color:", actual_color)
                return False
        # print("It IS scene:", type(self))
        return True

    @staticmethod
    def _wait_after_action(times = 1):
        time.sleep(SLEEP_AFTER_ACTION * times)

    @abstractmethod
    def exit(self):
        """
        go back to scene "Shop", the most basic scene.
        :param window:
        :return:
        """
        pass


if __name__ == "__main__":
    pass
