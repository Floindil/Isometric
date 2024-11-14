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
    def __init__(self, x: int, y: int, z: int, width: int, lenght: int, height: int) -> None:
        self.__rect = pygame.Rect(x, y, width, lenght)
        self.__z = z
        self.__height = height

    @property
    def x(self) -> int:
        return self.__rect.x
    
    @property
    def y(self) -> int:
        return self.__rect.y
    
    @property
    def z(self) -> int:
        return self.__z

    def draw(self, surface):
        lower_rect = calc_isometric_rect_points(self.__rect)
        upper_rect = calc_isometric_rect_points(self.__rect, self.__height*2/squash_factor)
        pygame.draw.lines(surface, "red", True, lower_rect)
        pygame.draw.lines(surface, "red", True, upper_rect)
        pygame.draw.line(surface, "red", lower_rect[0], upper_rect[0])
        pygame.draw.line(surface, "red", lower_rect[1], upper_rect[1])
        pygame.draw.line(surface, "red", lower_rect[2], upper_rect[2])
        pygame.draw.line(surface, "red", lower_rect[3], upper_rect[3])

    def collision(self, point: tuple[int, int, int]) -> bool:
        if point[2] > self.__height + self.z or point[2] < self.z:
            return False
        else:
            return self.__rect.collidepoint(point[0], point[1])

pygame.init()

screen_size = (1000, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Isometric")

surface = pygame.Surface(screen_size)
surface.fill("light grey")

rect = pygame.Rect(100,100,100,100)

box1 = Box(300, 300, 0, 100, 100, 50)
box2 = Box(350, 325, 0, 100, 100, 50)
box3 = Box(350, 275, 0, 100, 100, 50)
box4 = Box(400, 300, 0, 100, 100, 50)
boxes = [box1, box2, box3, box4]

clock = pygame.time.Clock()

running = True

location = [50, 50, 0]
speed = 3

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_w]:
        dy = -speed
    elif pressed_keys[pygame.K_s]:
        dy = speed
    else:
        dy = 0
    
    if pressed_keys[pygame.K_d]:
        dx = speed
    elif pressed_keys[pygame.K_a]:
        dx = -speed
    else:
        dx = 0

    temp_location = [location[0]+dx, location[1]+dy, location[2]]

    collision = False
    for box in boxes:
        if box.collision(temp_location):
            collision = True
            
    if not collision:
        location = temp_location

    screen.fill("light grey")

    pygame.draw.circle(screen,(255, 0, 0), (location[0], location[1]), 10)
    draw_rect_isometric(screen, rect)
    box1.draw(screen)
    box2.draw(screen)
    box3.draw(screen)
    box4.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
