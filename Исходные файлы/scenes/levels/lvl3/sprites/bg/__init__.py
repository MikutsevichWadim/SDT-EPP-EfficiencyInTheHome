from objects.multiAngleSprite import MultiAngleSprite




class Level3BG(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:
        
        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl3/sprites/bg/background-mainAngle.png',
                    [0,0],
                ],
            },
            'shelf': {
                'default': [
                    'scenes/levels/lvl3/sprites/bg/background-shelfAngle.png',
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
