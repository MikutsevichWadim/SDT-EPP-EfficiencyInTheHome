from objects.customSprite import CustomSprite




class Cabel(CustomSprite):

    def __init__(self,scene):

        states = {
            'plugged': [
                'scenes/levels/lvl1/sprites/cabel/cabel-on.png',
                [1354.63, 877.78],
            ],
            'unplugged': [
                'scenes/levels/lvl1/sprites/cabel/cabel-off.png',
                [1383.63, 877.78],
            ],
        }

        state = 'plugged'
        
        super().__init__(
            scene=scene,
            states=states,
            state=state,
        )
