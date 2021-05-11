import random
import pygame
from consts import *
import settings as s

class Snake:
    def __init__(self, color, border):
        self.reset()
        self.color = color
        self.border = border

    def move(self, other_snake):
        """ Constantly move the snake in the self.direction and check if it is hitting itself
            Returns whether the move has lead to a collision"""
        current_pos = self.positions[0]
        # Do not calculate the modulo when there is a border
        next_pos = ((current_pos[0] + self.direction[0] * CELL_SIZE), (current_pos[1] + self.direction[1] * CELL_SIZE)) if s.border else \
                   ((current_pos[0] + self.direction[0] * CELL_SIZE) % WIDTH, (current_pos[1] + self.direction[1] * CELL_SIZE) % HEIGHT)
        
        # Check if a hit occurs: snake hits other snake or it hits itself
        if (other_snake and next_pos in other_snake.positions 
            or len(self.positions) > 3 and next_pos in self.positions[3:]
            or s.border and (next_pos[0] > WIDTH - CELL_SIZE or next_pos[0] < 0 or next_pos[1] > HEIGHT - CELL_SIZE or next_pos[1] < 0)):
            if other_snake and s.teamplay:
                other_snake.reset()
            self.reset()
            return True
        # No hit: update the snake's positions
        else:
            self.positions.insert(0, next_pos)
            if len(self.positions) > self.length:
                self.positions.pop()
            return False

    def turn(self, direction):
        """ Change the direction if snake is bigger than 1 and direction is valid"""
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction

    def reset(self):
        self.length = 1
        # Set a random spawn position in the middle of the window
        self.positions = [( random.choice([x for x in range(WIDTH // SPAWN_AREA, WIDTH // SPAWN_AREA * (SPAWN_AREA - 1), CELL_SIZE)]), 
                            random.choice([y for y in range(HEIGHT // SPAWN_AREA, HEIGHT // SPAWN_AREA * (SPAWN_AREA - 1), CELL_SIZE)]))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, screen):
        for pos in self.positions:
            square = pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, self.color, square)
            pygame.draw.rect(screen, self.border, square, width=1)




