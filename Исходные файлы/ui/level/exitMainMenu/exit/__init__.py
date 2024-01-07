from objects.button import Button




class Exit(Button):

    def __init__(self, scene):

        pos = [990, 575]

        states = {
            'default': 'ui/level/exitMainMenu/exit/default.png',
            'hovered': 'ui/level/exitMainMenu/exit/hovered.png',
        }

        super().__init__(scene, pos, states)

    def on_click(self):
        super().on_click()
        self.scene.exit()
        self.scene.manager.scene = 'MainMenu'
