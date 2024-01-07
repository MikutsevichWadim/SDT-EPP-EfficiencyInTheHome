from objects.nested.multiAngleConsumer import MultiAngleConsumer




class ExtensionPlug(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'shelf': {
                'on': [
                    'scenes/levels/lvl3/sprites/extensionPlug/on.png',
                    [835,676],
                    'sounds/plug/plug-in.wav',
                ],
                'off': [
                    'scenes/levels/lvl3/sprites/extensionPlug/off.png',
                    [713,804.45],
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
