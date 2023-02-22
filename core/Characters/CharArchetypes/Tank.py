from core.Characters.Skeleton.Base import Base


class Tank(Base):
    def __init__(self, health=150, ad=7, ap=15, mana=30, alive=True, armor=20, heal_amount=15, stall=False):
        super().__init__(health, ad, ap, mana, alive)
        self._armor = armor
        self._healAmount = heal_amount
        self._stall = stall

    def stall_move(self):
        self._stall = True

    def hit(self, other, damage):
        if not self._stall:
            self.get_hit(damage * (1 - self._armor))
        else:
            other.get_hit(self._armor * 0.5)
        self._stall = False

    def heal(self):
        self.add_health(self._healAmount)
