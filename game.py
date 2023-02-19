import time
import pygame
from pygame.locals import *

WIDTH = 1000
HEIGHT = 800

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode([WIDTH, HEIGHT])
event = pygame.event.wait()
clock = pygame.time.Clock()

def du():
    pygame.display.update()
def init():
    pygame.init()
    pygame.display.set_caption("A bit Racey")
    clock.tick(60)

def draw_env():
    game_display.fill(WHITE)
    du()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_env()
        clock.tick(60)

if __name__ == '__main__':
    init()
    main()

##healthbar ???
