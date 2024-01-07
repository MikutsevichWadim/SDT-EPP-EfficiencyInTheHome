from objects.nested.consumerSprite import ConsumerSprite




class Lamp(ConsumerSprite):

    def __init__(self, scene) -> None:

        self.pos = [683,31]

        states = {
            'on': ['scenes/levels/lvl1/sprites/lamp/lamp-on.png', self.pos],
            'off': ['scenes/levels/lvl1/sprites/lamp/lamp-off.png', self.pos],
        }

        state = 'on'

        super().__init__(
            scene = scene,
            states = states,
            state = state,
        )
