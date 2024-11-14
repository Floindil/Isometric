import pygame
from core.Configuration import Display
class Renderer:
    def __init__(self) -> None:
        self.__display = pygame.display.set_mode(Display.SIZE)
        self.__images = []
        self.__coordinates = []

    def render(self) -> None:
        temp_image = pygame.Surface(self.__display.get_size(), pygame.SRCALPHA)
        temp_image.fill("blue")

        for i, image in enumerate(self.__images):
            temp_image.blit(image, self.__coordinates[i])

        self.__display.blit(temp_image, [0, 0])