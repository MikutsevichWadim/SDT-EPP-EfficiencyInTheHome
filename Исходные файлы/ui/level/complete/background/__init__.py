from objects.background import Background




class Background(Background):

    def __init__(self, scene) -> None:

        background_src = 'ui/level/complete/background/box.png'

        super().__init__(
            scene=scene,
            background_src=background_src,
        )
