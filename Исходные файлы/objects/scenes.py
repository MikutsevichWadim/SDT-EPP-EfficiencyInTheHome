from .scene import Scene
from config import *
from ui.menu import Menu




class Scenes:
    '''
    Scenes содержит список сцен
    и отвечает за их переключение.

    Переключение сцен:
    реализуется через передачу свойству scene названия сцены.
    '''

    # PROPERTIES

    @property
    def scene(self) -> Scene:
        return self._scene
    
    @scene.setter
    def scene(self, value:str) -> None:
        self.previous_scene_name = self._scene.__class__.__name__
        # print(self._scene.__class__.__name__, '.leave') # DEBUG
        self._scene.leave()
        self._scene = self.scenes[value]
        self._scene.update_pos_size()
        # print(self._scene.__class__.__name__, '.enter') # DEBUG
        self._scene.enter()

    # METHODS

    # constructor
    def __init__(
        self,
        game:object,
        surface:object,
        scenes:list[object],
    ) -> None:

        self.game = game
        self.surface = surface

        # при инициализации аттрибут _scene не задан,
        # задаётся пустая сцена для поддержки работоспособности
        # scene.leave() в свойстве scene
        from .scene import Scene
        self._scene = Scene(
            manager = self,
            surface = surface,
        )
        
        self.scenes = dict()

        menu = Menu(self)

        for Scene in scenes:
            scene = Scene(
                manager = self,
                surface = self.surface,
            )
            self.scenes[scene.__class__.__name__] = scene
            scene.set_menu(menu)

        self.scene = FIRST_SCENE
