import pygame
from core.Renderer import Renderer
from core.Eventhandler import Eventhandler
from scenes.testScene import TestScene

class Gameloop:
    def __init__(self) -> None:
        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__renderer = Renderer()
        self.__eventhandler = Eventhandler()
        self.__scene = TestScene()
        self.__scene.start()

    @property
    def running(self) -> bool:
        return self.__running

    def run(self):

        self.__running = self.__eventhandler.run()

        self.__scene.update()

        self.__renderer.render(self.__scene._render_kontext)
        pygame.display.flip()

        self.__clock.tick(60)

        return self.__running