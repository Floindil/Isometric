import pygame

class Display:
    SIZE: tuple = (1500, 1000)
    CAPTION: str = "Ismoetric Stuff"

class Player:
    SPEED = 5
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d

class Image:
    TYPE = "image"
    SUFFIX = ".png"
    PATH = "src/assets/images/"

class Animation:
    TYPE = "animation"
    SUFFIX = ".png"
    PATH = "src/assets/animations/"
    FRAMERATE = 4

class Sound:
    TYPE = "sound"
    SUFFIX = ".mp3"
    PATH = "src/assets/sounds/"

class Directions:
    S = "down"
    SW = "downLeft"
    SE = "downRight"
    N = "up"
    NW = "upLeft"
    NE = "upRight"
    W = "left"
    E = "right"

class EntityStates:
    WALKING = "walk"
    ATTACKING = "attack"
    DEAD = "death"
    IDLE = "idle"
    ROLLING = "roll"
    