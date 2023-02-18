from CharTypes.Assasin import Assasin as ass
from CharTypes.Mage import Mage as mag
from CharTypes.Fighter import Fighter as fig
from CharTypes.Tank import Tank as tan


Player1 = ass()
Player2 = fig()

def healthReportP1():
    print("Player 1 now has {} health".format(Player1.gethealth()))

def healthReportP2():
    print("Player 2 now has {} health".format(Player2.gethealth()))

def sop(string):
    print(string)

def main():
    healthReportP2()
    Player1.basicAttack(Player2)
    sop("Player 1 used Basic attack on Player 2")
    healthReportP2()
    Player2.bite(Player1)
    sop("Player 2 used bite on Player 1")
    healthReportP1()
    Player1.barrage(Player2)
    sop("Player 1 used Barrage on Player 2")
    healthReportP2()
    Player2.seriousPunch(Player1)
    sop("Player 2 used Serious Punch on Player 1")
    healthReportP1()
    Player1.slash(Player2)
    sop("Player 1 used Slash on Player 2")
    healthReportP2()
    sop("Player 1 wins!")

if __name__ == '__main__':

   main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
