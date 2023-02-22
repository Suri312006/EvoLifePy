from core.elements.CharStatus import Healthbar as char_status


class Base:
#Creates base character
    def __init__(self, name='nothing', health=100, ad=15, ap=20, mana=40, alive=True, hp_x_cord=20, hp_y_cord=20):
        self._name = name
        self._max_health = health
        self._health = health
        self._AD = ad
        self._AP = ap
        self._mana = mana
        self._alive = alive
        self._char_status = char_status(self)
        self._basic_attack_cost = 1

    def add_health(self, additional_health):
        self._health += additional_health

    def get_hit(self, damage):
        if self._health - damage >=0:
            self._health -= damage
        else:
            self._health=0

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
        return round(self._health, 2)
    def get_mana(self):
        return round(self._mana, 2)

    def get_max_health(self):
        return round(self._max_health, 2)

    def get_name(self):
        return self._name

    def health_report(self):
        return [self.get_health(),
                100 * round(self.get_health() / self.get_max_health(), 4)]

    def get_char_status(self):
        return self._char_status

