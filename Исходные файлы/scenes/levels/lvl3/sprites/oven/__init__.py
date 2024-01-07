from objects.nested.multiAngleConsumer import MultiAngleConsumer




class Oven(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl3/sprites/oven/on.png',
                    [1257,716],
                ],
                'off': [
                    'scenes/levels/lvl3/sprites/oven/off.png',
                    [1257,716],
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
