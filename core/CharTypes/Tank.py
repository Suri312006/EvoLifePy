from core.CharTypes.Skeleton.Base import Base


class Tank(Base):
    def __init__(self, health=150, ad=7, ap=15, mana=30, alive=True, armor=20, healAmount=15, stall=False):
        super().__init__(health, ad, ap, mana, alive)
        self._armor = armor
        self._healAmount = healAmount
        self._stall = stall

    def stall_move(self):
        self._stall = True

    def hit(self, other, damage):
        if not self._stall:
            super().get_hit(damage * (1 - self._armor))
        else:
            other.get_hit(self._armor * 0.5)
        stall = False

    def heal(self):
        super().add_health(self._healAmount)
