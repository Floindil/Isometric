import pygame
import os

from core.Configuration import Animation as A

class Animation:
    """
    A class to handle animations using Pygame.

    Attributes:
        __id (str): A unique identifier for the animation.
        __len (int): The number of frames in the animation.
        __count (int): The current frame counter.
        __play (bool): A flag indicating whether the animation is playing.
    """

    def __init__(self, folder: str, animation: str) -> None:
        """
        Initializes the Animation object.

        Args:
            folder (str): The folder where the animation frames are stored.
            animation (str): The name of the animation.
        """
        self.__id = f"{folder}_{animation}"
        self.__len = 0
        self.__count = 0
        self.__loops = 0
        self.__play = False

    @property
    def loops(self) -> int:
        return self.__loops

    @property
    def index(self) -> int:
        """
        Gets the current frame index based on the frame rate.

        Returns:
            int: The current frame index.
        """
        return self.__count // A.FRAMERATE
    
    @property
    def id(self) -> str:
        """
        Gets the unique identifier for the animation.

        Returns:
            str: The unique identifier for the animation.
        """
        return self.__id
    
    @property
    def type(self) -> str:
        return self.__id.split("_")[-1]

    def update(self) -> None:
        """
        Updates the animation frame counter if the animation is playing.
        """
        if self.__play:
            if self.__count <= self.__len * A.FRAMERATE:
                self.__count += 1
            else:
                self.__count = 0
                self.__loops +=1

    def start(self) -> None:
        """
        Starts playing the animation.
        """
        self.__play = True

    def stop(self) -> None:
        """
        Stops playing the animation and resets the frame counter.
        """
        self.__play = False
        self.__count = 0
        self.__loops = 0

    def load_frames(self) -> dict:
        """
        Loads animation frames from the specified directory.

        Returns:
            dict: A dictionary containing the loaded frames organized by direction.
        """
        id_split = self.__id.split("_")
        folder = id_split[0]
        animation = id_split[1]

        frames = {}
        path = f"{A.PATH}{folder}/{animation}/"

        for frame in os.listdir(path):
            surface = pygame.image.load(f"{path}{frame}")

            frame_id = frame.replace(A.SUFFIX, "")
            frame_id_split = frame_id.split("_")
            direction = frame_id_split[0]
            index = int(frame_id_split[-1])

            d = frames.get(direction)
            if not d:
                frames.update({direction: [surface]})
            else:
                frames[direction].insert(index, surface)

            if index > self.__len:
                self.__len = index
        
        return frames
