import pygame

import core.util.Colors as color
from core.elements.Elements import Elements as elements


class Button:
    def __init__(self, display=None, text="default", font='arial', text_size=10, text_color=color.black(),
                 width=75, height=15,
                 inactive_color=color.light_red(), active_color=color.red(),
                 action=None, action_target=None):

        self.display = display
        self.text = text
        self.font = font
        self.text_size = text_size
        self.text_color = text_color
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action
        self.action_target = action_target

        self.clicked = False

        self.mouse = None
        self.click = None
        self.update_mouse()
        self.element = elements(self.display)

    def update_mouse(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def run(self, x_cord, y_cord):
        self.update_mouse()

        if x_cord + self.width > self.mouse[0] > x_cord and \
                y_cord + self.height > self.mouse[1] > y_cord:
            pygame.draw.rect(self.display, self.active_color,
                             (x_cord, y_cord, self.width, self.height))

            if not self.clicked:
                if self.click[0] == 1 and self.action is not None and self.action_target is not None:
                    self.action(self.action_target)
                if self.click[0] == 1 and self.action is not None and self.action_target is None:
                    self.action()
                self.clicked = True

            if self.click[0] == 0:
                self.clicked = False

        else:
            pygame.draw.rect(self.display, self.inactive_color,
                             (x_cord, y_cord, self.width, self.height))

        self.element.render_text(self.text, x_cord + self.width / 2, y_cord + self.height / 2, self.font,
                                 self.text_size,
                                 self.text_color)
