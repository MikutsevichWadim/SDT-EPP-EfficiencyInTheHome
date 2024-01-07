from ui.common.buttons.contin import Continue




class Continue(Continue):

    def __init__(self, scene) -> None:

        pos = [710, 750]

        super().__init__(
            scene=scene,
            pos=pos
        )

    def on_click(self):
        super().on_click()
        self.scene.complete.close()
        self.scene.manager.scene = 'Map'
