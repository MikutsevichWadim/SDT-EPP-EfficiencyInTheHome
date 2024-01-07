from objects.nested.multiAngleConsumer import MultiAngleConsumer




class Knob(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
        poses: list[int],
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl3/objects/knob/main-on.png',
                    poses[0],
                ],
                'off': [
                    'scenes/levels/lvl3/objects/knob/main-off.png',
                    poses[0],
                ],
            },
            'shelf': {
                'on': [
                    'scenes/levels/lvl3/objects/knob/shelf-on.png',
                    poses[1],
                ],
                'off': [
                    'scenes/levels/lvl3/objects/knob/shelf-off.png',
                    poses[1],
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )

    def on_click(self) -> None:
        self.switch_state()
