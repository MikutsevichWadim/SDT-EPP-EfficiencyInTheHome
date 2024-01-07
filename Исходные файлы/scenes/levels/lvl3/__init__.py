from .sprites.angleSelectorShelf import AngleSelectorShelf
from .sprites.bg import Level3BG
from .sprites.darkness import Darkness
from .sprites.doorway import Doorway
from .sprites.extensionPlug import ExtensionPlug
from .sprites.fade import Fade
from .sprites.indicator import Indicator
from .sprites.lamps import Lamps
from .sprites.lightSwitch import LightSwitch
from .sprites.kettlePlug import KettlePlug
from .sprites.microwavePlug import MicrowavePlug
from .sprites.oven import Oven
from .sprites.powerKnob import PowerKnob
from .sprites.stovePowerKnobs import StovePowerKnob1
from .sprites.stovePowerKnobs import StovePowerKnob2
from .sprites.stovePowerKnobs import StovePowerKnob3
from .sprites.stovePowerKnobs import StovePowerKnob4
from .sprites.stovePowerKnobs import StovePowerKnobOven
from .sprites.stoves import Stove1
from .sprites.stoves import Stove2
from .sprites.stoves import Stove3
from .sprites.stoves import Stove4
from .sprites.table import Table
from .sprites.timerKnob import TimerKnob
from objects.multiAngleLevel import MultiAngleLevel




class Level3(MultiAngleLevel):

    def __init__(
        self,
        manager:object,
        surface:object
    ) -> None:

        angle = 'main'

        sprites = [
            Level3BG,

            AngleSelectorShelf,
            Doorway,
            ExtensionPlug,
            Indicator,
            KettlePlug,
            Lamps,
            LightSwitch,
            MicrowavePlug,
            
            Fade,
            Oven,
            PowerKnob,
            Stove1,
            Stove2,
            Stove3,
            Stove4,
            StovePowerKnob1,
            StovePowerKnob2,
            StovePowerKnob3,
            StovePowerKnob4,
            StovePowerKnobOven,
            Table,
            TimerKnob,

            Darkness,
        ]
        
        super().__init__(
            manager=manager,
            surface=surface,
            angle=angle,
            sprites=sprites,

            level_index=2,
        )
