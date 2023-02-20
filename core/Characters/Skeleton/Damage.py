from core.Characters.Skeleton.Base import Base


class Damage(Base):
    def __init__(self, name="damage", health=120, ad=20, ap=25, mana=40, alive=True):
        super().__init__(name, health, ad, ap, mana, alive)
        self._barrageCost = 15

    def barrage(self, other):
        if self.mana_check(self._barrageCost):
            other.get_hit(self._AD + self._AP)
        else:
            print("Cannot use Barrage move, not enough mana")

    def move2(self, other):
        self.barrage(other)

    def get_move2(self):
        return "Barrage", self._barrageCost
