#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/3

from .scene import Scene


class Unknown(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)

    def exit(self):
        self._window.tap_escape()


if __name__ == "__main__":
    pass
