from objects.button import Button




class Info(Button):
    
    def __init__(self, scene):

        pos = [1770, 930]

        states = {
            'default': 'scenes/main_menu/sprites/info/default.png',
            'hovered': 'scenes/main_menu/sprites/info/hovered.png',
        }

        super().__init__(scene, pos, states)

    def on_click(self):
        super().on_click()
        self.scene.manager.scene = 'Info'
