from core.Configuration import Directions, EntityStates
from assets.animations.Animation import Animation

class Entity:

    __current_animation: Animation

    def __init__(self, id: str) -> None:
        self.__id = id
        self._location = [0, 0, 0]
        self._image_ids = []
        self._animations = {}
        self._speed = 0
        self.__current_animation = None
        self._collision_boxes = []
        self._direction = Directions.S
        self._state = None
        self.__animated = False

    @property
    def x(self) -> int:
        return self._location[0]

    @property
    def y(self) -> int:
        return self._location[1]

    @property
    def z(self) -> int:
        return self._location[2]

    @property
    def id(self) -> str:
        return self.__id

    @property
    def location(self) -> list[int, int, int]:
        return self._location
    
    @property
    def animation_context(self) -> list[str, str, int]:
        if self.__current_animation:
            return self.__current_animation.id, self._direction, self.__current_animation.index
        
    @property
    def loops(self):
        return self.__current_animation.loops
    
    def set_state(self, state: str) -> None:
        if self._state != state:
            self._state = state
            animation: Animation = self._animations.get(state)
            if animation:
                if self.__current_animation:
                    self.__current_animation.stop()
                animation.start()
    
    def set_location(self, coordinates: list[int, int, int]) -> None:
        self._location = coordinates

    def set_animation(self) -> None:
        self.__current_animation = self._animations.get(self._state)
        self.__current_animation.start()

    def link_animation(self, state: str, animation: Animation) -> None:
        self.__animated = True
        self._animations.update({state: animation})

    def update(self):
        if self.__current_animation:
            if self.__current_animation.type != self._state:
                self.__current_animation.stop()
                self.set_animation()
        else:
            self.set_animation()

        self.__current_animation.update()
        
        

