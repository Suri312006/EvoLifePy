from core.Characters.Skeleton.Damage import Damage



class Assassin(Damage):
    def __init__(self, name="Assassin", health=120, ad=20, ap=25, mana=40, alive=True):
        super().__init__(name, health, ad, ap, mana, alive)
        self._execute_move_cost = 15
        self._slash_move_cost = 10

    def execute(self, other):

        if self.mana_check(self._execute_move_cost):
            other.die()
        else:
            print("Cannot use execute move, not enough mana")

    def slash(self, other):

        if self.mana_check(self._slash_move_cost):
            other.get_hit(1.5*self._AD)
        else:
            print("Cannot use Slash move, not enough mana")




    def move3(self, other):
        self.slash(other)
    def move4(self,other):
        self.execute(other)





    def get_move3(self):
        return "Slash", self._slash_move_cost

    def get_move4(self):
        return "Execute", self._execute_move_cost
