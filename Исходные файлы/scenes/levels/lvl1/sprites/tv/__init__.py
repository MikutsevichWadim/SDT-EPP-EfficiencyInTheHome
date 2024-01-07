from objects.nested.consumerSprite import ConsumerSprite




class TV(ConsumerSprite):

    def __init__(self,scene):

        self.pos = [-3,310]

        states = {
            'on': ['scenes/levels/lvl1/sprites/tv/tv-on.png', self.pos],
            'off': ['scenes/levels/lvl1/sprites/tv/tv-off.png', self.pos],
        }

        state = 'on'
        
        super().__init__(
            scene = scene,
            states = states,
            state = state,
        )
