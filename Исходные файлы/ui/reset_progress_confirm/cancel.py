from ui.common.buttons.cancel import Cancel




class Cancel(Cancel):

    def __init__(self, scene, box):
        
        pos = [575, 575]

        super().__init__(scene, pos)

        self.box = box

    def on_click(self):
        super().on_click()
        self.box.close()