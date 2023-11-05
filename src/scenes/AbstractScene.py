import pygame

import src


class AbstractScene(src.components.AbstractComponent):
    """Абстрактная сцена. Обычно всегда рендерится на весь экран."""

    _window_size: src.utils.Coordinates
    _title: str
    _fill_color: src.utils.Colors.BLACK

    def __init__(
        self, game: src.game.Game, window_size: src.utils.Coordinates, title
    ) -> None:
        super().__init__(game)
        self._window_size = window_size
        self._title = title

    def get_window_size(self) -> src.utils.Coordinates:
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
