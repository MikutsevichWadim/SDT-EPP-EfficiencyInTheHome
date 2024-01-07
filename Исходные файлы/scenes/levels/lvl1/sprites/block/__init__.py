from objects.nested.consumerSprite import ConsumerSprite




class Block(ConsumerSprite):

    def __init__(self,scene):

        states = {
            'plugged': [
                'scenes/levels/lvl1/sprites/block/block-on.png',
                [1343.63,999.28],
                'sounds/plug/plug-in.wav',
            ],
            'unplugged': [
                'scenes/levels/lvl1/sprites/block/block-off.png',
                [1481.63,859.04],
                'sounds/plug/plug-out.wav',
            ],
        }

        state = 'plugged'
        
        super().__init__(
            scene = scene,
            states = states,
            state = state,
        )

    def on_click(self):
        self.switch_state()
        self.scene.sprites_refs['Cabel'].switch_state()
