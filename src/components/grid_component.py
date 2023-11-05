from __future__ import annotations

import pygame

from src.components.abstract_component import AbstractComponent
from src.utils import coordinates, colors
from src.game import game


class GridComponent(AbstractComponent):
    """Компонент поля ввода"""

    _coordinates: coordinates.Coordinates
    _texts: list[list[str]]

    def __init__(
        self,
        game: game.Game,
        coordinates: coordinates.Coordinates,
        texts: list[list[str]],
    ):
        super().__init__(game)
        self._coordinates = coordinates
        self._texts = texts

    def _get_rect(self) -> pygame.Rect:
        """Возвращает прямоугольник, в котором находится поле ввода"""

        return pygame.Rect(self._coordinates.x, self._coordinates.y, 400, 400)

    def update(self) -> None:
        """Обновляет состояние поля ввода"""

    def render(self):
        """Отрисовывает поле ввода"""

        font = pygame.font.SysFont("monospace", 30)

        offset_y = 20

        for texts in self._texts:
            offset_x = 20

            for text in texts:
                self._game.get_display().blit(
                    font.render(text, 1, colors.Colors.WHITE),
                    coordinates.Coordinates(
                        self._coordinates.x + offset_x,
                        self._coordinates.y + offset_y,
                    ).to_tuple(),
                )

                offset_x += 200

            offset_y += 60

        pygame.draw.rect(
            self._game.get_display(),
            colors.Colors.WHITE,
            self._get_rect(),
            1,
        )
