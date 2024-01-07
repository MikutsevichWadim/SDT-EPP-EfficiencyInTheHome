from objects.nested.multiAngleConsumer import MultiAngleConsumer




class Lamps(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl3/sprites/lamps/on.png',
                    [513,0],
                ],
                'off': [
                    'scenes/levels/lvl3/sprites/lamps/off.png',
                    [513,0],
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
