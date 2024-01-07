from objects.customSprite import CustomSprite




class Background(CustomSprite):

    def __init__(
        self,
        scene:object,
        background_src:str='assets/mainBackground.png',
    ):

        states = {
            'default': [background_src, [0,0]],
        }

        state = 'default'
        
        super().__init__(
            scene=scene,
            states=states,
            state=state,
        )
