from objects.background import Background




class Background(Background):

    def __init__(self, box):

        background_src = 'ui/menu/box/background/box.png'

        super().__init__(box.manager.scene, background_src)
