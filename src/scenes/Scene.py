from assets.AssetManager import AssetManager
from scenes.components.ComponentManager import ComponentManager
from scenes.entities.EntityManager import EntityManager

class Scene:

    def __init__(self) -> None:
        self._render_kontext = []
        self.__asset_manager = AssetManager()
        self.__entity_manager = EntityManager()
        self.__component_manager = ComponentManager()

    def start(self) -> None:
        pass

    def update(self) -> None:
        self._render_kontext = []
        self.entityManager.update()
        pass

    @property
    def assetManager(self) -> AssetManager:
        return self.__asset_manager
    
    @property
    def entityManager(self) -> EntityManager:
        return self.__entity_manager