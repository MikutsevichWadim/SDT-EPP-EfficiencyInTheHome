import pygame
from pygame.event import Event

from .events import DRAW_EVENT
from .customGroup import CustomGroup




class Scene:
    '''
    Используется для хранения набора спрайтов,
    передачи событий входа и выхода со сцены спрайтам.
    '''

    def __init__(
        self,
        manager: object,
        surface: object,
        sprites: list[object]=[],
    ) -> None:
        
        self.is_init = True
        
        self.manager = manager
        self.surface = surface

        # определение соотношения сторон
        self.dsize = (1920, 1080) # default size
        self.ratio = self.dsize[0] / self.dsize[1]
        self.pos = [0,0]
        # self.sprites = []
        self.update_pos_size()

        # добавление возможности обращения
        # к спрайтам по названию их классов
        self.sprites_refs = dict()
        for i, Sprite in enumerate(sprites):
            sprite = Sprite(scene=self)
            sprites[i] = sprite
            self.sprites_refs[sprite.__class__.__name__] = sprite

        self.sprites = CustomGroup(sprites)

        self.is_init = False
        
        self.update_pos_size()

    def enter(self):
        '''
        Вызывается классом Scenes при входе на текущую сцену.
        '''
        for sprite in self.sprites:
            sprite.scene_enter()

    def leave(self):
        '''
        Вызывается классом Scenes при выходе из текущей сцены.
        '''
        for sprite in self.sprites:
            sprite.scene_leave()

    def update_pos_size(self):
        '''
        1) Вычисляет аттрибут size_hint: int,
        используемый спрайтами сцены для изменения своего размера.

        2) Вызывает метод update_pos_size() у группы спрайтов сцены.
        '''

        ssize = self.surface.get_size()
        sratio = ssize[0] / ssize[1]
        self.size = [0,0]
        self.pos = [0,0]

        if sratio >= self.ratio:
            self.size[1] = ssize[1]
            self.size[0] = round(self.size[1] * self.ratio)
            self.pos[0] = ssize[0] // 2 - self.size[0] // 2

        elif sratio < self.ratio:
            self.size[0] = ssize[0]
            self.size[1] = round(self.size[0] / self.ratio)
            self.pos[1] = ssize[1] // 2 - self.size[1] // 2
            
        self.size_hint = self.size[0] / self.dsize[0]

        # sprites update
        if not self.is_init:
            self.sprites.update_pos_size()

        pygame.event.post(Event(DRAW_EVENT))

    def set_menu(self, menu):
        menu(self, self.sprites)
