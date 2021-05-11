import pygame_menu
import pygame

# Window
WIDTH = 800
HEIGHT = 600

# Timing
FPS = 60
DEFAULT_DELAY = 150
DELAY_INC = 5
MIN_DELAY = 50

# Grid
CELL_SIZE = WIDTH // 40
GRID_ROWS = HEIGHT // CELL_SIZE
GRID_COLUMNS = WIDTH // CELL_SIZE
NUM_CELLS = GRID_ROWS * GRID_COLUMNS

# Propotion of spawnable area
# 5 means that snakes spawn beween 
# 1/5 and 4/5 of the screen width and height
SPAWN_AREA = 5

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (64, 64, 64)
GREEN = (0, 150, 35)
BLUE = (0, 110, 255)
DARK_BLUE = (0, 47, 110)
DARK_GREEN = (0, 92, 23)
RED = (210, 55, 0)
DARK_RED = (92, 11, 0)
YELLOW = (216, 227, 0)
DARK_YELLOW = (170, 176, 0)

BG_COLOR = BLACK
GRID_COLOR = GREY

SNAKE_1_COLOR = GREEN
SNAKE_1_BORDER_COLOR = DARK_GREEN
SNAKE_2_COLOR = BLUE
SNAKE_2_BORDER_COLOR = DARK_BLUE

FOOD_1_COLOR = RED
FOOD_1_BORDER_COLOR = DARK_RED
FOOD_2_COLOR = YELLOW
FOOD_2_BORDER_COLOR = DARK_YELLOW

# Texts
SCORE_WIDTH = 100
SCORE_WIDTH_MULTI = 250
SCORE_DIST = 150
SCORE_POS = (WIDTH // 2 - SCORE_WIDTH // 2, 10)
SCORE_POS_MULTI = (WIDTH // 2 - SCORE_WIDTH_MULTI // 2, 10)

PAUSE_WIDTH = 70
PAUSE_POS = (WIDTH // 2 - PAUSE_WIDTH // 2, HEIGHT // 2)

WINNER_WIDTH = 50

# Menu Theme
MENU_FONT = pygame_menu.font.FONT_OPEN_SANS
THEME = pygame_menu.themes.THEME_DARK.copy()
THEME.set_background_color_opacity(0)
THEME.title_background_color=(255, 255, 255, 50)
THEME.widget_font=MENU_FONT
THEME.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
THEME.widget_font_color=(255, 255, 255)
THEME.selection_color=(255, 255, 255)

# Sounds
EAT = pygame.mixer.Sound("sounds/eat.ogg")

ENGINE = pygame_menu.sound.Sound()
ENGINE.load_example_sounds()
ENGINE.set_sound(pygame_menu.sound.SOUND_TYPE_CLICK_MOUSE, None)
ENGINE.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, 'sounds/click.ogg', volume=1)
ENGINE.set_sound(pygame_menu.sound.SOUND_TYPE_KEY_ADDITION, 'sounds/eat.ogg', volume=1)