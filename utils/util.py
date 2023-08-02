#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 17:02
# @Author  : Samuel
# @File    : util.py
import ctypes
import os.path
import sys
from functools import reduce


class Util:
    @staticmethod
    def get_path(path):
        cur_path = os.path.dirname(__file__)
        base_dir = os.path.dirname(cur_path)
        return os.path.join(base_dir, os.path.normcase(path))

    @staticmethod
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    @staticmethod
    def get_converted_pt_list(pt_list):
        return sorted(pt_list, key=lambda x: x[1])

    @staticmethod
    def query_mode(modes):
        # Select the mode
        for c, desc in modes.items():
            print(f"{c}. {desc}")
        choice = input("Select your mode: ")
        while choice not in modes:
            choice = input(f"Choose one of: {', '.join(modes)}: ")
        print(f"Role: {modes[choice]}")
        return choice

    @staticmethod
    def query_yes_no(question, default="yes"):
        """Ask a yes/no question via raw_input() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
                It must be "yes" (the default), "no" or None (meaning
                an answer is required of the user).

        The "answer" return value is True for "yes" or False for "no".
        """
        valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
        if default is None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            sys.stdout.write(question + prompt)
            choice = input().lower()
            if default is not None and choice == "":
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

    @staticmethod
    def get_val(nested_dict: dict, key: str):
        """
        Get a nested dictionary item using single dot-delimited string path.
        Example:
        my_dict = {'a': {'b': {'c': 123}}}
        get_val(my_dict, "a.b.c") # 123
        """
        return reduce(lambda d, k: d[k], key.split('.'), nested_dict)

    @staticmethod
    def set_val(nested_dict: dict, key: str, value):
        """
        Set a nested dictionary item using single dot-delimited string path.
        Example:
        set_val(my_dict, "very.very.many.levels", True)
        """
        *keys, last_key = key.split('.')
        for k in keys:
            if k not in nested_dict:
                nested_dict[k] = dict()
            nested_dict = nested_dict[k]
        nested_dict[last_key] = value


if __name__ == '__main__':
    util = Util()
    util.get_converted_pt_list([(735, 251), (977, 248), (707, 356), (945, 356), (675, 464), (945, 464)])
