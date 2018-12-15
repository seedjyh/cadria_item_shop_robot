#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/8

"""
This package contains descriptions of all kinds of scene.
"""

from abc import ABCMeta, abstractmethod


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

    def match(self, window):
        """
        Identify if the type of current scene of game is this type
        :param window: pywindow.window.Window
        :return: True means current scene matches the current class.
        """
        rules = self.match_rules(window)
        for rule in rules:
            if not window.get_pixel_color(rule.position).similar_to(rule.colour, 8):
                print("It's NOT scene:", type(self), "unmatch rule:", rule)
                return False
        print("It IS scene:", type(self))
        return True

    @abstractmethod
    def match_rules(self, window):
        """
        return a list of MatchRule objects, defines if the *window* is current scene.
        :param window:
        :return: MatchRule[]
        """
        pass


if __name__ == "__main__":
    pass
