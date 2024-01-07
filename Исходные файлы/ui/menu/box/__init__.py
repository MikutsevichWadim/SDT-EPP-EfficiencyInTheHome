from pygame.sprite import Group

from .background import Background
from .buttons.contin import Continue
from .buttons.exitMainMenu import ExitMainMenu
from objects.backgroundFogging import BackgroundFogging




class Box(Group):
    
    def __init__(self, manager):

        self.manager = manager

        sprites = [
            Background,

            # ordered by position
            Continue,
            ExitMainMenu,
        ]

        for i in range(len(sprites)):
            sprites[i] = sprites[i](self)

        sprites.insert(0, BackgroundFogging(manager.scene))

        super().__init__(sprites)

    def open(self):
        self.manager.scene.sprites.add(self)

    def close(self):
        self.manager.scene.sprites.remove(self)
