from objects.multiAngleSprite import MultiAngleSprite




class LightSwitch(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl2/sprites/lightSwitch/on.png',
                    [330,458],
                    'sounds/light_switch/turn-on.wav',
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/lightSwitch/off.png',
                    [330,458],
                    'sounds/light_switch/turn-off.wav',
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
        self.scene.sprites_refs['Darkness'].switch_state()
        self.scene.sprites_refs['Lamps'].switch_state()
