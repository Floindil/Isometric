from core.Configuration import EntityStates
from scenes.Scene import Scene
from scenes.entities.Entity import Entity
from assets.animations.Animation import Animation
from scenes.PlayerManager import PlayerManager

class TestScene(Scene):
    
    def __init__(self) -> None:
        super().__init__()

    def start(self) -> None:
        super().start()

        player_walk = Animation("character", EntityStates.WALKING)
        player_idle = Animation("character", EntityStates.IDLE)
        player_roll = Animation("character", EntityStates.ROLLING)
        player_attack = Animation("character", EntityStates.ATTACKING)

        self.assetManager.register_asset(player_attack.id, player_attack.load_frames())
        self.assetManager.register_asset(player_idle.id, player_idle.load_frames(frames_x=4))
        self.assetManager.register_asset(player_roll.id, player_roll.load_frames())
        self.assetManager.register_asset(player_walk.id, player_walk.load_frames())
        
        player = Entity("player")
        player.link_animation(EntityStates.ATTACKING, player_attack)
        player.link_animation(EntityStates.IDLE, player_idle)
        player.link_animation(EntityStates.WALKING, player_walk)
        player.link_animation(EntityStates.ROLLING, player_roll)

        player.set_state(EntityStates.IDLE)

        self.__playerManager = PlayerManager(player)

    def update(self) -> None:
        super().update()
        self.__playerManager.update()
        player = self.__playerManager.player
        if player.animation_context:
            id, direction, index = player.animation_context
            player_current_frame = self.assetManager.get_animation_frame(id, direction, index)
            self._render_kontext.append((player_current_frame, [player.x, player.y]))


        