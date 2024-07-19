"""
英雄子类
"""
from Character.Character import Character


class Hero(Character):
    def __init__(self, name, max_hp, max_energy, max_attack, max_defense, max_crit_rate, max_dodge_rate, max_action_points):
        super().__init__(name, max_hp, max_energy, max_attack, max_defense, max_crit_rate, max_dodge_rate, max_action_points)
        self.active_skill = ""
        self.passive_skill = []
        self.talent = []

    def add_active_skill(self, skill_name):
        """
        给英雄单位学习主动技能
        :param skill_name:
        """
        self.active_skill = skill_name

    def switch_active_skill(self, skill_name):
        """
        切换英雄单位主动技能
        :param skill_name:
        """
        self.active_skill = skill_name

    def add_passive_skill(self, skill_name):
        """
        给英雄单位学习技能
        :param skill_name:
        """
        self.passive_skill.append(skill_name)

    def remove_passive_skill(self, skill_name):
        """
        给英雄单位遗忘技能
        :param skill_name:
        """
        if len(self.passive_skill) == 0:
            print("英雄单位没有技能")
            return False
        else:
            if skill_name not in self.passive_skill:
                print("英雄单位没有这个技能")
                return False
            self.passive_skill.remove(skill_name)
            return True

    def add_talent(self, talent_name):
        """
        给英雄单位学习天赋
        :param talent_name:
        """
        self.talent.append(talent_name)

    def remove_talent(self, talent_name):
        """
        给英雄单位移除天赋
        :param talent_name:
        """
        if len(self.talent) == 0:
            print("英雄单位没有天赋")
            return False
        else:
            if talent_name not in self.talent:
                print("英雄单位没有这个天赋")
                return False
            self.talent.remove(talent_name)
