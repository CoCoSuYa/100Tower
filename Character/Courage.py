"""
英雄角色类：勇者
"""
from Character.Hero import Hero


class Courage(Hero):
    def __init__(self):
        super().__init__("剑士", 100, 50, 15, 10, 5, 5, 3)
        self.default_cards = []