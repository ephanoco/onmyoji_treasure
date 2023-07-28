#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 17:16
# @Author  : Samuel
# @File    : beans_thrower.py
from utils.cursor import Cursor
from utils.matcher import Matcher
from utils.pt_dict import pt_dict


class BeansThrower(Matcher, Cursor):
    def __init__(self):
        super().__init__()
        self.rel_path = 'static/templates/town/demon_parade/'

    def throw_beans(self):
        self.__invite_friends()  # Choose the friend
        # Enter the ghost selection screen
        pt_enter = pt_dict['town']['demon_parade']['enter']
        if not pt_enter:
            pt_enter = pt_dict['town']['demon_parade']['enter'] = super().match(
                super().get_path(f'{self.rel_path}enter.png'))[0]
        super().left_click(pt_enter, (1, 2))
        # TODO
        # Choose the ghost
        pt_start = pt_dict['town']['demon_parade']['start']
        if not pt_start:
            pt_start = pt_dict['town']['demon_parade']['start'] = super().match(
                super().get_path(f'{self.rel_path}start.png'))[0]

    def __invite_friends(self, index: str = ''):
        # Clicking on the '+' button
        pt_invite = pt_dict['town']['demon_parade']['invite']
        if not pt_invite:
            pt_invite = pt_dict['town']['demon_parade']['invite'] = super().match(
                super().get_path(f'{self.rel_path}invite.png'))[0]
        super().left_click(pt_invite, (1, 2))
        # Invite someone from friend list
        scatter = self.__get_scatter()
        cur_index = 0 if not index else int(index)
        super().left_click(scatter[cur_index], (1, 2))

    def __get_scatter(self):
        scatter = pt_dict['town']['demon_parade']['scatter']
        if not scatter:
            x, y = super().match(super().get_path(f'{self.rel_path}friends.png'))[0]
            scatter = pt_dict['town']['demon_parade']['scatter'] = [(x + 100, y + 64), (x + 316, y + 64),
                                                                    (x + 100, y + 131), (x + 316, y + 131),
                                                                    (x + 100, y + 199), (x + 316, y + 199),
                                                                    (x + 100, y + 266), (x + 316, y + 266)]
        print(f'scatter: {scatter}')
        return scatter


if __name__ == '__main__':
    beans_thrower = BeansThrower()
    beans_thrower.throw_beans()
