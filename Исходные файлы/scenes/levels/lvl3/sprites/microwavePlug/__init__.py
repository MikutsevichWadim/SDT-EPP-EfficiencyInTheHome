from objects.nested.multiAngleConsumer import MultiAngleConsumer




class MicrowavePlug(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'shelf': {
                'on': [
                    'scenes/levels/lvl3/sprites/microwavePlug/on.png',
                    [565,582],
                    'sounds/plug/plug-in.wav',
                ],
                'off': [
                    'scenes/levels/lvl3/sprites/microwavePlug/off.png',
                    [550,583],
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
        self.scene.sprites_refs['Indicator'].switch_state()
