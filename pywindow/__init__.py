#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/8


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, position):
        return Position(self.x + position.x, self.y + position.y)

    def __str__(self):
        return "(x=%d,y=%d)" % (self.x, self.y)


if __name__ == "__main__":
    pass
