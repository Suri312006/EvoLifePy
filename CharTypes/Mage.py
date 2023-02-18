from CharTypes.Damage import Damage

class Mage(Damage):
    def __init__(self, health=120, AD=20, AP=25, mana=40, alive=True):
        super().__init__(health, AD, AP, mana, alive)
        self._spell_surge_cose = 15;

    def basicAttack(self, other):
        other.getHit((self._AD*0.5 + super.getAD*0.5)*1.5)

    def spellSurge(self, other):
        if self.manaCheck(self._spell_surge_cose):
            other.getHit(self._AP*2)
        else:
            print("Cannot use Spell Surge, not enough mana")
