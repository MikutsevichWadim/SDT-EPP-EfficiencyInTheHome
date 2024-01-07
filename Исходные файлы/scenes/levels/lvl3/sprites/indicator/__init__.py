from objects.consumer import Consumer
from objects.multiAngleSprite import MultiAngleSprite




class Indicator(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl3/sprites/indicator/main-on.png',
                    [701,506],
                ],
                'off': [
                    'scenes/levels/lvl3/sprites/indicator/main-off.png',
                    [701,506],
                ],
            },
            'shelf': {
                'on': [
                    'scenes/levels/lvl3/sprites/indicator/shelf-on.png',
                    [1033,465],
                ],
                'off': [
                    'scenes/levels/lvl3/sprites/indicator/shelf-off.png',
                    [1033,465],
                ],
            },
        }

        state = 'on'

        MultiAngleSprite.__init__(
            self = self,
            scene = scene,
            angles = angles,
            state = state,
        )

        Consumer.__init__(
            self = self,
            scene = scene,
        )
        
    def switch_state(self) -> None:
        MultiAngleSprite.switch_state(self)
        Consumer.switch_state(self)

    def scene_enter(self) -> None:
        MultiAngleSprite.scene_enter(self)
        Consumer.scene_enter(self)
