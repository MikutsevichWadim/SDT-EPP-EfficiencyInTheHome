from objects.background import Background




class Box(Background):

    def __init__(self, scene: object):

        background_src = 'ui/level/confirm/box/box.png'

        super().__init__(scene, background_src)
