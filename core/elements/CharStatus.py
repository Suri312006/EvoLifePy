from core.elements.Bars import Healthbar, Manabar
from core.util import Colors as color
import pygame


class CharStatus:
    def __init__(self, display, player):
        # values here
        self.display = display
        self.player = player
        self.char_healthbar = Healthbar(player)
        self.char_manabar = Manabar(player)
        pass

    def run(self, x_cord, y_cord):
        length = self.char_healthbar.get_max_length()
        height = self.char_healthbar.bar_height

        hp_bar_le = self.char_healthbar.get_current_length()
        hp_color = self.char_healthbar.get_color()
        offset = self.char_healthbar.offset

        pygame.draw.rect(self.display, color=color.off_white(),
                         rect=(x_cord, y_cord, length * 1, height * 3))

        pygame.draw.rect(self.display, color=color.gray(),
                         rect=(x_cord, y_cord, length, height), border_radius=15)
        # fill-in rect
        pygame.draw.rect(self.display, color=color.white(),
                         rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset),
                         border_radius=14)
        # actual changing rect

        if hp_bar_le > 0:
            pygame.draw.rect(self.display, color=hp_color,
                             rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset),
                             border_radius=15)

        # background rect
        pygame.display.update()
        pass
