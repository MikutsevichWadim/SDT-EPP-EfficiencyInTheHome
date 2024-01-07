from objects.multiAngleSprite import MultiAngleSprite




class Shower(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl2/sprites/shower/on.png',
                    [861,301],
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/shower/off.png',
                    [861,301],
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
