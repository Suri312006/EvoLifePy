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

from core.Player import Player
from core.elements.CharStatus import CharStatus


class game_screen:
    def __init__(self, display, display_width, display_height, ):
        self.display = display
        self.display_width = display_width
        self.display_height = display_height

        self.event = pygame.event.wait()
        self.clock = pygame.time.Clock()
        self.element = elements(self.display)

        self.Player1 = Player(self.display, image.suri(), MutantRaven)
        self.Player2 = Player(self.display, image.naila(), MutantRaven)

        self.Player1.set_enemy(self.Player2)
        self.Player2.set_enemy(self.Player1)

        self.Player1_moves = [self.Player1.button_move1(),
                              self.Player1.button_move2(),
                              self.Player1.button_move3(),
                              self.Player1.button_move4()]

        self.Player2_moves = [self.Player2.button_move1(),
                              self.Player2.button_move2(),
                              self.Player2.button_move3(),
                              self.Player2.button_move4()]

        self._block = self.display_height / 16

    def draw_env(self):
        self.display.fill(color.white())
        # self.element.character(self.Player1.get_char_img(), x_cord=10, y_cord=15)
        pygame.display.update()

    def game_loop(self):

        for i in range(len(self.Player1_moves)):
            self.Player1_moves[i].run(200,600+(i*100))

        for i in range(len(self.Player2_moves)):
            self.Player2_moves[i].run(1100,200+(i*100))

    def game_update(self):
        self.Player1.get_char_status().run(3 * self._block, 3 * self._block)
        self.Player2.get_char_status().run(16 * self._block, 9 * self._block)

    def run(self):
        self.game_loop()
        self.game_update()
