from pygame import Surface

from .sprites.back import Back
from .sprites.background import Background
from objects.scene import Scene




class Info(Scene):
    
    name = 'info'
    
    def __init__(self, manager, surface:Surface) -> None:

        sprites = [
            Background,
            Back,
        ]

        super().__init__(
            manager=manager,
            sprites=sprites,
            surface=surface,
        )
