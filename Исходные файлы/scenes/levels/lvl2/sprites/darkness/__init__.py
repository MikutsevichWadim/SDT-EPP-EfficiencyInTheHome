from objects.multiAngleSprite import MultiAngleSprite




class Darkness(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl2/sprites/darkness/on.png',
                    [0,0],
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/darkness/off.png',
                    [0,0],
                ],
            },
            'shower': {
                'on': [
                    'scenes/levels/lvl2/sprites/darkness/on.png',
                    [0,0],
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/darkness/off.png',
                    [0,0],
                ],
            },
        }

        state = 'off'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )

    def on_click(self):
        return True
