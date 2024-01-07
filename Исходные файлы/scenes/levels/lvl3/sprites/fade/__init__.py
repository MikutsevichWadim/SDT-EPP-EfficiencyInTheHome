from objects.multiAngleSprite import MultiAngleSprite




class Fade(MultiAngleSprite):

    def __init__(self, scene):
        
        angles = {
            'shelf': {
                'default': [
                    'scenes/levels/lvl3/sprites/fade/fade.png',
                    [437.5, 584],
                ],
            },
        }

        state = 'default'

        super().__init__(
            scene=scene,
            angles=angles,
            state=state,
        )

    def on_click(self):
        return True