from objects.button import Button




class Done(Button):
    
    def __init__(self, scene, pos):

        states = {
            'default': 'ui/common/buttons/done/default.png',
            'hovered': 'ui/common/buttons/done/hovered.png',
        }

        super().__init__(scene, pos, states)
