import pygame
import math

pygame.init()

screen_size = (1000, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Isometric")

surface = pygame.Surface(screen_size)
surface.fill("light grey")

clock = pygame.time.Clock()

running = True

location = [50, 50]
target = [50, 50]
speed = 3

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            target = pygame.mouse.get_pos()

    if location != target:
        angle = math.atan2(abs(location[1]-target[1]),abs(location[0]-target[0]))
        dx = math.cos(angle)*speed
        dy = math.sin(angle)*speed

        if abs(location[0] - target[0]) < speed and abs(location[1] - target[1]) < speed:
            location[0] = target[0]
            location[1] = target[1]
        else:
            if location[0] > target[0]:
                location[0] -= dx
            else:
                location[0] += dx

            if location[1] > target[1]:
                location[1] -= dy
            else:
                location[1] += dy

    screen.fill("light grey")

    #pygame.draw.rect(screen, (255, 0, 0), (location[0]-25, location[1]-25, 50, 50))
    pygame.draw.circle(screen,(255, 0, 0), (location[0], location[1]), 10)
    pygame.draw.line(screen, pygame.Color("green"), location, target)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
