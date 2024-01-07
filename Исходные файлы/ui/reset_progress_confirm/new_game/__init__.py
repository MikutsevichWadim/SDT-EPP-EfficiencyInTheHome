from objects.button import Button




class NewGame(Button):

    def __init__(self, scene, box):

        pos = [990, 575]

        states = {
            'default': 'ui/reset_progress_confirm/new_game/default.png',
            'hovered': 'ui/reset_progress_confirm/new_game/hovered.png',
        }

        super().__init__(scene, pos, states)

        self.box = box

    def on_click(self):
        super().on_click()
        self.scene.manager.game.new_game()
        self.scene.manager.scene = 'Map'
        self.box.close()
