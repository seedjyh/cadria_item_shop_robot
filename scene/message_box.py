#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/12
from pywindow import Position
from .scene import Scene


class MessageBox(Scene):
    """
    网络已断开
    登录信息已过期
    ……
    """
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(630, 175, "6BC7FF")
        self._append_rule(630, 195, "2E4A7F")
        self._append_rule(630, 534, "037C3F")

    def exit(self):
        self._actor.left_click(Position(648, 568))


if __name__ == "__main__":
    pass
