import pygame

class Eventhandler:
    def __init__(self) -> None:
        pass

    def run(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        return True