"""
卡牌基础构成
"""


class RootCard:
    """
    卡牌父类
    """
    def __init__(self, name, description, card_type, cost):
        self.name = name
        self.description = description
        self.card_type = card_type
        self.cost = cost

