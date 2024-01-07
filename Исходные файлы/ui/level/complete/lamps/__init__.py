from config import SUCCESS_REQUIRED
from objects.customSprite import CustomSprite




class Lamp(CustomSprite):

    def __init__(self, scene, index):
        
        poses = (
            [727, 350],
            [891, 350],
            [1055, 350]
        )

        states = {
            'notsuccessed': [
                'ui/level/complete/lamps/off.png',
                poses[index],
            ],
            'successed': [
                'ui/level/complete/lamps/on.png',
                poses[index],
            ],
        }

        super().__init__(
            scene=scene,
            states=states,
        )

        self.success_required = SUCCESS_REQUIRED[index]

    def __call__(self, success):
        self.state = list(self.states.keys()) [int(success >= self.success_required)]

class Lamp1(Lamp):

    def __init__(self, scene):
        index = 0
        super().__init__(scene, index)

class Lamp2(Lamp):

    def __init__(self, scene):
        index = 1
        super().__init__(scene, index)

class Lamp3(Lamp):

    def __init__(self, scene):
        index = 2
        super().__init__(scene, index)

lamps_list = [
    Lamp1,
    Lamp2,
    Lamp3,
]
