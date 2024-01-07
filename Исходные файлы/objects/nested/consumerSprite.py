from objects.consumer import Consumer
from objects.customSprite import CustomSprite




class ConsumerSprite(Consumer, CustomSprite):
    '''
    Объединяет логику классов Consumer и CustomSprite
    '''

    def __init__(
        self,
        scene: object,
        states: dict,
        state: str = None,
    ):
        
        Consumer.__init__(
            self = self,
            scene = scene,
        )

        CustomSprite.__init__(
            self = self,
            scene = scene,
            states = states,
            state = state,
        )

    def scene_enter(self):
        Consumer.scene_enter(self)
        CustomSprite.scene_enter(self)

    def switch_state(self) -> None:
        Consumer.switch_state(self)
        CustomSprite.switch_state(self)
    