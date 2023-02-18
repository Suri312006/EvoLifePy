from CharTypes.Base import Base


class Damage(Base):
    def __init__(self, health=120, ad=20, ap=25, mana=40, alive=True):
        super().__init__(health, ad, ap, mana, alive)
        self._barrageCost = 15

    def barrage(self, other):
        if self.mana_check(self._barrageCost):
            other.get_hit(self._AD + self._AP)
        else:
            print("Cannot use Barrage move, not enough mana")
