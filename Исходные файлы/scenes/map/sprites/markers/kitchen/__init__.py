from scenes.map.objects.marker import Marker




class MarkerKitchen(Marker):

    def __init__(self,scene):

        pos = [1014, 540]

        states = {
            'default': 'scenes/map/sprites/markers/kitchen/default.png',
            'hovered': 'scenes/map/sprites/markers/kitchen/hovered.png',
            'unavailable': 'scenes/map/sprites/markers/kitchen/unavailable.png',
        }

        level_i = 2

        scene_name = 'Level3'
        
        super().__init__(
            scene=scene,
            pos=pos,
            states=states,
            level_i=level_i,
            scene_name=scene_name,
        )
