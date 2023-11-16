from __future__ import annotations

from src.game import abstract_game


class AbstractComponent:
    """Класс для всех компонентов"""

    _game: abstract_game.AbstractGame

    def __init__(self, game: abstract_game.AbstractGame):
        self._game = game

    def get_game(self) -> abstract_game.AbstractGame:
        """Возвращает объект игры"""

        return self._game

    def update(self) -> None:
        """Обновляет компонент"""

        pass

    def render(self) -> None:
        """Отрисовывает компонент"""

        pass
