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


class Scene:
    """
    description of the entire window.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def match(self, window):
        """
        Identify if the type of current scene of game is this type
        :param window: pywindow.window.Window
        :return:
        """
        # TODO: change it to `def match_rules()` returns a list of MatchRule objects.
        pass


if __name__ == "__main__":
    pass
