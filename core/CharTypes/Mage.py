from core.CharTypes.Skeleton.Damage import Damage


class Mage(Damage):
    def __init__(self, name="Mage", health=120, ad=20, ap=25, mana=40, alive=True):
        super().__init__(name, health, ad, ap, mana, alive)
        self._spell_surge_cost = 15;

    def basic_attack(self, other):
        other.get_hit((self._AD * 0.5 + self._AP * 0.5) * 1.5)

    def spell_surge(self, other):
        if self.mana_check(self._spell_surge_cost):
            other.get_hit(self._AP * 2)
        else:
            print("Cannot use Spell Surge, not enough mana")

    def final_spark(self, other):
        other.get_hit(self._AP * self._mana)
        self._mana = 0

    def move1(self, other):
        self.basic_attack(other)

    def move3(self, other):
        self.spell_surge(other)

    def move4(self, other):
        self.final_spark(other)

    def get_move1(self):
        return "Basic Attack", self._basic_attack_cost

    def get_move3(self):
        return "Spell Surge", self._spell_surge_cost

    def get_move4(self):
        return "Final Spark", self._mana
