import pygame
import math

squash_factor = 4
        
def calc_isometric_rect_points(rect: pygame.Rect, y_offset = 0):
    p1 = [rect.x+rect.width/2, rect.y - y_offset]
    p2 = [rect.x+rect.width, rect.y+rect.height/squash_factor - y_offset]
    p3 = [rect.x+rect.width/2, rect.y+rect.height*2/squash_factor - y_offset]
    p4 = [rect.x, rect.y+rect.height/squash_factor - y_offset]
    return [p1, p2, p3, p4]

def draw_rect_isometric(surface: pygame.Surface, rect: pygame.Rect):
    points = calc_isometric_rect_points(rect)
    pygame.draw.lines(surface, "red", True, points)

class Box:
    def __init__(self, x: int, y: int, width: int, lenght: int, height: int) -> None:
        self.rect = pygame.Rect(x, y, width, lenght)
        self.height = height

    def draw(self, surface):
        lower_rect = calc_isometric_rect_points(self.rect)
        upper_rect = calc_isometric_rect_points(self.rect, self.height*2/squash_factor)
        pygame.draw.lines(surface, "red", True, lower_rect)
        pygame.draw.lines(surface, "red", True, upper_rect)
        pygame.draw.line(surface, "red", lower_rect[0], upper_rect[0])
        pygame.draw.line(surface, "red", lower_rect[1], upper_rect[1])
        pygame.draw.line(surface, "red", lower_rect[2], upper_rect[2])
        pygame.draw.line(surface, "red", lower_rect[3], upper_rect[3])

pygame.init()

screen_size = (1000, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Isometric")

surface = pygame.Surface(screen_size)
surface.fill("light grey")

rect = pygame.Rect(100,100,100,100)

box1 = Box(300, 300, 100, 100, 50)
box2 = Box(350, 325, 100, 100, 50)
box3 = Box(350, 275, 100, 100, 50)
box4 = Box(400, 300, 100, 100, 50)

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

    pygame.draw.circle(screen,(255, 0, 0), (location[0], location[1]), 10)
    pygame.draw.line(screen, pygame.Color("green"), location, target)
    draw_rect_isometric(screen, rect)
    box1.draw(screen)
    box2.draw(screen)
    box3.draw(screen)
    box4.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
