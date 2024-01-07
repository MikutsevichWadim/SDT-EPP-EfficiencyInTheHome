from pygame.sprite import Group

from .background import Background
from .done import Done
from data import Data
from objects.backgroundFogging import BackgroundFogging




class Rules(Group):

    def __init__(self, scene) -> None:

        self.scene = scene
        
        super().__init__(
            BackgroundFogging(scene),
            Background(scene),
            Done(scene, self),
        )

    def __call__(self):
        self.scene.sprites.add(self)
        Data.data['game']['show_rules'] = False

    def close(self):
        self.scene.sprites.remove(self)
