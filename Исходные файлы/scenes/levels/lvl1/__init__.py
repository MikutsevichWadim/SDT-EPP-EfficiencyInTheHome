from pygame import Surface

from .sprites.block import Block
from .sprites.background import Level1Bg
from .sprites.cabel import Cabel
from .sprites.door import Door
from .sprites.light_switch import LightSwitch
from .sprites.lamp import Lamp
from .sprites.tv import TV
from .sprites.tv_plug import TVPlug
from .sprites.windowsLight import WindowsLight
from objects.level import Level




class Level1(Level):

    def __init__(self, manager, surface:Surface):

        sprites = [
            Level1Bg,

            Block,
            Cabel,
            Door,
            LightSwitch,
            Lamp,
            TV,
            TVPlug,
            WindowsLight,
        ]

        super().__init__(
            manager=manager,
            sprites=sprites,
            surface=surface,
            level_index=0
        )
