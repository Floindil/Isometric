import pygame
from core.Configuration import Player, Directions, EntityStates
from scenes.entities.Entity import Entity

class PlayerManager:

    def __init__(self, player_entity: Entity) -> None:
        self.__player = player_entity
        self.__player._speed = Player.SPEED

    @property
    def player(self) -> Entity:
        return self.__player

    def update(self):
        movement = self.raycast()
        if self.__player._state == EntityStates.ATTACKING:
            pass
        elif self.__player._state == EntityStates.ROLLING:
            pass
        elif movement != [0, 0, 0]:
            direction = self.get_direction(movement)
            self.__player._direction = direction
            self.__player.set_state(EntityStates.WALKING)
            self.update_location(movement)
        else:
            self.__player.set_state(EntityStates.IDLE)

        self.__player.update()

    def update_location(self, movement: list[int, int, int]):
        x = self.__player.x + movement[0]
        y = self.__player.y + movement[1]
        z = self.__player.z + movement[2]
        self.__player.set_location([x, y, z])

    def raycast(self) -> list[int, int, int]:
        keys = pygame.key.get_pressed()
        movement = [0, 0, 0]

        if keys[Player.UP]:
            movement[1] -= self.__player._speed

        if keys[Player.DOWN]:
            movement[1] += self.__player._speed

        if keys[Player.LEFT]:
            movement[0] -= self.__player._speed

        if keys[Player.RIGHT]:
            movement[0] += self.__player._speed

        return movement

    @staticmethod
    def get_direction(movement: list[int, int, int]) -> str:
        if movement[1] < 0:
            if movement[0] > 0:
                direction = Directions.NE
            elif movement[0] < 0:
                direction = Directions.NW
            else:
                direction = Directions.N
        
        elif movement[1] > 0:
            if movement[0] > 0:
                direction = Directions.SE
            elif movement[0] < 0:
                direction = Directions.SW
            else:
                direction = Directions.S
        
        else:
            if movement[0] > 0:
                direction = Directions.E
            elif movement[0] < 0:
                direction = Directions.W
        
        return direction
