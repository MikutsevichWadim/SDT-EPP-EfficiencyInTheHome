from pygame.sprite import Group

from .background import Background
from .done import Done
from objects.backgroundFogging import BackgroundFogging




class Thanks(Group):

    def __init__(self, scene) -> None:

        self.scene = scene
        
        super().__init__(
            BackgroundFogging(scene),
            Background(scene),
            Done(scene, self),
        )

    def __call__(self):
        self.scene.sprites.add(self)

    def close(self):
        self.scene.sprites.remove(self)
