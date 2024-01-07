import pygame
from pygame.event import Event
from pygame.locals import *

from config import *




DRAW_EVENT = USEREVENT + 1
PRINT_FPS_EVENT = USEREVENT + 2


if PRINT_FPS:
    pygame.time.set_timer(PRINT_FPS_EVENT, 250)




class Events:

    def __init__(self, game):
        self.game = game
        self.scenes = game.scenes
        self.surface = game.scenes.surface

    def __call__(self):

        draw_event_handled = False
        
        for event in pygame.event.get():

            if event.type == DRAW_EVENT and not draw_event_handled:
                self.surface.fill(BACKGROUND)
                self.scenes.scene.sprites.draw(self.surface)
                draw_event_handled = True
                pygame.display.flip()

            elif event.type == MOUSEMOTION:

                multi_layer_hovering = True
                
                for sprite in self.scenes.scene.sprites.hoverable_sprites:
                    if multi_layer_hovering and sprite.rect.collidepoint(event.pos):
                        multi_layer_hovering = sprite.on_hover()
                    else:
                        sprite.on_unhover()

            elif event.type == MOUSEBUTTONDOWN:
                for sprite in self.game.scenes.scene.sprites.clickable_sprites:
                    if sprite.rect.collidepoint(event.pos):
                        multiLayerClick = sprite.on_click()
                        if not multiLayerClick:
                            break

            elif event.type == KEYDOWN:
                if event.key == K_F11:
                    if self.game.surface.get_flags() & FULLSCREEN:
                        self.game.surface = pygame.display.set_mode((900, 600), RESIZABLE)
                    else:
                        self.game.surface = pygame.display.set_mode((0, 0), RESIZABLE | FULLSCREEN)
                self.game.scenes.scene.update_pos_size()

            elif event.type == pygame.VIDEORESIZE:
                self.game.scenes.scene.update_pos_size()
            
            elif event.type == PRINT_FPS_EVENT:
                print(self.game.clock.get_fps())
                
            elif event.type == QUIT:
                self.game.quit()
                return True
            
    def draw(self):
        pygame.event.post(Event(DRAW_EVENT))
