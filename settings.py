import shelve

global sound
sound = False

global teamplay
teamplay = True

global speed_inc
speed_inc = True

global border
border = False

d = shelve.open("highscore.txt")

global highscore_single
global highscore_multi_team
global highscore_multi_1
global highscore_multi_2

try:
    highscore_single = d["highscore_single"]
    highscore_multi_team = d["highscore_multi_team"]
    highscore_multi_1 = d["highscore_multi_1"]
    highscore_multi_2 = d["highscore_multi_2"]
except KeyError:
    highscore_single = 0
    highscore_multi_team = 0
    highscore_multi_1 = 0
    highscore_multi_2 = 0

d.close() 
