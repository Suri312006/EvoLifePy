from Base import Base


class Fighter(Base):

    def __init__(self, health=120, AD=20, AP=25, mana=40, alive=True, maxHpPercentage=0.15):
        super().__init__(health, AD, AP, mana, alive)
        self._maxHpPercentage = maxHpPercentage

        self._inverseADMult = 2
        self._seriousPunchCost = 25

    def bite(self, other):
        other.getHit(other.health * self._maxHpPercentage)

    def basicAttack(self, other):
        other.getHit(self.AD * (1 + self._inverseADMult * (1 / self._health)))

    def seriousPunch(self, other):
        if super().manaCheck(self._seriousPunchCost):
            other.getHit(other.health*self._inverseADMult*(1/self._health*0.1))
        else:
            print("Cannot use Serious Punch move, not enough mana")