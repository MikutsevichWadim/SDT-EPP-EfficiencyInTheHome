from scenes.levels.lvl3.objects.knob import Knob




class PowerKnob(Knob):

    def __init__(self, scene:object):

        poses = [
            [691, 450],
            [1009, 227],
        ]
        
        super().__init__(
            scene=scene,
            poses=poses
        )

    