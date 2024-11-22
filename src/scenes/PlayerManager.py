import pygame
from core.Configuration import Player, Directions, EntityStates
from scenes.entities.Entity import Entity

class PlayerManager:

    def __init__(self, player_entity: Entity) -> None:
        self.__player = player_entity
        self.__player._speed = Player.SPEED
        self.__key_watch = []

    @property
    def player(self) -> Entity:
        return self.__player

    def update(self):

        movement = self.process_input()

        if self.player._state == EntityStates.ATTACKING:
            if self.player.loops > 0:
                self.player.set_state(EntityStates.IDLE)

        elif self.player._state == EntityStates.ROLLING:
            movement = self.directional_movement(self.player._direction, 5)
            self.update_location(movement)
            if self.player.loops > 0:
                self.player.set_state(EntityStates.IDLE)

        elif movement != [0, 0, 0]:
            direction = self.get_direction(movement)
            self.player._direction = direction
            self.player.set_state(EntityStates.WALKING)
            self.update_location(movement)
        else:
            self.player.set_state(EntityStates.IDLE)

        self.player.update()

    def update_location(self, movement: list[int, int, int]):
        x = self.__player.x + movement[0]
        y = self.__player.y + movement[1]
        z = self.__player.z + movement[2]
        self.__player.set_location([x, y, z])

    def update_key_watch(self, key: int, state: bool) -> bool:
        if state and key not in self.__key_watch:
            self.__key_watch.append(key)
            return True

        elif not state and key in self.__key_watch:
            self.__key_watch.remove(key)

        return False

    def process_input(self) -> list[int, int, int]:

        keys = pygame.key.get_pressed()

        if self.update_key_watch(Player.ATTACK, keys[Player.ATTACK]):
            self.player.set_state(EntityStates.ATTACKING)

        if self.update_key_watch(Player.ROLL, keys[Player.ROLL]):
            self.player.set_state(EntityStates.ROLLING)

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
    
    @staticmethod
    def directional_movement(direction: str, movement_lenght: int):
        
        movement = [0, 0, 0]

        if Directions.N in direction.lower():
            movement[1] -= movement_lenght

        elif Directions.S in direction.lower():
            movement[1] += movement_lenght

        if Directions.E in direction.lower():
            movement[0] += movement_lenght

        elif Directions.W in direction.lower():
            movement[0] -= movement_lenght
        
        return movement