from objects.multiAngleSprite import MultiAngleSprite




class Table(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl3/sprites/table/default.png',
                    [586,705],
                ],
            },
        }

        state = 'default'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
