from __future__ import annotations

import pygame

from src.components import text_component, panel_component, text_input_component
from src.scenes import abstract_scene, select_snake_color_scene
from src.game import abstract_game
from src.snake import snake_game_settings
from src.utils import coordinates, colors


class EnterUsernameScene(abstract_scene.AbstractScene):
    _text_component: text_component.TextComponent
    _text_hint_component: text_component.TextComponent
    _input_component: text_input_component.TextInputComponent
    _snake_game_settings: snake_game_settings.SnakeGameSettings

    def __init__(
        self,
        game: abstract_game.AbstractGame,
        snake_game_settings: snake_game_settings.SnakeGameSettings,
    ):
        super().__init__(game, coordinates.Coordinates(1100, 600), "Выбор цвета змейки")

        self._text_component = text_component.TextComponent(
            self._game,
            "Введите имя пользователя.",
            coordinates.Coordinates(20, 20),
        )

        self._text_hint_component = text_component.TextComponent(
            self._game,
            "Нажмите Enter, чтобы продолжить:",
            coordinates.Coordinates(20, 70),
        )

        self._snake_game_settings = snake_game_settings

        self._input_component = text_input_component.TextInputComponent(
            self._game, coordinates.Coordinates(20, 150)
        )

    def update(self) -> None:
        super().update()

        self._text_component.update()

        self._input_component.update()

        self._text_hint_component.update()

        for event in self._game.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self._enter_username()

    def render(self) -> None:
        super().render()

        self._text_component.render()

        self._text_hint_component.render()

        self._input_component.render()

    def _enter_username(self) -> None:
        username = self._input_component.get_text()

        if not username:
            return

        self._snake_game_settings.set_username(self._input_component.get_text())

        self._game.set_scene(
            select_snake_color_scene.SelectSnakeColorScene(
                self._game, self._snake_game_settings
            )
        )
