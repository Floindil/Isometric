from core.Configuration import EntityStates
from scenes.entities.Entity import Entity

class EntityManager:

    def __init__(self) -> None:
        self.__entities = {}

    @property
    def entities(self) -> dict:
        return self.__entities

    def register_entity(self, entity: Entity):
        self.__entities.update({entity.id: entity})

    def get_entity(self, id: str) -> Entity:
        return self.__entities.get(id)
    
    def unregister_entity(self, id: str) -> None:
        self.__entities.pop(id)

    def update(self) -> None:
        active_entities: list[Entity] = self.entities.values()
        for entity in active_entities:
            entity.update()
            if entity.state == EntityStates.DEAD:
                self.unregister_entity(entity.id)