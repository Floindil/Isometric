import pygame
import os

from core.Configuration import Animation as A

class Animation:
    
    def __init__(self, folder: str, animation: str) -> None:
        self.len = 0
        self.frames = self.load_frames(folder, animation)
        self.count = 0
        self.play = False

    def update(self):
        if self.play:
            if self.count <= self.len * A.FRAMERATE:
                self.count += 1
            else:
                self.count = 0

    def start(self):
        self.play = True

    def stop(self):
        self.play = False
        self.count = 0

    def get_frame(self, direction) -> pygame.Surface:
        i = self.count // A.FRAMERATE
        frame = self.frames.get(direction)[i]
        return frame

    def load_frames(self, folder: str, animation: str) -> dict:
        frames = {}
        path = f"src/assets/animations/{folder}/{animation}/"
        for frame in os.listdir(path):
            surface = pygame.image.load(f"{path}{frame}")
            name_parts = frame.replace(".png", "").split("_")
            direction = name_parts[0]
            index = int(name_parts[-1])
            d = frames.get(direction)
            if not d:
                frames.update({direction: [surface]})
            else:
                frames[direction].insert(index, surface)

            if index > self.len:
                self.len = index
        
        return frames
            

