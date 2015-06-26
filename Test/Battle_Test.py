# -*- coding: utf-8 -*-
__author__ = 'Jackie'

from Role import Role
from Team import Team
from Battle import Battle

if __name__ == '__main__':
    r1 = Role(100000, 20000, 'AA')
    r2 = Role(50000, 10000, 'BB')
    r3 = Role(30000, 8000, 'CC')
    l1 = [r1, r2, r3]
    t1 = Team(l1, 'Team One')

    r4 = Role(100000, 20000, 'AA')
    r5 = Role(50000, 10000, 'BB')
    r6 = Role(30000, 8000, 'CC')
    l2 = [None, None, None, r4, r5, r6]
    t2 = Team(l2, 'Team Two')

    b = Battle(t1, t2)
    b.start()


