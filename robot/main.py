#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/7
import logging
import time

from pywindow.window import get_window_handle
from robot.task_collect_resource import TaskCollectResource
from robot.task_handle_bank import TaskHandleBank
from robot.task_handle_faction_war import TaskHandleFactionWar


def main():
    logging.basicConfig(
        format="%(asctime)s|%(name)s|%(message)s",
        datefmt="%Y-%m-%d %I:%M:%S",
        level=logging.DEBUG,
    )
    window_text = "Cadria Item Shop"
    window_handle = get_window_handle(window_text)
    window_handle.set_foreground()
    time.sleep(1)
    tasks = [
        TaskCollectResource(),
        # TaskHandleBank(),
        TaskHandleFactionWar(),
    ]
    while True:
        time.sleep(1)
        for task in tasks:
            task.do(window_handle)


if __name__ == "__main__":
    main()

