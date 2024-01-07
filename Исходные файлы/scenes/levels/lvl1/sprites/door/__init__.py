from objects.button import Button




class Door(Button):

    def __init__(self,scene):

        states = {
            'default': 'scenes/levels/lvl1/sprites/door/door.png',
        }

        pos = [649, 337.5]
        
        super().__init__(
            scene=scene,
            pos=pos,
            states=states,
        )

    def on_click(self):
        super().on_click()
        self.scene.confirm()

    def on_hover(self):
        pass

    def on_unhover(self):
        pass
