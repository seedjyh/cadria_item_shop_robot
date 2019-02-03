#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/11
from abc import ABCMeta, abstractmethod


class Task:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def do(self, window):
        """

        :param window: handle of game window.
        :return: True means task finished, next task shell be done, False requiring this task do() again.
        """
        pass


if __name__ == "__main__":
    pass
