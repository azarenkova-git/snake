from __future__ import annotations

import pygame

from src.tiles import abstract_tile
from src.scenes import main_scene


class AbstractBonus(abstract_tile.AbstractTile):
    """Абстрактный класс бонуса на карте - например яблока"""

    def __init__(self, main_scene: main_scene.MainScene, color: pygame.Color):
        super().__init__(main_scene, color, main_scene.provide_free_tile_coordinates())

    def on_take(self) -> None:
        """Обработчик события, когда змея съела бонус"""

        raise NotImplementedError()
