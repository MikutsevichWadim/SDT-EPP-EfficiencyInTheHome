from .sprites.angleSelectorShower import AngleSelectorShower
from .sprites.background import Level2BG
from .sprites.darkness import Darkness
from .sprites.door import Door
from .sprites.lamps import Lamps
from .sprites.lightSwitch import LightSwitch
from .sprites.shower import Shower
from .sprites.showerTap import ShowerTap
from .sprites.showerWater import ShowerWater
from .sprites.tap import Tap
from .sprites.toilet import Toilet
from objects.multiAngleLevel import MultiAngleLevel




class Level2(MultiAngleLevel):

    def __init__(
        self,
        manager:object,
        surface:object,
    ) -> None:

        angle = 'main'

        sprites = [
            Level2BG,

            Door,
            Lamps,
            LightSwitch,
            Shower,
            ShowerWater,
            ShowerTap,
            Tap,
            Toilet,

            AngleSelectorShower,
            Darkness,
        ]
        
        super().__init__(
            manager=manager,
            surface=surface,
            angle=angle,
            sprites=sprites,

            level_index=1,
        )
