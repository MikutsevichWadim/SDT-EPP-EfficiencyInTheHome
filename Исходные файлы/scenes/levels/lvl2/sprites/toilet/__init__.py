from objects.multiAngleSprite import MultiAngleSprite




class Toilet(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl2/sprites/toilet/default.png',
                    [1350,680],
                ],
            },
        }

        state = 'default'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
