import random

from pygame.mixer import Sound

from .customSprite import CustomSprite
from config import BUTTON_SOUNDS_COUNT




class Button(CustomSprite):

    # здесь states должно иметь
    # только название
    # и путь к изображению
    def __init__(self, scene, pos, states: dict, available: bool = True):

        for state_name, image_src in states.items():
            states[state_name] = [image_src, pos]
        state = ['unavailable', 'default'][available]
        super().__init__(scene, states, state)

        self.sounds = list()
        for sound_i in range(BUTTON_SOUNDS_COUNT):
            self.sounds.append(Sound(f'sounds/button/button_click_{sound_i}.wav'))

    def on_click(self):
        print(self.__class__.__name__, 'pressed')
        if self.state != 'unavailable':
            random.choice(self.sounds).play()

    def on_hover(self):
        if self.state != 'unavailable' and self.state != 'hovered':
            self.switch_state('hovered')
        
    def on_unhover(self):
        if self.state != 'unavailable' and self.state != 'default':
            self.switch_state('default')
