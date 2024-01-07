class Consumer:
    '''
    Расширение для спрайтов, являющихся непосредственным потребителем.

    Реализует логику для смены состояния "Включён" - "Выключен".
    Автоматически добавляет экземпляр в список потребителей уровня.

    При использовании с другими суперклассами,
    во всех методах дочерних классов требуется
    вызов метода данного класса через Consumer.scene_enter(self) (далее пример):

    def scene_enter(self):
    
        OtherClassExample.scene_enter(self)

        Consumer.scene_enter(self)

    '''

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        # print(f'[{self.scene.__class__.__name__}][{self.__class__.__name__}][{value}]') # DEBUG
        self._enabled = value
    
    def __init__(
        self,
        scene: object,
    ) -> None:
        
        scene.consumers.append(self)
        
        self.scene = scene
        
        self.enabled = True

    def switch_state(
        self,
    ) -> None:
        
        '''
        Расширение стандартного метода
        цикличным переключением аттрибута "enabled".
        '''
        
        self.enabled = not self.enabled

    def scene_enter(self):
        '''
        Сбрасывает состояние спрайта во "Включён"
        '''
        self.enabled = True
