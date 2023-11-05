from __future__ import annotations

import pygame

from src.components import abstract_component
from src.utils import coordinates, colors
from src.game import game


class AbstractScene(abstract_component.AbstractComponent):
    """Абстрактная сцена. Обычно всегда рендерится на весь экран."""

    _window_size: coordinates.Coordinates
    _title: str
    _fill_color: pygame.Color
    _tick_rate: int

    def __init__(
        self, game: game.Game, window_size: coordinates.Coordinates, title
    ) -> None:
        super().__init__(game)
        self._tick_rate = 10
        self._fill_color = colors.Colors.BLACK
        self._window_size = window_size
        self._title = title

    def get_window_size(self) -> coordinates.Coordinates:
        """Возвращает размеры окна"""

        return self._window_size

    def get_title(self) -> str:
        """Возвращает заголовок окна"""

        return self._title

    def render(self) -> None:
        """Отрисовывает сцену"""

        self._game.get_display().fill(self._fill_color)

    def update(self) -> None:
        """Обновляет сцену"""

        self._check_for_exit()

    def get_tick_rate(self) -> int:
        """Количество кадров в секунду"""

        return self._tick_rate

    def _check_for_exit(self):
        """
        Проверяет, не было ли события выхода из игры.
        Если было, то завершает игру.
        Потенциально, каждая сцена могла бы самостоятельно обрабатывать это событие, но
        для упрощения реализации, это делается здесь.
        """

        for event in self._game.get_events():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
