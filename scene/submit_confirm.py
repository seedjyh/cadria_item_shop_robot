#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/5
from pywindow import Position
from .scene import Scene


class SubmitConfirm(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(411, 285, "49ACF4")
        self._append_rule(505, 534, "111BB0")
        self._append_rule(737, 534, "037C3F")

    def submit(self):
        self._actor.left_click(Position(749, 574))
        self._wait_after_action(times=3)  # wait disappear of banner

    def submit_if_match(self):
        if self.match():
            self.submit()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
