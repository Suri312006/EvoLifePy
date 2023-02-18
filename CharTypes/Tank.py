from Base import Base


class Tank(Base):
    def __init__(self, health=150, AD=7, AP=15, mana=30, alive=True, armor=20, healAmount=15, stall=False):
        super().__init__(health, AD, AP, mana, alive)
        self._armor = armor
        self._healAmount = healAmount
        self._stall = stall

    def stallMove(self):
        self._stall = True;

    def hit(self, other, damage):
        if not self._stall:
            super().getHit(damage*(1-self._armor))
        else:
            other.getHit(self._armor*0.5)
        stall = False

    def heal(self):
        super().addHealth(self._healAmount)