from collections.abc import Iterable

import pygame
from pygame.event import Event
from pygame.sprite import Group

from .events import DRAW_EVENT



class CustomGroup:

    def __init__(self, *sprites):

        self._group = Group(*sprites)

        self.hoverable_sprites = []
        self.clickable_sprites = []
        
        self.add_interactive(*sprites)

    def __call__(self, *args, **kwargs) -> None:
        map(
            lambda sprite: sprite(*args, **kwargs),
            self._group.sprites()
        )

    def __iter__(self):
        return iter(self._group.sprites())

    def add_interactive(self, *sprites):

        for sprite in sprites:
            if isinstance(sprite, Iterable):
                self.add_interactive(*sprite)
            else:
                if sprite.hoverable:
                    self.hoverable_sprites.insert(0, sprite)
                if sprite.clickable:
                    self.clickable_sprites.insert(0, sprite)

    def remove_interactive(self, *sprites):

        for sprite in sprites:
            if isinstance(sprite, Iterable):
                self.remove_interactive(*sprite)
            else:
                if sprite in self.hoverable_sprites:
                    self.hoverable_sprites.remove(sprite)
                if sprite in self.clickable_sprites:
                    self.clickable_sprites.remove(sprite)

    def update_pos_size(self) -> None:
        for sprite in self.sprites():
            sprite.update_pos_size()

    def add(self, *sprites) -> None:
        self._group.add(*sprites)
        self.add_interactive(*sprites)
        self.update_pos_size()
        pygame.event.post(Event(DRAW_EVENT))

    def draw(self, *args, **kwargs):
        self._group.draw(*args, **kwargs)

    def remove(self, *sprites) -> None:
        self._group.remove(*sprites)
        self.remove_interactive(*sprites)
        pygame.event.post(Event(DRAW_EVENT))

    def sprites(self):
        return self._group.sprites()
        