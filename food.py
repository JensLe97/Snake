import pygame
import random
from consts import *

class Food:
    def __init__(self, color, border):
        self.random_pos()
        self.color = color
        self.border = border

    def draw(self, screen):
        square = pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.color, square)
        pygame.draw.rect(screen, self.border, square, width=1)

    def random_pos(self, snake_pos=[]):
        """ Try to generate a valid spawning position, Return True if the game is "won",
            i.e. no more free cells left, else returns false. """
        if len(snake_pos) >= NUM_CELLS:
            return True
            
        while True:
            pos = (random.randint(0, GRID_COLUMNS - 1) * CELL_SIZE, random.randint(0, GRID_ROWS - 1) * CELL_SIZE)
            if pos not in snake_pos:
                self.position = pos
                return False
        