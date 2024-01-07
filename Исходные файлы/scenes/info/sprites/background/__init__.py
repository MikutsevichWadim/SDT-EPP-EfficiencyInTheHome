from objects.customSprite import CustomSprite




class Background(CustomSprite):

    def __init__(self, scene):
        state = 'default'
        states = {
            'default': ['scenes/info/sprites/background/background.png', [0,0]]
        }
        super().__init__(scene, states, state)
