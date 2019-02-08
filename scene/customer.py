#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/7

from .scene import Scene


class Customer(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(703, 161, "3667A0")
        self._append_rule(643, 186, "1E4CEA")
        self._append_rule(1131, 186, "1E4EEA")

    def refuse(self):
        self._window.tap_letter("r")
        self._wait_after_action()

    def sell(self):
        self._window.tap_letter("d")
        self._wait_after_action()

    def discount(self):
        self._window.tap_letter("a")
        self._wait_after_action()

    def surcharge(self):
        self._window.tap_letter("q")
        self._wait_after_action()

    def buy(self):
        self._window.tap_letter("d")
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
