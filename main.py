from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'HIDE'

import os
import sys

path = os.path.abspath(os.path.join('..'))
if path not in sys.path:
    sys.path.append(path)

import pygame_menu   
import pygame
pygame.init()

from consts import *
import settings as s
from snake import Snake
from food import Food

from menus.main_menu import menu_fun
from menus.highscore_menu import save_highscores, update_highscores

# ========= PyGame Initialization ==========
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

font = pygame.font.SysFont("candara", 30)

def draw_text(text, pos, color):
    text = font.render(text, True, color)
    screen.blit(text, pos)

def draw_grid(screen):
    for i in range(1, GRID_ROWS):
        for j in range(1, GRID_COLUMNS):
            pygame.draw.line(screen, GRID_COLOR, (j * CELL_SIZE, 0), (j * CELL_SIZE, HEIGHT))
            pygame.draw.line(screen, GRID_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))

def check_controls(snake, event, wasd):
    if wasd:
        if event.key == pygame.K_w:
            snake.turn(UP)
        elif event.key == pygame.K_s:
            snake.turn(DOWN)
        elif event.key == pygame.K_a:
            snake.turn(LEFT)
        elif event.key == pygame.K_d:
            snake.turn(RIGHT)
    else:
        if event.key == pygame.K_UP:
            snake.turn(UP)
        elif event.key == pygame.K_DOWN:
            snake.turn(DOWN)
        elif event.key == pygame.K_LEFT:
            snake.turn(LEFT)
        elif event.key == pygame.K_RIGHT:
            snake.turn(RIGHT)  

def start_game(multiplayer):
    # Disable the main menu loop
    from menus.main_menu import menu
    menu.disable()
    menu.full_reset()

    paused = False

    snake_1 = Snake(GREEN, DARK_GREEN)
    food_1 = Food(RED, DARK_RED)

    if multiplayer:
        snake_2 = Snake(BLUE, DARK_BLUE)
        food_2 = Food(YELLOW, DARK_YELLOW)

    # Controls the speed of the game
    SCREEN_UPDATE = pygame.USEREVENT
    delay = DEFAULT_DELAY
    pygame.time.set_timer(SCREEN_UPDATE, delay)

    # Game Loop for GUI
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_highscores()
                    update_highscores()
                    menu.enable()
                    return
                if event.key == pygame.K_p:
                    paused = not paused

                check_controls(snake_1, event, False)
                if multiplayer:
                    check_controls(snake_2, event, True)                 

            if event.type == SCREEN_UPDATE and not paused:
                collision_1 = collision_2 = False
                if multiplayer:
                    collision_1 = snake_1.move(snake_2)
                    collision_2 = snake_2.move(snake_1)
                else:
                    collision_1 = snake_1.move(None)
                # Reset the delay after any collision
                if collision_1 or collision_2:
                    delay = DEFAULT_DELAY
                    pygame.time.set_timer(SCREEN_UPDATE, delay)

        screen.fill(BG_COLOR)   
        draw_grid(screen)  

        food_1.draw(screen)
        if multiplayer:
            food_2.draw(screen)
        
        snake_1.draw(screen)
        if multiplayer:  
            snake_2.draw(screen)

        if paused:
            draw_text("Pause", PAUSE_POS, WHITE)

        won = False
        if snake_1.positions[0] == food_1.position:
            if s.sound:
                pygame.mixer.Sound.play(EAT)
            snake_1.length += 1
            snake_2_pos = snake_2.positions if multiplayer else []
            won = food_1.random_pos(snake_1.positions + snake_2_pos)
            if s.speed_inc and delay - DELAY_INC >= MIN_DELAY:
                delay -= DELAY_INC
            pygame.time.set_timer(SCREEN_UPDATE, delay)

        if multiplayer and snake_2.positions[0] == food_2.position:
            if s.sound:
                pygame.mixer.Sound.play(EAT)
            snake_2.length += 1
            won = food_2.random_pos(snake_1.positions + snake_2.positions)
            if s.speed_inc and delay - DELAY_INC >= MIN_DELAY:
                delay -= DELAY_INC
            pygame.time.set_timer(SCREEN_UPDATE, delay)
        
        if won:
            draw_text("YOU WON!", (WIDTH // 2 - WINNER_WIDTH, HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            start_game()

        # Multiplayer and teamplay
        if multiplayer and s.teamplay:
            score = snake_1.length + snake_2.length - 2
            draw_text(f"Score: {score}", SCORE_POS, WHITE)
            if score > s.highscore_multi_team:
                s.highscore_multi_team = score
        # Multiplayer without teamplay
        elif multiplayer:
            score_1 = snake_1.length - 1
            score_2 = snake_2.length - 1
            draw_text(f"Score: {score_1}", SCORE_POS_MULTI, GREEN)
            draw_text(f"Score: {score_2}", (SCORE_POS_MULTI[0] + SCORE_DIST, SCORE_POS_MULTI[1]), BLUE)
            if score_1 > s.highscore_multi_1:
                s.highscore_multi_1 = score_1
            elif score_2 > s.highscore_multi_2:
                s.highscore_multi_2 = score_2
        # Singleplayer
        else:
            score = snake_1.length - 1
            draw_text(f"Score: {score}", SCORE_POS, GREEN)
            if score > s.highscore_single:
                s.highscore_single = score
        pygame.display.update()

if __name__ == '__main__':
    menu_fun()