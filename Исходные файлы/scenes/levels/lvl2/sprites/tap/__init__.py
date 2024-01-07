from pygame.mixer import Sound

from objects.nested.multiAngleConsumer import MultiAngleConsumer




class Tap(MultiAngleConsumer):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'on': [
                    'scenes/levels/lvl2/sprites/tap/on.png',
                    [457,636],
                ],
                'off': [
                    'scenes/levels/lvl2/sprites/tap/off.png',
                    [457,636],
                ],
            },
        }

        state = 'on'

        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )

        self.sound = Sound('sounds/tap.wav')
        self.sound_enabled = False

        print(self.dstate)

    def scene_enter(self):
        super().scene_enter()
        self.sound.play(loops=-1)
        self.sound_enabled = True

    def scene_leave(self):
        super().scene_leave()
        self.sound.stop()
        self.sound_enabled = False

    def on_click(self) -> None:
        self.switch_state()

    def switch_state(self) -> None:
        super().switch_state()

        if self.sound_enabled:
            self.sound.stop()
        else:
            self.sound.play(loops=-1)
        self.sound_enabled = not self.sound_enabled
