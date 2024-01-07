# from objects.image import Image
from objects.customSprite import CustomSprite



class WindowsLight(CustomSprite):

    def __init__(self,scene) -> None:

        state='disabled'

        states = {
            'disabled': [
                'assets/null.png',
                [0, 0]
            ],
            'default': [
                'scenes/levels/lvl1/sprites/windowsLight/windowsLight.png',
                [0,0]
            ],
        }

        super().__init__(
            scene=scene,
            state=state,
            states=states,
        )

    def on_click(self) -> bool:
        return True
    
    def switch_state(self, state: str = None) -> None:
        print('kek', self.state)
        return super().switch_state(state)
