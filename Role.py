# -*- coding: utf-8 -*-
__author__ = 'Jackie'



class Role(object):

    def __init__(self, max_health, atk, name=''):
        self.__max_health = max_health
        self.__cur_health = max_health
        self.__atk = atk
        self.__is_alive = False
        self.__name = name

    def get_name(self):
        return self.__name

    def is_alive(self):
        return self.__cur_health > 0

    def get_atk(self):
        return self.__atk

    def get_health(self):
        return self.__cur_health

    def add_health(self, v):
        if self.__cur_health + v < self.__max_health:
            self.__cur_health += v
        else:
            self.__cur_health = self.__max_health           # 回满血

    def rem_health(self, v):
        self.__cur_health -= v

        if self.__cur_health < 0:
            self.__cur_health = 0
            self.__is_alive = False


    def __str__(self):
        return "Max: %d, Current: %d, Attack: %d" % (self.__max_health, self.__cur_health, self.__atk)

    def __repr__(self):
        return "Max: %d, Current: %d, Attack: %d" % (self.__max_health, self.__cur_health, self.__atk)

