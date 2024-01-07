from objects.button import Button




class ExitMainMenu(Button):

    def __init__(self, box):

        pos = [710, 550]

        states = {
            'default': 'ui/menu/box/buttons/exitMainMenu/default.png',
            'hovered': 'ui/menu/box/buttons/exitMainMenu/hovered.png',
        }

        super().__init__(box.manager.scene, pos, states)

        self.box = box
        self.manager = box.manager

    def on_click(self):
        super().on_click()
        self.box.close()
        self.scene.manager.scene = 'MainMenu'
