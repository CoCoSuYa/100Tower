import Cards.AttackCard

attack_cards = []


def init_all_cards():
    """
    初始化所有卡牌
    :return:
    """
    global attack_cards
    attack_cards.append(Cards.AttackCard.AttackCard("刺击", "基于攻击力造成等值无视护盾的穿透伤害", "attack", 1, ["Shield Ignore", "Piercing"]))
    attack_cards.append(Cards.AttackCard.AttackCard("砍击", "基于攻击力造成等值切割伤害", "attack", 1, ["Cutting"]))
    attack_cards.append(Cards.AttackCard.AttackCard("猛击", "基于攻击力造成1.3倍切割伤害，50%概率造成5层流血效果", "attack", 2, ["Cutting", "Bleeding"], 1.3))
    return attack_cards
