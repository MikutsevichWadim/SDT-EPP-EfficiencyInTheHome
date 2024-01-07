from scenes.levels.lvl3.objects.stovePowerKnob import StovePowerKnob




class StovePowerKnob1(StovePowerKnob):
    def __init__(self, scene:object):

        pos = [1325, 679]

        super().__init__(
            scene = scene,
            pos = pos,
        )

    def on_click(self):
        super().on_click()
        self.scene.sprites_refs['Stove1'].switch_state()

class StovePowerKnob2(StovePowerKnob):
    def __init__(self, scene:object):

        pos = [1357, 681]

        super().__init__(
            scene = scene,
            pos = pos,
        )

    def on_click(self):
        super().on_click()
        self.scene.sprites_refs['Stove2'].switch_state()
        
class StovePowerKnob3(StovePowerKnob):
    def __init__(self, scene:object):

        pos = [1389, 683]

        super().__init__(
            scene = scene,
            pos = pos,
        )

    def on_click(self):
        super().on_click()
        self.scene.sprites_refs['Stove3'].switch_state()
        
class StovePowerKnob4(StovePowerKnob):
    def __init__(self, scene:object):

        pos = [1421, 684]

        super().__init__(
            scene = scene,
            pos = pos,
        )

    def on_click(self):
        super().on_click()
        self.scene.sprites_refs['Stove4'].switch_state()
        
class StovePowerKnobOven(StovePowerKnob):
    def __init__(self, scene:object):

        pos = [1276, 676]

        super().__init__(
            scene = scene,
            pos = pos,
        )

    def on_click(self):
        super().on_click()
        self.scene.sprites_refs['Oven'].switch_state()
    