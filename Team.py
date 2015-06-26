# -*- coding: utf-8 -*-
__author__ = 'Jackie'

from ConstantDefinition import TEAM_MEMBER_COUNT, LAST_TEAM_MEMBER_INDEX

class Team(object):

    def __init__(self, role_list=[], team_name=''):
        self.__role_list = role_list
        self.__name = team_name

        while len(self.__role_list) < TEAM_MEMBER_COUNT:            # 每个队伍6张卡
            self.__role_list.append(None)

        if len(self.__role_list) > TEAM_MEMBER_COUNT:
            self.__role_list = self.__role_list[0:TEAM_MEMBER_COUNT]

    def __str__(self):
        return self.__name

    def append_role(self, r):
        if len(self.__role_list) < TEAM_MEMBER_COUNT:
            self.__role_list.append(r)
        # TODO else throw

    def add_role(self, r, position):
        if position <= LAST_TEAM_MEMBER_INDEX:
            self.__role_list[position] = r
        # TODO else throw

    def all_role_killed(self):
        for role in self.__role_list:
            if role is not None:
                if role.is_alive():
                    return False
        return True

    def get_role_by_pos(self, pos):
        if self.__role_list[pos] is not None:
            role = self.__role_list[pos]
            if role.is_alive():
                return role
        return None

    def if_first_line_alive(self):
        pass

    def get_target_by_ouput_pos(self, pos):
        same_line_flag = True

        if pos >= 3:
            pos -= 3
            same_line_flag = False

        while pos <= LAST_TEAM_MEMBER_INDEX:
            role = self.__role_list[pos]
            if role is not None:
                if role.is_alive():
                    return role
            pos += 1
        return None





