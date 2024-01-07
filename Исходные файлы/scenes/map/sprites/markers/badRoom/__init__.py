from scenes.map.objects.marker import Marker




class MarkerBadRoom(Marker):

    def __init__(self,scene):

        pos = [659, 639]

        states = {
            'default': 'scenes/map/sprites/markers/badRoom/default.png',
            'hovered': 'scenes/map/sprites/markers/badRoom/hovered.png',
            'unavailable': 'scenes/map/sprites/markers/badRoom/unavailable.png',
        }

        level_i = 0

        scene_name = 'Level1'
        
        super().__init__(
            scene=scene,
            pos=pos,
            states=states,
            level_i=level_i,
            scene_name=scene_name,
        )
