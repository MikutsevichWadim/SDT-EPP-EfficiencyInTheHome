from scenes.levels.lvl3.objects.knob import Knob




class TimerKnob(Knob):

    def __init__(self, scene:object):

        poses = [
            [691, 481],
            [1009, 360],
        ]
        
        super().__init__(
            scene=scene,
            poses=poses
        )
    