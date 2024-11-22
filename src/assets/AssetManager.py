import pygame
from core.Configuration import Animation as A, Image as I, Sound as S

class AssetManager:

    def __init__(self) -> None:
        self.__assets = {
            A.TYPE: {},
            I.TYPE: {},
            S.TYPE: {}
        }

    def register_asset(self, id: str, asset: any) -> None:

        asset_type = self.get_asset_type(asset)

        if not asset_type:
            print("unknow asset type")
            return

        if not self.__assets.get(asset_type):
            self.__assets.update({asset_type: {}})

        self.__assets[asset_type].update({id: asset})

    def get_image(self, id: str) -> pygame.Surface:
        return self.__assets[I.TYPE].get(id)
    
    def get_animation_frame(self, id: str, direction: str, index: int) -> list[pygame.Surface]:
        frame = None
        animation = self.__assets[A.TYPE].get(id)
        if animation:
            frame = animation[direction][index]
        return frame
    
    def get_asset_type(self, asset: any) -> str:

        if isinstance(asset, dict):
            return A.TYPE
        elif isinstance(asset, pygame.Surface):
            return I.TYPE
        elif isinstance(asset, pygame.mixer.Sound):
            return S.TYPE
        else:
            return None