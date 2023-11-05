import pygame

import src


class AbstractTile(src.components.AbstractComponent):
    """Абстрактный класс тайла на игровом поле. Например - сегмент змеи или яблоко"""

    _coordinates: src.utils.Coordinates
    _main_scene: src.scenes.MainScene
    _color: pygame.Color

    def __init__(
        self,
        main_scene: src.scenes.MainScene,
        color: pygame.Color,
        coordinates: src.utils.Coordinates,
    ) -> None:
        super().__init__(main_scene.get_game())
        self._coordinates = coordinates
        self._main_scene = main_scene
        self._color = color

    def render(self) -> None:
        """Отрисовывает тайл"""

        pygame.draw.rect(self._game.get_display(), self._color, self._get_rect())

    def _get_rect(self) -> pygame.Rect:
        """Возвращает прямоугольник, который занимает тайл"""

        return pygame.Rect(
            self._coordinates.x,
            self._coordinates.y,
            self._main_scene.get_tile_size(),
            self._main_scene.get_tile_size(),
        )

    def is_occupying_tile_by_coordinates(self, coordinates: Coordinates) -> bool:
        """Возвращает True, если тайл занимает тайл с переданными координатами"""

        return self._coordinates == coordinates

    def is_out_of_bounds(self) -> bool:
        """Возвращает True, если тайл вышел за границы игрового поля"""

        window_size = self._main_scene.get_window_size()

        return (
            self._coordinates.x < 0
            or self._coordinates.x > window_size.x
            or self._coordinates.y < 0
            or self._coordinates.y > window_size.y
        )

    def intersects_with(self, other: "AbstractTile") -> bool:
        """Возвращает True, если тайл пересекается с другим тайлом"""

        return self._get_rect().colliderect(other._get_rect())

    def get_coordinates(self) -> src.utils.Coordinates:
        """Возвращает координаты тайла"""

        return self._coordinates.copy()
