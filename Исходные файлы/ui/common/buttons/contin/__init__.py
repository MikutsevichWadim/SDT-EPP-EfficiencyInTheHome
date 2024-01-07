from objects.button import Button




class Continue(Button):
    '''
    Кнопка с предопределёнными изображениями.
    '''

    def __init__(self, scene, pos):

        states = {
            'default': 'ui/common/buttons/contin/default.png',
            'hovered': 'ui/common/buttons/contin/hovered.png',
            'unavailable': 'ui/common/buttons/contin/unavailable.png',
        }

        super().__init__(scene, pos, states)
