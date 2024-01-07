from objects.background import Background




class Background(Background):

    def __init__(self, scene):
        super().__init__(
            background_src='assets/mainBackground.png',
            scene=scene,
        )
