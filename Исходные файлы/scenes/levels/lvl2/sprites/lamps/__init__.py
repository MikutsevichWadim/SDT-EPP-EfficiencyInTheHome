from objects.nested.multiAngleConsumer import MultiAngleConsumer




class Lamps(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl2/sprites/lamps/on.png',
                    [547,0],
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/lamps/off.png',
                    [547,0],
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
