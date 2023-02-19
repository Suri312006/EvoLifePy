from core.CharTypes.Assasin import Assassin as ass
from core.CharTypes.Skeleton.Healthbar import Healthbar as hbar
class Player:

    def __init__(self, character=ass(name="default"), hp_x_cord=100, hp_y_cord=100):
        self._character = character
        self._hbar = hbar(character,x_cord=hp_x_cord, y_cord=hp_y_cord)

        ###multiple inheritance?