from objects.multiAngleSprite import MultiAngleSprite




class Door(MultiAngleSprite):

    def __init__(
        self,
        scene: object,
    ) -> None:

        angles = {
            'main': {
                'default': [
                    'scenes/levels/lvl2/sprites/door/default.png',
                    [26,254],
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
        self.scene.confirm()

# from objects.button import Button




# class Door(Button):

#     def __init__(self,scene):

#         states = {
#             'default': 'scenes/levels/lvl2/sprites/door/default.png',
#         }

#         pos = [26,254]
        
#         super().__init__(
#             scene=scene,
#             pos=pos,
#             states=states,
#         )

#     def on_click(self):
#         super().on_click()
#         self.scene.confirm()

#     def on_hover(self):
#         pass

#     def on_unhover(self):
#         pass
