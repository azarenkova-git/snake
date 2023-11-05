from __future__ import annotations

import pygame

from src.components import text_component
from src.scenes import abstract_scene, enter_username_scene
from src.game import game
from src.snake import snake_game_settings
from src.utils import coordinates


class StartScene(abstract_scene.AbstractScene):
    _text: text_component.TextComponent

    def __init__(self, game: game.Game):
        super().__init__(game, coordinates.Coordinates(1100, 600), "Стартовый экран")
        self._text = text_component.TextComponent(
            self._game, "Нажмите любую клавишу, чтобы начать игру"
        )

    def update(self) -> None:
        """Обновляет сцену"""

        super().update()
        for event in self._game.get_events():
            if event.type == pygame.KEYDOWN:
                self._open_change_color_scene()

    def _open_change_color_scene(self) -> None:
        """Открывает сцену выбора цвета змейки"""

        self._game.set_scene(
            enter_username_scene.EnterUsernameScene(
                self._game, snake_game_settings.SnakeGameSettings()
            )
        )

    def render(self) -> None:
        """Отрисовывает сцену"""

        super().render()
        self._text.render()
