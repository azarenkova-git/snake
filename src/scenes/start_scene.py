from __future__ import annotations

import pygame

from src.components import text_component, grid_component
from src.scenes import abstract_scene, enter_username_scene
from src.game import game
from src.snake import snake_game_settings
from src.utils import coordinates


class StartScene(abstract_scene.AbstractScene):
    _text_component: text_component.TextComponent
    _hint_text_component: text_component.TextComponent
    _grid_component: grid_component.GridComponent

    def __init__(self, game: game.Game):
        super().__init__(game, coordinates.Coordinates(1100, 600), "Стартовый экран")

        self._text_component = text_component.TextComponent(
            self._game, "Нажмите любую клавишу, чтобы начать игру"
        )

        self._hint_text_component = text_component.TextComponent(
            self._game, "Топ 5 игроков:", coordinates.Coordinates(20, 70)
        )

        texts = list(
            sorted(
                list(
                    map(
                        lambda item: (item[0], str(max(item[1]))),
                        self._game.get_scores().items(),
                    )
                ),
                key=lambda item: int(item[1]),
                reverse=True,
            )
        )[:5]

        self._grid_component = grid_component.GridComponent(
            self._game, coordinates.Coordinates(20, 120), texts  # type: ignore
        )

    def update(self) -> None:
        """Обновляет сцену"""

        super().update()

        self._grid_component.update()

        self._text_component.update()

        self._hint_text_component.update()

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

        self._text_component.render()

        self._hint_text_component.render()

        self._grid_component.render()
