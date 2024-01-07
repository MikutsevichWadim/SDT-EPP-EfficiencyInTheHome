from config import SUCCESS_REQUIRED
from objects.customSprite import CustomSprite




class NextLevelHint(CustomSprite):

    def __init__(self, scene):

        states = {
            'notsuccessed': [
                'ui/level/complete/next_level_hint/notsuccessed.png',
                [710, 850],
            ],
            'successed': [
                'assets/null.png',
                [710, 850],
            ],
        }

        super().__init__(
            scene=scene,
            states=states,
        )

        self.success_required = SUCCESS_REQUIRED[2]

    def __call__(self, success):
        if success == self.success_required:
            self.state = 'successed'
        else:
            self.state = 'notsuccessed'
