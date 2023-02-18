from CharTypes.Base import Base


class Fighter(Base):

    def __init__(self, health=120, ad=20, ap=25, mana=40, alive=True, maxHpPercentage=0.15):
        super().__init__(health, ad, ap, mana, alive)
        self._maxHpPercentage = maxHpPercentage

        self._inverseADMult = 2
        self._seriousPunchCost = 25

    def bite(self, other):

        other.get_hit(other.get_health() * self._maxHpPercentage)

    def basic_attack(self, other):
        other.get_hit(self._AD * (1 + self._inverseADMult * (1 / self._health)))

    def seriousPunch(self, other):
        if super().mana_check(self._seriousPunchCost):
            other.get_hit(other.get_health() * self._inverseADMult * (1 / self._health * 0.1))
        else:
            print("Cannot use Serious Punch move, not enough mana")