#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/14
from abc import ABCMeta, abstractmethod


class Area:
    """
    Area is similar to scene, the pixel index related to entire window. But smaller than scene.
    Scene is root and areas are branches and leaves and.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_state(self, window):
        pass


if __name__ == "__main__":
    pass
