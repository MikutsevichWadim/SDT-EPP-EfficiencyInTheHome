import pygame
pygame.display.init()
from pygame.locals import *




# DISPLAY
DISPLAY_CAPTION = 'Эффективность в доме'
pdinfo = pygame.display.Info()
DWIDTH, DHEIGHT = pdinfo.current_w, pdinfo.current_h
DISPLAY_SIZE = (DWIDTH, DHEIGHT)
DISPLAY_MODE = (DISPLAY_SIZE, RESIZABLE | FULLSCREEN)
PRINT_FPS = False

# LEVELS
LEVELS_COUNT = 3
LEVEL_SUCCES_TO_PASS = 1
SUCCESS_REQUIRED = [.25, .5, 1]

# RENDER
BACKGROUND = (255, 255, 255)
FPS = 60

# SCENES
SCENES_WITH_MENU = ['Map', 'Level1', 'Level2', 'Level3']
FIRST_SCENE='MainMenu'

# OTHER
BUTTON_SOUNDS_COUNT = 6
DATA_FILE = 'data'




__all__ = [
    'BACKGROUND',
    'DATA_FILE',
    'DISPLAY_CAPTION',
    'DISPLAY_MODE',
    'FPS',
    'LEVEL_SUCCES_TO_PASS',
    'LEVELS_COUNT',
    'SUCCESS_REQUIRED',
    'BUTTON_SOUNDS_COUNT',
    'SCENES_WITH_MENU',
    'FIRST_SCENE',
    'PRINT_FPS',
]