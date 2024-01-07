from objects.multiAngleSprite import MultiAngleSprite




class AngleSelectorShower(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:
        
        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl2/sprites/angleSelectorShower/main-default.png',
                    [965,309],
                ],
                'hovered': [
                    'scenes/levels/lvl2/sprites/angleSelectorShower/main-hovered.png',
                    [965,309],
                ],
            },
            'shower': {
                'default': [
                    'scenes/levels/lvl2/sprites/angleSelectorShower/shower-default.png',
                    [681, 935],
                ],
                'hovered': [
                    'scenes/levels/lvl2/sprites/angleSelectorShower/shower-hovered.png',
                    [681, 935],
                ],
            },
        }

        state = 'default'
        
        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )

    def on_click(self) -> None:
        angles = ['main', 'shower']
        self.scene.switch_angle(angles[angles.index(self._angle)-1])
    
        self.state = 'default'

    def on_hover(self) -> None:
        self.state = 'hovered'

    def on_unhover(self) -> None:
        self.state = 'default'
