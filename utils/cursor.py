#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 17:01
# @Author  : Samuel
# @File    : cursor.py
import random
import time

import win32api
import win32con


class Cursor:
    @staticmethod
    def __set_cursor_pos(pt):
        x, y = pt
        win32api.SetCursorPos((x, y))

    @staticmethod
    def __get_offset_pt(pt):
        x, y = pt
        offset_y = offset_x = random.randint(-5, 5)  # random.randint(0, 10)
        return x + offset_x, y + offset_y

    def left_click(self, pt, delay: int | float | tuple = None):
        offset_pt = self.__get_offset_pt(pt)
        self.__set_cursor_pos(offset_pt)
        time.sleep(0.1)
        x, y = offset_pt
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x, y)
        if isinstance(delay, int | float):
            time.sleep(delay)
        elif isinstance(delay, tuple):
            start, stop = delay
            random_delay = random.uniform(start, stop)
            time.sleep(random_delay)
