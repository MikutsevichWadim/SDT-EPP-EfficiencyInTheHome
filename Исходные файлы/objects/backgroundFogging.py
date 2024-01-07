import pygame

from .customSprite import CustomSprite




class BackgroundFogging(CustomSprite):
    
    def __init__(self,scene):

        states = {
            'default': ['assets/backgroundFogging.png', [0,0]],
        }

        state = 'default'

        super().__init__(
            scene=scene,
            states=states,
            state=state,
        )

    def on_hover(self):
        return True
    
    def on_unhover(self):
        pass
