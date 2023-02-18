class Base:

    def __init__(self, health=100, AD=15, AP=20, mana=40, alive=True):
        self._health = health
        self._AD = AD
        self._AP = AP
        self._mana = mana
        self._alive = alive

    def addHealth(self, additionalHealth):
        self._health += additionalHealth

    def getHit(self, damage):
        self._health -= damage

    def hit(self, other, damage):
        other.getHit(damage)

    def manaCheck(self, moveCost):
        if self._mana > moveCost:
            self._mana -= moveCost
            return True
        return False

    def die(self):
        self._alive = False

    def basicAttack(self, other):
        self.hit(other, self._AD)

    def gethealth(self):
        return round(self._health,2)
