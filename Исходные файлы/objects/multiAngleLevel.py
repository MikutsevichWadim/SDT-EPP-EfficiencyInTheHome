from .customGroup import CustomGroup
from .level import Level




class MultiAngleLevel(Level):

    def __init__(
            
        self,

        # MultiAngleLevel -> Level -> Scene
        manager:object,
        sprites:list[object],
        surface:object,

        # MultiAngleLevel -> Level
        level_index:int,

        # MultiAngleLevel
        angle:str,

    ) -> None:
        
            
        super().__init__(
            manager=manager,
            sprites=sprites,
            surface=surface,
            level_index=level_index,
        )

        # так как self.sprites используеться для отрисовки
        # и не содержит всех спрайтов, необходимо сохранить
        # список всех спрайтов в отдельную переменную
        self.all_sprites = sprites

        self.angles = dict()
        for sprite in self.sprites:
            for angle_key in sprite.angles.keys():
                if angle_key not in self.angles.keys():
                    self.angles[angle_key] = []
                self.angles[angle_key].append(sprite)

        for angle_key in self.angles.keys():
            self.angles[angle_key] = CustomGroup(self.angles[angle_key])
        
        self.switch_angle(angle)

    def switch_angle(self, angle):
        self._angle = angle
        self.sprites = self.angles[angle]
        for sprite in list(self.sprites):
            sprite.switch_angle(angle)
        # self.manager.menu(self)
            
    def set_menu(self, menu:object):
        for angle_key in self.angles:
            menu(self, self.angles[angle_key])

    def enter(self):
        for sprite in self.all_sprites:
            sprite.scene_enter()

    def leave(self):
        for sprite in self.all_sprites:
            sprite.scene_leave()
