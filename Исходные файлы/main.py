'''
Проект по учебной практике по предмету
"Технология разработки программного обеспечения"

Игровое приложение
"Эффективность в доме"
на тему "Энергоэффективность"

Разработал: Микуцевич Вадим
'''

import pygame
from pygame.locals import *
from pygame.time import Clock
pygame.init()
pygame.display.init()
pygame.mixer.init()
pygame.transform.set_smoothscale_backend('GENERIC')

from config import *
from data import Data
from objects.events import Events
from objects.scenes import Scenes
from scenes.info import Info
from scenes.main_menu import MainMenu
from scenes.map import Map
from scenes.levels.lvl1 import Level1
from scenes.levels.lvl2 import Level2
from scenes.levels.lvl3 import Level3




class Game:

    def __init__(self):

        self.clock = Clock()
        
        pygame.mixer.Sound('music/continue.wav').play(loops=-1)

        # scenes
        surface = pygame.display.set_mode(*DISPLAY_MODE)
        pygame.display.set_icon(pygame.image.load('assets/icon.png'))
        pygame.display.set_caption(DISPLAY_CAPTION)
        scenes = (
            MainMenu,
            Info,
            
            Map,
            
            Level3,
            Level2,
            Level1,
        )

        self.scenes = Scenes(
            game=self,
            scenes=scenes,
            surface=surface,
        )
        
        self.events = Events(self)

        self.surface = surface

        self.open_rules = True

    def run(self):
        
        self.events()
        self.events.draw()

        while True:
            if self.events(): # handling
                break
            self.clock.tick(FPS)

        pygame.quit()

    def new_game(self):

        Data.reset_progress(Data)
        Data.data['game']['started'] = True

    def quit(self):
        Data.save(Data)
        pygame.quit()

if __name__ == '__main__':
    Game().run()
