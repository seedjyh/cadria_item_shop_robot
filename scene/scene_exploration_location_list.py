#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/12/2
import logging
import time

from pywindow import Position
from pywindow.colour import Colour
from scene import Scene, MatchRule
from scene.grid_exploration_location_zone import GridExplorationLocationZone


logger = logging.getLogger("SceneExplorationLocationList")


class SceneExplorationLocationList(Scene):
    """

    """
    def __init__(self):
        self.__zone_list = [
            GridExplorationLocationZone(Position(28, 141)),
            GridExplorationLocationZone(Position(28, 237)),
        ]

    def match_rules(self, window):
        return [
            MatchRule(position=Position(100, 61), colour=Colour("62D5F9")),
            MatchRule(position=Position(100, 63), colour=Colour("0F387C")),
            MatchRule(position=Position(100, 65), colour=Colour("56C8F8")),
        ]

    def exit(self, window):
        window.move_to(Position(67, 677))
        window.left_click()

    def zone_list(self):
        return self.__zone_list

    def select_location(self, window, index):
        """
        select exploration location for index 0 ~ 8
        :param window:
        :param index:
        :return:
        """
        logger.debug("selecting exploration location.")
        # scroll to most left
        window.move_to(Position(402, 365))
        for i in range(100):
            window.scroll(-1)
        time.sleep(1)
        for i in range(int(7.5 * index)):
            window.scroll(1)
        time.sleep(1)
        if index <= 6:
            window.move_to(Position(402, 365))
            window.left_click()
        elif index == 7:  # right boundary for scroll
            window.move_to(Position(697, 365))
            window.left_click()
        elif index == 8:  # right boundary for scroll
            window.move_to(Position(1036, 365))
            window.left_click()
        else:
            print("invalid exploration location %d, should be 0~8" % index)
            pass


if __name__ == "__main__":
    pass
