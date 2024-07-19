"""
怪物子类
"""
from Character.Character import Character


class Monster(Character):
    def __init__(self, name, max_hp, max_energy, max_attack, max_defense, max_crit_rate, max_dodge_rate, max_action_points):
        super().__init__(name, max_hp, max_energy, max_attack, max_defense, max_crit_rate, max_dodge_rate, max_action_points)
        self.passive_skill = []