
import pygame

from core.Characters.playablecharacters.Assassins.MutantRaven import MutantRaven
from core.Characters.playablecharacters.Assassins.MutantSpider import MutantSpider

from core.Characters.playablecharacters.Fighters.BeeWeasel import BeeWeasel
from core.Characters.playablecharacters.Fighters.SharkDoggy import SharkDoggy

from core.Characters.playablecharacters.Mages.MushRoon import MushRoon
from core.Characters.playablecharacters.Mages.AngryPlant import AngryPlant
from core.Characters.playablecharacters.Mages.ForestSpirit import ForestSpirit

from core.Characters.playablecharacters.Tanks.RolyPoly import RolyPoly
from core.Characters.playablecharacters.Tanks.TortiCat import TortiCat

from core.elements.Button import Button as Button
from core.elements.Elements import Elements as elements
from core.util import Colors as color
import core.util.References as image


class game_screen:
    def __init__(self, display):
        self.display = display


        event = pygame.event.wait()
        clock = pygame.time.Clock()
        element = elements(game_display)

        Player1 = Player(image.suri(), MutantRaven)
        Player2 = Player(image.naila(), MutantRaven)

        Player1.set_enemy(Player2)
        Player2.set_enemy(Player1)

        Player1_moves = [Player1.get_button1(),
                         Player1.get_button2(),
                         Player1.get_button3(),
                         Player1.get_button4()]

        Player2_moves = [Player2.get_button1(),
                         Player2.get_button2(),
                         Player2.get_button3(),

    def draw_env(self):
        self.display.fill(color.white())
        self.display.character(Player1.get_char_img(), x_cord=10, y_cord=15)
        pygame.display.update()
