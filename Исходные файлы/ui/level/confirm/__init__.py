from pygame.sprite import Group

from .box import Box
from .cancel import Cancel
from .complete import Complete
from objects.backgroundFogging import BackgroundFogging





class LevelConfirm(Group):

    def __init__(self,scene) -> None:
        
        # сохранения ссылки на экран уровня для возможности
        # добавления и удаления из очереди отрисовки
        # и очереди обработки событий
        self.scene = scene

        # добавление спрайтов в группу
        super().__init__(
            BackgroundFogging(scene),

            Box(scene),
            Cancel(scene),
            Complete(scene),
        )

    def __call__(self) -> None:
        self.scene.sprites.add(self)

    def close(self) -> None:
        self.scene.sprites.remove(self)
