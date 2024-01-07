from objects.background import Background




class Rooms(Background):

    def __init__(self,scene):

        super().__init__(
            background_src='scenes/map/sprites/rooms/rooms.png',
            scene=scene,
        )
        