from consts import WIDTH, HEIGHT, THEME
import pygame_menu

instructions_menu = pygame_menu.Menu("Instructions", WIDTH, HEIGHT, theme=THEME)   

instructions_menu.add.label("The goal is to eat as much food as possible")
instructions_menu.add.label("The green snake is controlled by the arrow keys")
instructions_menu.add.label("It needs to find red food items")
instructions_menu.add.label("The blue snake is controlled by the WASD keys")
instructions_menu.add.label("It needs to find the yellow food items")
instructions_menu.add.label("")
instructions_menu.add.label("Hitting another player or yourself restarts")
instructions_menu.add.label("Highscore values are to be found in the menu")
instructions_menu.add.label("Enable the border to add colliders to the edges")
instructions_menu.add.label("Enable speed inc to increase the difficulty")
instructions_menu.add.label("")
instructions_menu.add.label("Have fun playing!")
instructions_menu.add.label("")
instructions_menu.add.button("Back", pygame_menu.events.BACK)
instructions_menu.add.label("")