"""
攻击类卡牌
"""
from Cards.RootCard import RootCard


class AttackCard(RootCard):
    def __init__(self, name, description, card_type, cost, effects, damage_multiplier=1):
        super().__init__(name, description, card_type, cost)
        self.shield_ignore = False
        self.damage_multiplier = damage_multiplier
        self.effects = effects

    def Card_Effect(self, user, target, effect_name):
        """
        使卡牌效果生效
        """
        if effect_name == "Shield Ignore":
            self.shield_ignore = True
        elif effect_name == "Piercing":
            pass
        elif effect_name == "Cutting":
            pass
        elif effect_name == "Bleeding":
            pass

