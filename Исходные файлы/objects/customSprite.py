import pygame
from pygame import Surface
from pygame.event import Event
from pygame.mixer import Channel
from pygame.mixer import Sound
from pygame.sprite import Sprite

from .events import DRAW_EVENT




class CustomSprite(Sprite):
    '''
    Субкласс класса Sprite.

    Класс спрайтов с состояниями и
    ссылочной связью с экраном.
    
    Состояние имеет название и определяет
    текущее изображение и позицию спрайта.

    Состояние спрайта изменяется путем передачи
    названия состояния аттрибуту state.
    '''
    
    #### PROPERTIES ####

    #### image ####

    @property
    def image(self) -> Surface:
        return self._image

    @image.setter
    def image(self, image:Surface) -> None:
        image_size = list(map(
            lambda size: size*self.scene.size_hint,
            image.get_size(),
        ))
        
        self._image = pygame.transform.smoothscale(image, image_size)
        if hasattr(self, 'rect'):
            x, y = self.rect.x, self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
        else:
            self.rect = self.image.get_rect()

    #### state ####

    @property
    def state(self) -> str:
        return self._state
    
    @state.setter
    def state(self, state:str) -> None:
        self._state = state
        self.image = self.states[self._state][0]
        self.rect.x, self.rect.y = (
            round(self.scene.pos[0]+self.states[state][1][0]*self.scene.size_hint),
            round(self.scene.pos[1]+self.states[state][1][1]*self.scene.size_hint),
        )
        pygame.event.post(Event(DRAW_EVENT))
    
    @property
    def hoverable(self) -> bool:
        '''
        Используется сценой при инициализации группы спрайтов сцены.

        При наличии методов on_hover и on_unhover,
        экземпляр автоматически заносится в список спрайтов,
        поддерживающих наведение курсором мыши.
        '''

        if (
            hasattr(self, 'on_hover')
            and hasattr(self, 'on_unhover')
        ):
            return True

        return False
            
    @property
    def clickable(self) -> bool:
        '''
        Используется сценой при инициализации группы спрайтов сцены.

        При наличии метода on_click,
        экземпляр автоматически заносится в список спрайтов,
        поддерживающих наведение курсором мыши.
        '''

        if hasattr(self, 'on_click'):
            return True
        
        return False

    #### METHODS ####

    #### constructor ###
    def __init__(
        self,
        scene: object,
        states: dict,
        state: str = None, # можно не указывать при инициализации
    ):
        '''
        Параметр state можно не указывать при инициализации:
        подходит для спрайтов с одним состоянием
        или спрайтов, состояние которых определяется при вызове.
        '''
        
        super().__init__()

        # сохранение ссылки на связанный экран
        self.scene = scene
        
        # замена путей изображений на сами изображения
        # замена путей звуков, если они добавлены, на сами звуки
        for key in states.keys():
            if type(states[key][0]) != Surface:
                states[key][0] = pygame.image.load(states[key][0])
            if len(states[key]) == 3:
                states[key][2] = Sound(states[key][2])
        self.states = states
        
        if not state:
            self.state = list(self.states.keys())[0]
        else:
            self.state = state

        # используется для сброса состояния при входе на сцену
        self.dstate = self.state

    # def on_click(self) -> None:
        '''
        Выполняется при нажатии на спрайт.
        Вызывается в main.py для всех спрайтов текущего экрана,
        с определённым методом.
        '''

    # def on_hover(self) -> None:
        '''
        Выполняется при наведении на спрайт,
        с определённым методом.
        '''

    # def on_unhover(self) -> None:
        '''
        Выполняется при прекращении наведения на спрайт,
        с определённым методом.
        '''

    def switch_state(
        self,
        state: str = None,
    ) -> None:
        '''
        Вместо обычной установки состояния через свойство state,
        воспроизводит звук состояния, если установлен.

        Цикличная смена состояния,
        если не указан параметр state
        '''

        # установка состояния по значению
        if state:
            self.state = state

        # цилкичная смена состояния
        else:
            states_names = list(self.states.keys())
            cur_state_i = states_names.index(self.state)
            new_state_i = cur_state_i - 1
            self.state = states_names[new_state_i]
            self.current_state = states_names[new_state_i]
            
        if len(self.states[self._state]) == 3:
            Channel(1).play(self.states[self._state][2])

    def update_pos_size(self) -> None:
        self.state = self.state

    def scene_enter(self):
        '''
        Вызывается классом Scene при входе на сцену.

        Сбрасывает состояния спрайта в стандартное.
        '''

        self.state = self.dstate

    def scene_leave(self):
        '''
        Вызывается классом Scene при выходе их сцены.
        '''
