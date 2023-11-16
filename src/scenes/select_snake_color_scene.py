from __future__ import annotations

import pygame

from src.components import text_component, panel_component
from src.scenes import abstract_scene, main_scene, select_level_scene
from src.game import abstract_game
from src.snake import snake_game_settings
from src.utils import coordinates, colors


class SelectSnakeColorScene(abstract_scene.AbstractScene):
    _text_component: text_component.TextComponent
    _panel_components: list[panel_component.PanelComponent]
    _snake_game_settings: snake_game_settings.SnakeGameSettings

    def __init__(
        self,
        game: abstract_game.AbstractGame,
        snake_game_settings: snake_game_settings.SnakeGameSettings,
    ):
        super().__init__(game, coordinates.Coordinates(1100, 600), "Выбор цвета змейки")

        self._snake_game_settings = snake_game_settings

        self._text = text_component.TextComponent(self._game, "Выберите цвет змейки")

        self._panel_components = [
            panel_component.PanelComponent(
                self._game,
                coordinates.Coordinates(20, 80),
                colors.Colors.GREEN,
                lambda: self._select_snake_color(colors.Colors.GREEN),
            ),
            panel_component.PanelComponent(
                self._game,
                coordinates.Coordinates(20, 200),
                colors.Colors.VIOLET,
                lambda: self._select_snake_color(colors.Colors.VIOLET),
            ),
        ]

    def update(self) -> None:
        super().update()

        self._text.update()

        for panel_component in self._panel_components:
            panel_component.update()

    def render(self) -> None:
        super().render()

        self._text.render()

        for panel_component in self._panel_components:
            panel_component.render()

    def _select_snake_color(self, color: pygame.Color) -> None:
        self._snake_game_settings.set_snake_color(color)
        self._game.set_scene(
            select_level_scene.SelectLevelScene(self._game, self._snake_game_settings)
        )
