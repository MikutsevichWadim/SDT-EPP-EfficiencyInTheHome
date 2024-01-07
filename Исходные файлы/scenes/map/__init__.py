from pygame import Surface

from .sprites.background import Background
from .sprites.rooms import Rooms
from .sprites.markers.badRoom import MarkerBadRoom
from .sprites.markers.kitchen import MarkerKitchen
from .sprites.markers.restRoom import MarkerRestRoom
from data import Data
from objects.scene import Scene
from ui.rules import Rules
from ui.thanks import Thanks




class Map(Scene):

    name = 'map'
    
    def __init__(self, manager, surface:Surface) -> None:

        sprites = [
            Background,
            Rooms,
            
            MarkerBadRoom,
            MarkerKitchen,
            MarkerRestRoom,
        ]

        super().__init__(
            manager=manager,
            sprites=sprites,
            surface=surface,
        )

        self.rules = Rules(self)

    def enter(self):
        super().enter()
        if self.manager.previous_scene_name == 'MainMenu':
            self.rules()

        if Data.data['game']['show_thanks']:
            Data.data['game']['show_thanks'] = False
            Thanks(self)()
        
