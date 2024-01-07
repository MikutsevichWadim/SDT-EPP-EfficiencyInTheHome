from objects.customSprite import CustomSprite




class TVPlug(CustomSprite):

    def __init__(self,scene):

        states = {
            'on': [
                'scenes/levels/lvl1/sprites/tv_plug/tv_plug_on.png',
                [20, 682],
                'sounds/plug/plug-in.wav',
            ],
            'off': [
                'scenes/levels/lvl1/sprites/tv_plug/tv_plug_off.png',
                [30, 746],
                'sounds/plug/plug-out.wav',
            ],
        }

        state = 'on'
        
        super().__init__(
            scene=scene,
            states=states,
            state=state,
        )

    def on_click(self):
        self.switch_state()
        self.scene.sprites_refs['TV'].switch_state()
