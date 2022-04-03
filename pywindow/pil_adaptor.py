#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/28
import time
import win32gui

from PIL import ImageGrab

from pywindow import Position
from pywindow.window import get_window_handle


def do_grab(filename):
    window = get_window_handle("Cadria Item Shop")
    window.set_foreground()
    window_rect = window.get_rect()
    print("window rect:", window_rect)
    image = ImageGrab.grab()
    image2 = image.crop((window_rect.left, window_rect.top, window_rect.right, window_rect.bottom))
    image2.save("D:\\window.bmp")

        # pix = image.load()
        # for y in range(30):
        #     for x in range(30):
        #         now_p = window_left_top.add(Position(x, y))
        #         color = pix[now_p.x, now_p.y]
        #         color_str = "".join(["%02X" % c for c in color][::-1])
        #         f.write("(%3d,%3d)=%s," % (x, y, color_str))
        #     f.write("\n")




if __name__ == "__main__":
    time_start = time.time()
    do_grab("D:\\color.txt")
    time_end = time.time()
    print("COST:", time_end - time_start)
