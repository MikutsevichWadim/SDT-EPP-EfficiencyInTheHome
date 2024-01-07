from objects.nested.multiAngleConsumer import MultiAngleConsumer




class KettlePlug(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl3/sprites/kettlePlug/on.png',
                    [967,577],
                    'sounds/plug/plug-in.wav',
                ],
                'off': [
                    'scenes/levels/lvl3/sprites/kettlePlug/off.png',
                    [930,610],
                    'sounds/plug/plug-out.wav',
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
    