from objects.button import Button




class Cancel(Button):

    def __init__(self, scene, pos):

        states = {
            'default': 'ui/common/buttons/cancel/default.png',
            'hovered': 'ui/common/buttons/cancel/hovered.png',
        }

        super().__init__(scene, pos, states)
