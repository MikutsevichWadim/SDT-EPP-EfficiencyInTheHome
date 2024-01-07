from objects.multiAngleSprite import MultiAngleSprite




class AngleSelectorShelf(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:
        
        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl3/sprites/angleSelectorShelf/main-default.png',
                    [554,531],
                ],
                'hovered': [
                    'scenes/levels/lvl3/sprites/angleSelectorShelf/main-hovered.png',
                    [554,531],
                ],
            },
            'shelf': {
                'default': [
                    'scenes/levels/lvl3/sprites/angleSelectorShelf/shelf-default.png',
                    [681, 935],
                ],
                'hovered': [
                    'scenes/levels/lvl3/sprites/angleSelectorShelf/shelf-hovered.png',
                    [681, 935],
                ],
            },
        }

        state = 'hovered'
        
        super().__init__(
            scene = scene,
            angles = angles,
            state = state,
        )

    def on_click(self) -> None:
        angles = ['main', 'shelf']
        self.scene.switch_angle(angles[angles.index(self._angle)-1])
    
        self.state = 'default'

    def on_hover(self) -> None:
        self.state = 'hovered'

    def on_unhover(self) -> None:
        self.state = 'default'
