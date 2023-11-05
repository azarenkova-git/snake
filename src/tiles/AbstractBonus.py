import pygame

import src


class AbstractBonus(src.tiles.AbstractTile):
    """Абстрактный класс бонуса на карте - например яблока"""

    def __init__(self, main_scene: src.scenes.MainScene, color: pygame.Color):
        super().__init__(main_scene, color, main_scene.provide_free_tile_coordinates())

    def on_take(self) -> None:
        """Обработчик события, когда змея съела бонус"""

        raise NotImplementedError()
