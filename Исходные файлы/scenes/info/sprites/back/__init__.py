from objects.button import Button




class Back(Button):

    def __init__(self, scene):

        pos = [835,950]

        states = {
            'default': 'scenes/info/sprites/back/default.png',
            'hovered': 'scenes/info/sprites/back/hovered.png',
        }

        super().__init__(scene, pos, states)

    def on_click(self):
        super().on_click()
        self.scene.manager.scene = 'MainMenu'