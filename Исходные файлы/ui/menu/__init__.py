from .box import Box
from .hamburger import Hamburger
from config import SCENES_WITH_MENU




class Menu:

    def __init__(self, manager):
        self.manager = manager
        self.Hamburger = Hamburger

    def __call__(self, scene, sprites):
        if scene.__class__.__name__ in SCENES_WITH_MENU:
            sprites.add(self.Hamburger(scene, self))

    def open(self):
        Box(self.manager).open()

    def close(self):
        Box(self.manager).close()

    def main_menu(self):
        self.manager.scene = 'MainMenu'
        