from CharTypes.Assasin import Assassin as ass
from CharTypes.Mage import Mage as mag
from CharTypes.Fighter import Fighter as fig
from CharTypes.Tank import Tank as tan
from core.Healthbar import Healthbar as hbar
class Player:

    def __init__(self, character=ass(name="default"), ):
        self._character = character
        self._