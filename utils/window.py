#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 17:02
# @Author  : Samuel
# @File    : window.py
from ctypes.wintypes import HWND

import win32gui


class Window:
    def __init__(self):
        # self.hwnd: HWND = win32gui.FindWindow(None, '阴阳师 - MuMu模拟器')
        self.hwnd: HWND = self.get_hwnd()

    def get_hwnd(self):
        hwnd_list = self.get_hwnd_list()
        for hwnd in hwnd_list:
            wnd_text = self.get_wnd_text(hwnd)
            if 'MuMu模拟器' in wnd_text:
                return hwnd

    @staticmethod
    def get_wnd_text(hwnd):
        return win32gui.GetWindowText(hwnd)

    @staticmethod
    def get_hwnd_list():
        hwnd_list = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_list)
        return hwnd_list


if __name__ == '__main__':
    window = Window()
    window.get_hwnd()
