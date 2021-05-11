from consts import WIDTH, HEIGHT, THEME
import pygame
import pygame_menu

screen = pygame.display.set_mode((WIDTH, HEIGHT))

from menus.singleplayer_menu import singleplayer_menu
from menus.multiplayer_menu import multiplayer_menu
from menus.options_menu import options_menu
from menus.credits_menu import credits_menu
from menus.highscore_menu import highscore_menu
from menus.instructions import instructions_menu

menu = pygame_menu.Menu("Snake", WIDTH, HEIGHT, theme=THEME)

# Setup background music
pygame.mixer.music.load("sounds/almost_bliss.mp3")
# Play from beginning and repeat
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.pause()

bg_image = pygame_menu.BaseImage(image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER)

def main_background():
    bg_image.draw(screen)

def menu_fun():
    menu.enable()
    menu.add.button("One Player", singleplayer_menu)
    menu.add.button("Two Players", multiplayer_menu)
    menu.add.button("Highscores", highscore_menu)
    menu.add.button("Instructions", instructions_menu)
    menu.add.button("Options", options_menu)
    menu.add.button("Credits", credits_menu)
    menu.add.label("")
    menu.add.button("Quit", pygame_menu.events.EXIT)

    if menu.is_enabled():
        menu.mainloop(screen, main_background)