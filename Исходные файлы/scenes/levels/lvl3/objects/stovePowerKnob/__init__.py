from objects.multiAngleSprite import MultiAngleSprite




class StovePowerKnob(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
        pos: list[int],
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl3/objects/stovePowerKnob/on.png',
                    pos,
                ],
                'off': [
                    'scenes/levels/lvl3/objects/stovePowerKnob/off.png',
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

    def on_click(self):
        self.switch_state()
