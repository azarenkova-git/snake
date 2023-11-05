import src


class AbstractComponent:
    """Класс для всех компонентов"""

    _game: src.game.Game

    def __init__(self, game: src.game.Game):
        self._game = game

    def get_game(self) -> src.game.Game:
        """Возвращает объект игры"""

        return self._game

    def update(self) -> None:
        """Обновляет компонент"""

        pass

    def render(self) -> None:
        """Отрисовывает компонент"""

        pass
