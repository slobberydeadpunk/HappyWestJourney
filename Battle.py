# -*- coding: utf-8 -*-
__author__ = 'Jackie'

from ConstantDefinition import TEAM_MEMBER_COUNT, LAST_TEAM_MEMBER_INDEX

class Battle(object):

    def __init__(self, team_one, team_two):
        self.__team_one, self.__team_two = self._get_attack_sequence(team_one, team_two)

    def _get_attack_sequence(self, team_one, team_two):      # 先手判定
        return team_one, team_two

    '''
    Return Value: 如果已经有队伍胜出则返回True，否则返回 False
    '''
    def attack(self, active_team, positive_team, pos):
        if active_team.all_role_killed():
            print "Winner is %s" % str(positive_team)
            return True

        role = active_team.get_role_by_pos(pos)     # 根据回合数选取先手队的角色
        if role is not None:                        # 回合位置空的话什么都不做
            attack = role.get_atk()
            target_role = positive_team.get_target_by_pos(pos)
            if target_role is not None:
                target_role.rem_health(attack)
                print "Team: %s, Role: %s 攻击 Team: %s, Role: %s, 伤害: %d, 剩余血量: %d" % (
                    str(active_team), role.get_name(),
                    str(positive_team), target_role.get_name(),
                    attack,
                    target_role.get_health()
                )
                if not target_role.is_alive():
                    print "Team: %s, Role: %s is killed!!!" % (str(positive_team), target_role.get_name())
            else:
                print "Winer is %s" % str(active_team)
                return True

        return False



    def start(self):
        round_count = 30            # 回合数
        round = 1

        while round <= 30:
            print "================================================================"
            print "Round %d BEGIN" % round
            pos = 0
            complete_flag = False

            while pos < TEAM_MEMBER_COUNT:
                if self.attack(self.__team_one, self.__team_two, pos):            # 该回合先手
                    complete_flag = True
                    break
                if self.attack(self.__team_two, self.__team_one, pos):
                    complete_flag = True
                    break
                pos += 1

            if complete_flag:
                break

            round += 1


