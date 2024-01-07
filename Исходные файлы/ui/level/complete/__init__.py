from pygame.sprite import Group

from .again import Again
from .background import Background
from .contin import Continue
from .lamps import Lamp1
from .lamps import Lamp2
from .lamps import Lamp3
from .next_level_hint import NextLevelHint
from data import Data
from objects.backgroundFogging import BackgroundFogging




class LevelComplete(Group):

    def __init__(self,scene) -> None:

        self.scene = scene

        self.lamps = Group(
            Lamp1(scene),
            Lamp2(scene),
            Lamp3(scene),
        )

        self.nextLevelHint = NextLevelHint(scene)

        super().__init__(
            BackgroundFogging(scene),
            Background(scene),
            Again(scene),
            Continue(scene),
            self.nextLevelHint,
            self.lamps,
        )

    def __call__(self) -> None:
        disabled_count = 0
        for consumer in self.scene.consumers:
            if not consumer.enabled:
                disabled_count += 1

        success = disabled_count / len(self.scene.consumers)

        Data.level_completed(Data, self.scene.level_index, success)

        self.nextLevelHint(success)
        for lamp in self.lamps:
            lamp(success)
        self.scene.sprites.add(self)

    def close(self):
        self.scene.sprites.remove(self)
