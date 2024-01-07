from pygame.mixer import Sound

from objects.nested.multiAngleConsumer import MultiAngleConsumer




class ShowerWater(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'shower': {
                'on': [
                    'scenes/levels/lvl2/sprites/showerWater/on.png',
                    [1017,183],
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/showerWater/off.png',
                    [1017,183],
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )

        self.sound = Sound('sounds/shower.wav')
        self.sound_enabled = False

    def scene_enter(self):
        super().scene_enter()
        self.sound_enabled = True
        self.sound.play(loops=-1)

    def scene_leave(self):
        super().scene_leave()
        self.sound_enabled = False
        self.sound.stop()

    def switch_state(self) -> None:
        super().switch_state()

        if self.sound_enabled:
            self.sound.stop()
        else:
            self.sound.play()
        self.sound_enabled = not self.sound_enabled
