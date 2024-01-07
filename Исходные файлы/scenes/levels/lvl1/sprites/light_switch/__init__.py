from objects.customSprite import CustomSprite




class LightSwitch(CustomSprite):

    def __init__(self,scene):

        self.pos = [550,463]

        states = {
            'on': [
                'scenes/levels/lvl1/sprites/light_switch/light_switch_on.png',
                self.pos,
                'sounds/light_switch/turn-on.wav'],
            'off': [
                'scenes/levels/lvl1/sprites/light_switch/light_switch_off.png',
                self.pos,
                'sounds/light_switch/turn-off.wav'],
        }

        state = 'on'
        
        super().__init__(
            scene=scene,
            states=states,
            state=state,
        )

    def on_click(self):
        self.switch_state()
        self.scene.sprites_refs['Lamp'].switch_state()
        self.scene.sprites_refs['WindowsLight'].switch_state()
