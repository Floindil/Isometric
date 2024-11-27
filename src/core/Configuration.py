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
    ATTACK = pygame.K_o
    ROLL = pygame.K_p

class Image:
    TYPE = "image"
    SUFFIX = ".png"
    PATH = "src/assets/images/"

class Animation:
    TYPE = "animation"
    SUFFIX = ".png"
    PATH = "src/assets/animations/"
    FRAMERATE = 4
    SHEETSIZE = [6, 4] # Frames per side
    FRAMESIZE = 256

class Sound:
    TYPE = "sound"
    SUFFIX = ".mp3"
    PATH = "src/assets/sounds/"

class Directions:
    S = "180"
    SW = "225"
    SE = "135"
    N = "000"
    NW = "315"
    NE = "045"
    W = "270"
    E = "090"

class EntityStates:
    WALKING = "walk"
    ATTACKING = "attack"
    DYING = "dying"
    DEAD = "dead"
    IDLE = "idle"
    ROLLING = "roll"
    