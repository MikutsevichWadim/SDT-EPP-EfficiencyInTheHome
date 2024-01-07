from objects.multiAngleSprite import MultiAngleSprite




class Darkness(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'off': [
                    'assets/null.png',
                    [0,0],
                ],
                'on': [
                    'scenes/levels/lvl2/sprites/darkness/on.png',
                    [0,0],
                ],
            },
            'shelf': {
                'off': [
                    'assets/null.png',
                    [0,0],
                ],
                'on': [
                    'scenes/levels/lvl2/sprites/darkness/on.png',
                    [0,0],
                ],
            },
        }

        state = 'off'

        super().__init__(scene, angles, state)

    def on_click(self):
        # multi layer click
        return True
