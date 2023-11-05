from __future__ import annotations

from src.game import game


class AbstractComponent:
    """Класс для всех компонентов"""

    _game: game.Game

    def __init__(self, game: game.Game):
        self._game = game

    def get_game(self) -> game.Game:
        """Возвращает объект игры"""

        return self._game

    def update(self) -> None:
        """Обновляет компонент"""

        pass

    def render(self) -> None:
        """Отрисовывает компонент"""

        pass
