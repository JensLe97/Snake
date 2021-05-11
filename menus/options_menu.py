from consts import WIDTH, HEIGHT, THEME, ENGINE
import settings as s
import pygame
import pygame_menu

music_on = False

def set_sound(with_sound):
    from menus.main_menu import menu
    if s.sound:
        menu.set_sound(None, recursive=True)
    else:
        menu.set_sound(ENGINE, recursive=True)
    s.sound = not s.sound

def set_music(with_music):
    global music_on
    if music_on:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    music_on = not music_on
    
options_menu = pygame_menu.Menu("Options", WIDTH, HEIGHT, theme=THEME)

options_menu.add.toggle_switch('Sound Effects  ', False, onchange=set_sound)
options_menu.add.toggle_switch('Music  ', False, onchange=set_music)
options_menu.add.label("")
options_menu.add.button('Back', pygame_menu.events.BACK)