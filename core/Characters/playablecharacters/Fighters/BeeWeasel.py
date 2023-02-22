from core.Characters.CharArchetypes.Fighter import Fighter
from core.util import References as img


class BeeWeasel(Fighter):

    def __init__(self, name="Bee Weasel", health=120, ad=20, ap=25, mana=40, alive=True, max_hp_percentage=0.15):
        super().__init__(name, health, ad, ap, mana, alive, max_hp_percentage)
        self._img = img.bee_weasel()

    def get_img(self):
        return self._img


