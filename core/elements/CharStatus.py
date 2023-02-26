from core.elements.Bars import Healthbar, Manabar
from core.util import Colors as color
from core.elements.Elements import Elements

import pygame


class CharStatus:
    def __init__(self, display, char, width=400, height=300):
        # values here
        self.display = display
        self.char = char
        self.char_healthbar = Healthbar(self.char)
        self.char_manabar = Manabar(self.char)

        self.width = width
        self.height = height

        self.unit = width/16

        self.element = Elements(self.display)
        pass

    def draw_hp_bar(self, x_cord, y_cord):
        length = self.char_healthbar.get_max_length()
        height = self.char_healthbar.bar_height

        hp_bar_le = self.char_healthbar.get_current_length()
        hp_color = self.char_healthbar.get_color()
        offset = self.char_healthbar.offset

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

    def draw_mana_bar(self, x_cord, y_cord):
        length = self.char_manabar.get_max_length()
        height = self.char_manabar.bar_height

        mana_bar_le = self.char_manabar.get_current_length()
        mana_color = self.char_manabar.get_color()
        offset = self.char_manabar.offset

        pygame.draw.rect(self.display, color=color.gray(),
                         rect=(x_cord, y_cord, length, height), border_radius=15)
        # fill-in rect
        pygame.draw.rect(self.display, color=color.white(),
                         rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset),
                         border_radius=14)
        # actual changing rect

        if mana_bar_le > 0:
            pygame.draw.rect(self.display, color=mana_color,
                             rect=(x_cord + offset / 2, y_cord + offset / 2, mana_bar_le - offset, height - offset),
                             border_radius=15)

    def draw_base(self,x_cord,y_cord):
        pygame.draw.rect(self.display, color=color.off_white(),
                         rect=(x_cord, y_cord, self.width, self.height), border_radius=15)

    def run(self, x_cord=0, y_cord=0):
        self.draw_base(x_cord,y_cord)
        self.draw_hp_bar(x_cord+self.unit, y_cord+self.unit)
        self.draw_mana_bar(x_cord + (self.unit), y_cord + (self.unit*4))

        # background rect
        pygame.display.update()
        pass
