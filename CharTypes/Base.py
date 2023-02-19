class Base:

    def __init__(self, health=100, ad=15, ap=20, mana=40, alive=True):
        self._health = health
        self._AD = ad
        self._AP = ap
        self._mana = mana
        self._alive = alive

    def add_health(self, additional_health):
        self._health += additional_health

    def get_hit(self, damage):
        self._health -= damage

    def hit(self, other, damage):
        other.get_hit(damage)

    def mana_check(self, move_cost):
        if self._mana > move_cost:
            self._mana -= move_cost
            return True
        return False

    def die(self):
        self._alive = False

    def basic_attack(self, other):
        self.hit(other, self._AD)

    def get_health(self):
        return round(self._health,2)
