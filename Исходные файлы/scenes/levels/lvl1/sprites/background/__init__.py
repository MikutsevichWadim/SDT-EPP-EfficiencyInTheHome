from objects.background import Background




class Level1Bg(Background):

    def __init__(self,scene):

        super().__init__(
            background_src='scenes/levels/lvl1/sprites/background/background.png',
            scene=scene,
        )
        