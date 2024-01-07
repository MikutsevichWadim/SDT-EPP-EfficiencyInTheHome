from data import Data
from ui.common.buttons.contin import Continue




class Continue(Continue):

    def __init__(self, scene):

        pos = [710, 340]

        super().__init__(scene, pos)

    def on_click(self):
        super().on_click()
        if self.state != 'unavailable':
            self.scene.manager.scene = 'Map'

    def scene_enter(self):
        super().scene_enter()
        self.state = ['unavailable', 'default'][int(Data.data['game']['started'])]
