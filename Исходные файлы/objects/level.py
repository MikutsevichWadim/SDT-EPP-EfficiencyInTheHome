from objects.scene import Scene
from ui.level.confirm import LevelConfirm
from ui.level.complete import LevelComplete
from ui.level.exitMainMenu import ExitMainMenu




class Level(Scene):

    def __init__(
        
        self,

        # positioned

        # Level -> Scene
        manager:object,
        surface:object,
        sprites:list[object],

        # Level
        level_index:int,

    ) -> None:
        
        self.consumers = list()

        super().__init__(
            manager=manager,
            sprites=sprites,
            surface=surface,
        )
        
        self.level_index = level_index
        
        self.passed = False
        self.success = .0
        
        self.complete = LevelComplete(scene=self)
        self.confirm = LevelConfirm(scene=self)
        self.exit_main_menu = ExitMainMenu(scene=self)
