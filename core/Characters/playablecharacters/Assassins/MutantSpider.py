from core.Characters.CharArchetypes.Assassin import Assassin
from core.util import References as img
class MutantSpider(Assassin):
    def __init__(self, name="Mutant Spider", health=120, ad=20, ap=25, mana=40, alive=True):
        super().__init__(name, health, ad, ap, mana, alive)