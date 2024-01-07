from .sprites.background import Background
from .sprites.contin import Continue
from .sprites.exit import Exit
from .sprites.info import Info
from .sprites.start import Start
from objects.scene import Scene




class MainMenu(Scene):

    def __init__(self, manager: object, surface: object) -> None:

        sprites = [
            Background,
            
            Continue,
            Exit,
            Info,
            Start,
        ]

        super().__init__(manager, surface, sprites)
