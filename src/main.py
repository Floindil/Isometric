import pygame
from core.Gameloop import Gameloop

pygame.init()

gameloop = Gameloop()

while gameloop.running:
    gameloop.run()

pygame.quit()