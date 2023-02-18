from CharTypes.Damage import Damage

class Mage(Damage):
    def __init__(self, health=120, ad=20, ap=25, mana=40, alive=True):
        super().__init__(health, ad, ap, mana, alive)
        self._spell_surge_cose = 15;

    def basic_attack(self, other):
        other.get_hit((self._AD * 0.5 + super.getAD * 0.5) * 1.5)

    def spellSurge(self, other):
        if self.mana_check(self._spell_surge_cose):
            other.get_hit(self._AP * 2)
        else:
            print("Cannot use Spell Surge, not enough mana")
