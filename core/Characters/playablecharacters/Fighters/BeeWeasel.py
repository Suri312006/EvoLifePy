from core.Characters.CharArchetypes.Fighter import Fighter
from core.util import References as img
class BeeWeasel(Fighter):

    def __init__(self, name="Bee Weasel", health=120, ad=20, ap=25, mana=40, alive=True, maxHpPercentage=0.15):
        super.__init__(name, health, ad, ap, mana, alive, maxHpPercentage)
        self._img = img.bee_weasel()

    def get_img(self):
        return self._img

    def move1(self, other):
        self.basic_attack(other)

    def move2(self, other):
        self.bite(other)

    def move3(self, other):
        self.serious_punch(other)

    def move4(self, other):
        self.execute(other)

    def get_move1(self):
        return "Basic Attack", self._basic_attack_cost

    def get_move2(self):
        return "Barrage", self._barrageCost

    def get_move3(self):
        return "Slash", self._slash_move_cost

    def get_move4(self):
        return "Execute", self._execute_move_cost