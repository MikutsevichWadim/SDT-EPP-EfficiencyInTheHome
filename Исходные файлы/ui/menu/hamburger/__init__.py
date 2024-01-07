from objects.button import Button




class Hamburger(Button):

    def __init__(self, scene, box):

        pos = [1770,50]

        states = {
            'default': 'ui/menu/hamburger/default.png',
            'hovered': 'ui/menu/hamburger/hovered.png',
        }

        super().__init__(scene, pos, states)

        self.box = box

    def on_click(self):
        super().on_click()
        self.box.open()

    def switch_angle(self, *args):
        pass
