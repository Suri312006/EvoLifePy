from CharTypes.Base import Base


class Damage(Base):
    def __init__(self, health=120, AD=20, AP=25, mana=40, alive=True):
        super().__init__(health, AD, AP, mana, alive)
        self._barrageCost = 15

    def barrage(self, other):
        if self.manaCheck(self._barrageCost):
            other.getHit(self._AD+self._AP)
        else:
            print("Cannot use Barrage move, not enough mana")
