from scenes.map.objects.marker import Marker




class MarkerRestRoom(Marker):

    def __init__(self,scene):

        pos = [1008, 304]

        states = {
            'default': 'scenes/map/sprites/markers/restRoom/default.png',
            'hovered': 'scenes/map/sprites/markers/restRoom/hovered.png',
            'unavailable': 'scenes/map/sprites/markers/restRoom/unavailable.png',
        }

        level_i = 1

        scene_name = 'Level2'
        
        super().__init__(
            scene=scene,
            pos=pos,
            states=states,
            level_i=level_i,
            scene_name=scene_name,
        )
