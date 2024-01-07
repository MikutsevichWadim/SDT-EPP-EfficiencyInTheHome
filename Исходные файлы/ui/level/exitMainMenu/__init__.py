from pygame.sprite import Group

from .box import Box
from .cancel import Cancel
from .exit import Exit
from objects.backgroundFogging import BackgroundFogging




class ExitMainMenu(Group):

    def __init__(self, scene) -> None:

        self.scene = scene
        
        super().__init__(
            BackgroundFogging(scene),
            Box(scene),
            Cancel(scene, self),
            Exit(scene),
        )

    def __call__(self):
        self.scene.sprites.add(self)

    def close(self):
        self.scene.sprites.remove(self)
