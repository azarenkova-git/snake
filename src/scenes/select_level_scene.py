from __future__ import annotations

import enum

from src.components import text_component, button_component
from src.scenes import abstract_scene, main_scene
from src.snake import snake_game_settings
from src.game import game
from src.utils import coordinates


class SnakeLevel(enum.Enum):
    EASY = 1
    STANDARD = 2
    HARD = 3
    SMALL = 4
    STRANGE = 5


class SelectLevelScene(abstract_scene.AbstractScene):
    _snake_game_settings: snake_game_settings.SnakeGameSettings
    _label_text_component: text_component.TextComponent
    _button_components: list[button_component.ButtonComponent]

    def __init__(
        self,
        game: game.Game,
        snake_game_settings: snake_game_settings.SnakeGameSettings,
    ):
        super().__init__(game, coordinates.Coordinates(1100, 600), "Выбор уровня")

        self._snake_game_settings = snake_game_settings

        offset = 70

        initial_offset = 30

        self._label_text_component = text_component.TextComponent(
            self._game, "Выберите уровень:"
        )

        self._button_components = [
            button_component.ButtonComponent(
                self._game,
                "Легкий",
                coordinates.Coordinates(10, initial_offset + offset),
                lambda: self._set_level(SnakeLevel.EASY),
            ),
            button_component.ButtonComponent(
                self._game,
                "Средний",
                coordinates.Coordinates(10, initial_offset + offset * 2),
                lambda: self._set_level(SnakeLevel.STANDARD),
            ),
            button_component.ButtonComponent(
                self._game,
                "Сложный",
                coordinates.Coordinates(10, initial_offset + offset * 3),
                lambda: self._set_level(SnakeLevel.HARD),
            ),
            button_component.ButtonComponent(
                self._game,
                "Маленький",
                coordinates.Coordinates(10, initial_offset + offset * 4),
                lambda: self._set_level(SnakeLevel.SMALL),
            ),
            button_component.ButtonComponent(
                self._game,
                "Странный",
                coordinates.Coordinates(10, initial_offset + offset * 5),
                lambda: self._set_level(SnakeLevel.STRANGE),
            ),
        ]

    def _set_level(self, level: SnakeLevel) -> None:
        match level:
            case SnakeLevel.EASY:
                self._snake_game_settings.set_speed_multiplication_coefficient(1)
                self._snake_game_settings.set_rate_of_random_bonuses(2)

            case SnakeLevel.STANDARD:
                self._snake_game_settings.set_speed_multiplication_coefficient(1.2)
                self._snake_game_settings.set_rate_of_random_bonuses(1)

            case SnakeLevel.HARD:
                self._snake_game_settings.set_speed_multiplication_coefficient(3)
                self._snake_game_settings.set_rate_of_random_bonuses(0.5)

            case SnakeLevel.SMALL:
                self._snake_game_settings.set_number_of_tiles(16)
                self._snake_game_settings.set_speed_multiplication_coefficient(1)

            case SnakeLevel.STRANGE:
                self._snake_game_settings.set_number_of_tiles(64)
                self._snake_game_settings.set_speed_multiplication_coefficient(2.0)
                self._snake_game_settings.set_rate_of_random_bonuses(10)

        self.get_game().set_scene(
            main_scene.MainScene(
                self.get_game(),
                self._snake_game_settings,
            )
        )

    def update(self) -> None:
        super().update()

        for text_component in self._button_components:
            text_component.update()

    def render(self) -> None:
        super().render()

        self._label_text_component.render()

        for text_component in self._button_components:
            text_component.render()
