from objects.background import Background




class Background(Background):

    def __init__(self, scene):

        background_src = 'ui/rules/background/rules.png'

        super().__init__(
            scene=scene,
            background_src=background_src,
        )
