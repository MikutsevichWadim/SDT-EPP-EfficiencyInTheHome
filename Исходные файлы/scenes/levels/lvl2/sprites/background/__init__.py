from objects.multiAngleSprite import MultiAngleSprite




class Level2BG(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:
        
        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl2/sprites/background/background.png',
                    [0,0],
                ],
            },
            'shower': {
                'default': [
                    'scenes/levels/lvl2/sprites/background/shower.png',
                    [0,0],
                ],
            },
        }

        state = 'default'
        
        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
