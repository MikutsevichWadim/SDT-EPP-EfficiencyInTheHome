from pygame.mixer import Channel

from objects.button import Button




class Music(Button):

    def __init__(self, scene, pos):

        states = {
            'enabled': 'ui/music/enabled.png',
            'disabled': 'ui/music/enabled.png',
        }

        super().__init__(scene, pos, states)

    def on_click(self):
        super().on_click()
        self.switch_state()
        if self.state == 'enabled':
            Channel(0).set_volume(1)
        else:
            Channel(0).set_volume(0)

    def on_hover(self):
        pass

    def on_unhover(self):
        pass
