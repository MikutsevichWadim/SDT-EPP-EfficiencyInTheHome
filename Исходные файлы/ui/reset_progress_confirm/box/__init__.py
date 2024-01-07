from objects.background import Background




class Box(Background):

    def __init__(self, scene):

        background_src = 'ui/reset_progress_confirm/box/box.png'

        super().__init__(
            scene=scene,
            background_src=background_src,
        )
