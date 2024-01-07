from objects.button import Button




class Again(Button):

    def __init__(self,scene) -> None:

        pos = [710, 625]

        states = {
            'default': 'ui/level/complete/again/default.png',
            'hovered': 'ui/level/complete/again/hovered.png',
        }

        super().__init__(
            scene=scene,
            pos=pos,
            states=states,
        )

    def __call__(self, passed):
        if passed:
            self.state = 'passed'
        else:
            self.state = 'notpassed'

    def on_click(self):
        super().on_click()
        self.scene.complete.close()
        self.scene.manager.scene = self.scene.__class__.__name__
