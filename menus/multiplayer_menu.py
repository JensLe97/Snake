from consts import WIDTH, HEIGHT, THEME
import settings as s
import pygame_menu

def set_border(with_border, new=False):
    s.border = new if new else with_border

def set_speed_inc(with_speed_inc, new=False): 
    s.speed_inc = new if new else with_speed_inc

def set_teamplay(with_teamplay, new=False): 
    s.teamplay = new if new else with_teamplay

def update_widgets(w_1, w_2, w_3):
    """ Updates the settings (global variables) of the toggle switches.
    When changing from single to multiplayer, widgets that are not changed again,
    are not updated automatically and the old value from the other menu is used. 
    Therefore, this method updates these states again.
    w_1:    toggle switch border
    w_2:    toggle switch speed_inc
    w_3:    toggle switch teamplay"""
    w_1.change(w_1.get_value())
    w_2.change(w_2.get_value())
    w_3.change(w_3.get_value())
    # Start Game with multiplayer = True
    from main import start_game
    start_game(True)

multiplayer_menu = pygame_menu.Menu("Two Players", WIDTH, HEIGHT, theme=THEME)

w_1 = multiplayer_menu.add.toggle_switch("With Border:  ", False, onchange=set_border)

w_2 = multiplayer_menu.add.toggle_switch("Increase Speed:  ", True, onchange=set_speed_inc)

w_3 = multiplayer_menu.add.toggle_switch("Teamplay:  ", True, onchange=set_teamplay)
multiplayer_menu.add.button("Play", update_widgets, w_1, w_2, w_3)
multiplayer_menu.add.label("")
multiplayer_menu.add.button('Back', pygame_menu.events.BACK)