import pygame
from core.Configuration import Display
class Renderer:
    def __init__(self) -> None:
        self.__display = pygame.display.set_mode(Display.SIZE)
        pygame.display.set_caption(Display.CAPTION)

    def render(self, render_kontext) -> None:
        temp_image = pygame.Surface(self.__display.get_size(), pygame.SRCALPHA)
        temp_image.fill("blue")

        for image, coordinates in render_kontext:
            temp_image.blit(image, coordinates)

        self.__display.blit(temp_image, [0, 0])