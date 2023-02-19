from core.CharTypes.Skeleton.Damage import Damage


class Assassin(Damage):
    def __init__(self, name="Assassin", health=120, ad=20, ap=25, mana=40, alive=True):
        super().__init__(name, health, ad, ap, mana, alive)
        self._execute_move_cost = 15

    def execute(self, other):
        if self.mana_check(self._execute_move_cost):
            other.die()
        else:
            print("Cannot use execute move, not enough mana")

    def slash(self, other):
        other.get_hit(self._AD)

    def get_move1(self):
        pass

    def get_move2(self):
        pass

    def get_move3(self):
        pass

    def get_move4(self):
        pass
