from core.Characters.Skeleton.Base import Base


class Fighter(Base):

    def __init__(self, name="fighter", health=120, ad=20, ap=25, mana=40, alive=True, max_hp_percentage=0.15):
        super().__init__(name, health, ad, ap, mana, alive)
        self._maxHpPercentage = max_hp_percentage

        self._inverseADMult = 2
        self._seriousPunchCost = 25

    def bite(self, other):

        other.get_hit(other.get_health() * self._maxHpPercentage)

    def basic_attack(self, other):
        other.get_hit(self._AD * (1 + self._inverseADMult * (1 / self._health)))

    def serious_punch(self, other):
        if super().mana_check(self._seriousPunchCost):
            other.get_hit(other.get_health() * self._inverseADMult * (1 / self._health * 0.1))
        else:
            print("Cannot use Serious Punch move, not enough mana")
