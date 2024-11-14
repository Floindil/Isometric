import pygame
from core.Renderer import Renderer
from core.Eventhandler import Eventhandler

class Gameloop:
    def __init__(self) -> None:
        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__renderer = Renderer()
        self.__eventhandler = Eventhandler()

    @property
    def running(self) -> bool:
        return self.__running

    def run(self):

        self.__running = self.__eventhandler.run()

        self.__renderer.render()
        pygame.display.flip()

        self.__clock.tick(60)

        return self.__running