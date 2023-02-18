from CharTypes.Damage import Damage


class Assasin(Damage):
    def __init__(self, health=120, AD=20, AP=25, mana=40, alive=True):
        super().__init__(health, AD, AP, mana, alive)
        self._execute_move_cost = 15;

    def execute(self, other):
        if self.manaCheck(self._execute_move_cost):
            other.die()
        else:
            print("Cannot use execute move, not enough mana")

    def slash(self, other):
        other.getHit(self._AD)
