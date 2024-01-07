from objects.button import Button




class Done(Button):

    def __init__(self, scene, thanks):

        pos = [835, 835]

        states = {
            'default': 'ui/common/buttons/done/default.png',
            'hovered': 'ui/common/buttons/done/hovered.png',
        }

        super().__init__(scene, pos, states)

        self.thanks = thanks

    def on_click(self):
        super().on_click()
        self.thanks.close()
