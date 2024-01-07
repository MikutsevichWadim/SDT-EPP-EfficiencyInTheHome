from objects.consumer import Consumer
from objects.multiAngleSprite import MultiAngleSprite




class MultiAngleConsumer(Consumer, MultiAngleSprite):
    '''
    Объединяет логику классов Consumer и MultiAngleSprite
    '''

    def __init__(
        self,
        scene: object,
        angles: dict,
        state: str,
    ) -> None:
        
        Consumer.__init__(
            self = self,
            scene = scene,
        )

        MultiAngleSprite.__init__(
            self = self,
            scene = scene,
            angles = angles,
            state = state,
        )
        
    def switch_state(self) -> None:
        MultiAngleSprite.switch_state(self)
        Consumer.switch_state(self)

    def scene_enter(self) -> None:
        MultiAngleSprite.scene_enter(self)
        Consumer.scene_enter(self)
