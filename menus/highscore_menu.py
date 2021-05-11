from consts import WIDTH, HEIGHT, THEME
import pygame_menu
import settings as s
import shelve

def reset_highscores():
    d = shelve.open("highscore.txt")
    d["highscore_single"] = s.highscore_single = 0
    d["highscore_multi_team"] = s.highscore_multi_team = 0
    d["highscore_multi_1"] = s.highscore_multi_1 = 0
    d["highscore_multi_2"] = s.highscore_multi_2 = 0
    d.close()

def save_highscores():
    d = shelve.open("highscore.txt")
    d["highscore_single"] = s.highscore_single 
    d["highscore_multi_team"] = s.highscore_multi_team
    d["highscore_multi_1"] = s.highscore_multi_1 
    d["highscore_multi_2"] = s.highscore_multi_2
    d.close()

# Remove Comment if you want to reset the highscore 
# file and save a new one for the upcoming game sessions:
# reset_highscores()

highscore_menu = pygame_menu.Menu("Highscores", WIDTH, HEIGHT, theme=THEME) 

def update_highscores():
    """ Updates the highscores labels at the end of every game """
    widgets = highscore_menu.get_widgets()
    widgets[0].set_title(f"Singleplayer: {s.highscore_single}")
    widgets[2].set_title(f"Multiplayer Team: {s.highscore_multi_team}")
    widgets[4].set_title(f"Multiplayer Competitive: {s.highscore_multi_1} vs. {s.highscore_multi_2}")

highscore_menu.add.label(title=f"Singleplayer: {s.highscore_single}")
highscore_menu.add.label("")
highscore_menu.add.label(title=f"Multiplayer Team: {s.highscore_multi_team}")
highscore_menu.add.label("")
highscore_menu.add.label(title=f"Multiplayer Competitive: {s.highscore_multi_1} vs. {s.highscore_multi_2}")
highscore_menu.add.label("")
highscore_menu.add.button('Back', pygame_menu.events.BACK)
highscore_menu.add.label("")