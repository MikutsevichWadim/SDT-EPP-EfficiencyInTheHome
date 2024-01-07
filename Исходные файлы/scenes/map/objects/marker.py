from objects.button import Button
from data import Data




class Marker(Button):

    def __init__(self, scene, pos, states, level_i, scene_name):
        
        self.level_i = level_i
        self.scene_name = scene_name
        self.available = Data.available[self.level_i]
        
        super().__init__(
            scene=scene,
            pos=pos,
            states=states,
            available=self.available,
        )
        
    def on_click(self):
        super().on_click()
        if self.state == 'default' or self.state == 'hovered':
            self.scene.manager.scene = self.scene_name

    def scene_enter(self):
        self.state = ['unavailable', 'default'][Data.available[self.level_i]]
