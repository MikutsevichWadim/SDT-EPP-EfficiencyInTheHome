from objects.multiAngleSprite import MultiAngleSprite




class ShowerTap(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'shower': {
                'on': [
                    'scenes/levels/lvl2/sprites/showerTap/on.png',
                    [1170,519],
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/showerTap/off.png',
                    [1170,519],
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
        self.scene.sprites_refs['Shower'].switch_state()
        self.scene.sprites_refs['ShowerWater'].switch_state()
