from objects.multiAngleSprite import MultiAngleSprite




class Doorway(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl3/sprites/doorway/default.png',
                    [375,328],
                ],
            },
        }

        state = 'default'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )

    def on_click(self) -> None:
        self.scene.confirm()