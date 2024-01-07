from objects.button import Button




class Cancel(Button):

    def __init__(self, scene, box):

        pos = [575, 575]

        states = {
            'default': 'ui/level/exitMainMenu/cancel/default.png',
            'hovered': 'ui/level/exitMainMenu/cancel/hovered.png',
        }

        super().__init__(scene, pos, states)

        self.box = box

    def on_click(self):
        super().on_click()
        self.box.close()
