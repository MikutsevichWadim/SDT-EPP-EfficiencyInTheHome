from objects.button import Button
from data import Data
from ui.reset_progress_confirm import ResetProgressConfirm




class Start(Button):
    
    def __init__(self, scene):

        pos = [710, 490]

        states = {
            'default': 'scenes/main_menu/sprites/start/default.png',
            'hovered': 'scenes/main_menu/sprites/start/hovered.png',
        }

        super().__init__(scene, pos, states)

        self.rpc = ResetProgressConfirm(self.scene)

    def on_click(self):
        super().on_click()
        if Data.data['game']['started']:
            self.rpc()
        else:
            self.scene.manager.game.new_game()
            self.scene.manager.scene = 'Map'
