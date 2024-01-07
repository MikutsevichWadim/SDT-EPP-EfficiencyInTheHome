import pygame
from pygame.event import Event

from objects.button import Button




class Exit(Button):
    
    def __init__(self, scene):

        pos = [710, 640]

        states = {
            'default': 'scenes/main_menu/sprites/exit/default.png',
            'hovered': 'scenes/main_menu/sprites/exit/hovered.png',
        }

        super().__init__(scene, pos, states)

    def on_click(self):
        super().on_click()
        pygame.event.post(Event(pygame.QUIT))
