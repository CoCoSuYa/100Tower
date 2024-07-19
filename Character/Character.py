"""
角色基础属性
"""


class Character:
    """
    角色父类
    """

    def __init__(self, name, max_hp, max_energy, max_attack, max_defense, max_crit_rate, max_dodge_rate, max_action_points):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_energy = max_energy
        self.current_energy = 0
        self.max_attack = max_attack
        self.current_attack = max_attack
        self.max_defense = max_defense
        self.current_defense = max_defense
        self.max_crit_rate = max_crit_rate
        self.current_crit_rate = max_crit_rate
        self.max_dodge_rate = max_dodge_rate
        self.current_dodge_rate = max_dodge_rate
        self.max_action_points = max_action_points
        self.current_action_points = max_action_points
        self.shield = 0

    def heal(self, hp):
        """
        恢复生命值
        :param hp:
        """
        self.current_hp = min(self.max_hp, self.current_hp + hp)

    def take_damage(self, damage):
        """
        承受伤害
        :param damage:
        """
        if self.shield > 0:
            if self.shield >= damage:
                self.shield -= damage
                damage = 0
            else:
                damage -= self.shield
                self.shield = 0
        self.current_hp = max(0, self.current_hp - damage)

    def take_energy(self, energy):
        """
        恢复/消耗能量
        :param energy:
        :return:
        """
        self.current_energy = min(self.max_energy, self.current_energy + energy)

    def take_attack_number(self, number):
        """
        增强/削弱攻击力(数值)
        """
        self.current_attack = min(self.max_attack, self.current_attack + number)

    def take_attack_percent(self, amount):
        """
        增强/削弱攻击力(百分比)
        """
        self.current_attack = self.max_attack * amount

    def take_defense_number(self, number):
        """
        增强/削弱防御力(数值)
        """
        self.current_defense = min(self.max_defense, self.current_defense + number)

    def take_defense_percent(self, amount):
        """
        增强/削弱防御力(百分比)
        """
        self.current_defense = self.max_defense * amount

    def take_crit_rate_number(self, number):
        """
        增强/削弱暴击率(数值)
        """
        self.current_crit_rate = min(self.max_crit_rate, self.current_crit_rate + number)

    def take_crit_rate_percent(self, amount):
        """
        增强/削弱暴击率(百分比)
        """
        self.current_crit_rate = self.max_crit_rate * amount

    def take_dodge_rate_number(self, number):
        """
        增强/削弱闪避率(数值)
        """
        self.current_dodge_rate = min(self.max_dodge_rate, self.current_dodge_rate + number)

    def take_dodge_rate_percent(self, amount):
        """
        增强/削弱闪避率(百分比)
        """
        self.current_dodge_rate = self.max_dodge_rate * amount

    def take_action_points(self, points):
        """
        恢复/消耗行动点
        :param points:
        """
        self.current_action_points = min(self.max_action_points, self.current_action_points + points)

    def take_shield(self, shield, amount=1):
        """
        获得护盾
        :param amount:
        :param shield:
        """
        self.shield += self.current_defense * amount
