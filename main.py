from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'HIDE'
import pygame_menu
import pygame
import sys
pygame.init()

WIDTH = 700
HEIGHT = WIDTH

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = BLACK

# ========= PyGame Initialization ==========
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def start_game():
    # Game Loop for GUI
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

        screen.fill(BG_COLOR)       

        pygame.display.update()

start_game()