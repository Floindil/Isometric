import pygame
from core.Renderer import Renderer
from core.Eventhandler import Eventhandler
from assets.animations.Animation import Animation

class Gameloop:
    def __init__(self) -> None:
        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__renderer = Renderer()
        self.__eventhandler = Eventhandler()
        self.attack = Animation("character", "attack")
        self.attack.start()

    @property
    def running(self) -> bool:
        return self.__running

    def run(self):

        self.__running = self.__eventhandler.run()

        self.attack.update()
        self.__renderer.set_images([self.attack.get_frame("down")], [[0,0]])

        self.__renderer.render()
        pygame.display.flip()

        self.__clock.tick(60)

        return self.__running