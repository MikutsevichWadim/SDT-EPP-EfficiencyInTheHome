import pygame

from .customSprite import CustomSprite




class MultiAngleSprite(CustomSprite):

    # angle setter
    def angle(self, value:str):
        self.states = self.angles[value]
        self.state = self.state

    angle = property(None, angle)

    def __init__(
        self,
        scene: object,
        angles: dict,
        state: str,
    ) -> None:
        
        super().__init__(
            scene = scene,
            state = state,

            # сохраняет набор состояний первого ракурса
            states = angles[list(angles.keys())[0]],
        )

        for angle in angles:
            for state in list(angles[angle].keys()):
                if type(angles[angle][state][0]) == str:
                    angles[angle][state][0] = pygame.image.load(angles[angle][state][0])
        self.angles = angles

    def switch_angle(self, angle:str) -> None:
        self._angle = angle
        self.states = self.angles[angle]
        self.state = self.state
