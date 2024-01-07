from objects.nested.multiAngleConsumer import MultiAngleConsumer




class Stove(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
        pos: list[int],
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl3/objects/stove/on.png',
                    pos,
                ],
                'off': [
                    'scenes/levels/lvl3/objects/stove/off.png',
                    pos,
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )
