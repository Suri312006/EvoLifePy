from core.Characters.CharArchetypes.Assasin import Assassin as ass
from core.Characters.CharArchetypes.Mage import Mage as mag

Player1 = ass(name="lol")
Player2 = mag(name="okay")


def healthrep(player):
    print("{} has {} health ({}%)".format(player.get_name(), player.health_report()[0], player.health_report()[1]))


def sop(string):
    print(string)

def moverep(player,getmove,  other)
    print("{} used {} on {}".format(player.get_name, getmove[0],other.get_name ))

def main():
    healthrep(Player1)
    Player1.move1(Player2)
    sop("Player 1 used Basic attack on Player 2")

    healthrep(Player2)
    Player2.bite(Player1)
    sop("Player 2 used bite on Player 1")
    Player1.basic_attack(Player2)
    Player1.barrage(Player2)
    sop("Player 1 used Barrage on Player 2")
    healthrep(Player2)
    Player2.serious_punch(Player1)
    sop("Player 2 used Serious Punch on Player 1")
    healthrep(Player2)
    Player1.slash(Player2)
    sop("Player 1 used Slash on Player 2")
    healthrep(Player2)
    sop("Player 1 wins!")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
