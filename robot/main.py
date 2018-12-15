#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/7
import logging
import time

from pywindow.window import get_window_handle
from robot.task_clean_completed_primary_manufacture_slot import TaskCleanCompletedPrimaryManufactureSlot
from robot.task_process_exploration import TaskProcessExploration
from robot.task_process_faction_war import TaskProcessFactionWar
from robot.task_process_manufacture import TaskProcessManufacture

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
        TaskProcessExploration(),
        TaskProcessManufacture(),
        TaskCleanCompletedPrimaryManufactureSlot(),
        TaskProcessFactionWar(),
    ]
    while True:
        for task in tasks:
            task.do(window_handle)

if __name__ == "__main__":
    main()

