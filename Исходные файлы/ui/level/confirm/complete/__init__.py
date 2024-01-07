from objects.button import Button




class Complete(Button):

    def __init__(self, scene):

        pos = 990, 575

        states = {
            'default': 'ui/level/confirm/complete/default.png',
            'hovered': 'ui/level/confirm/complete/hovered.png',
        }

        super().__init__(scene, pos, states)

    def on_click(self):
        super().on_click()
        self.scene.confirm.close()
        self.scene.complete()
