from ui.common.buttons.contin import Continue




class Continue(Continue):

    def __init__(self, box):

        scene = box.manager.scene

        pos = [710, 400]

        super().__init__(scene, pos)

        self.box = box

    def on_click(self):
        super().on_click()
        self.box.close()
