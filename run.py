import Cards.CardList
import Character.Courage
import Character.Monster
import Cards.RootCard


def game_init():
    Cards.CardList.init_all_cards()
    courage = Character.Courage.Courage()
    monster = Character.Monster.Fish()
    return courage, monster

player, monster = game_init()
