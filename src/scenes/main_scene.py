from __future__ import annotations
import math
import random

import pygame

from src.components import text_component
from src.scenes import abstract_scene
from src.snake import snake
from src.tiles import abstract_bonus, food
from src.game import game
from src.utils import coordinates, colors


class MainScene(abstract_scene.AbstractScene):
    """Класс сцены игрового поля"""

    _tile_size: int
    _number_of_tiles: int
    _snake_color: pygame.Color
    _snake: snake.Snake
    _bonuses: list[abstract_bonus.AbstractBonus]
    _score: int
    _speed_coeff: int
    _score_text: text_component.TextComponent

    def __init__(self, game: game.Game):
        self._tile_size = 10
        self._number_of_tiles = 64
        super().__init__(
            game,
            coordinates.Coordinates(
                self._tile_size * self._number_of_tiles,
                self._tile_size * self._number_of_tiles,
            ),
            "Игровое поле",
        )
        self._snake_color = colors.Colors.GREEN
        self._snake = snake.Snake(self)
        self._bonuses = []
        self._score = 0
        self._speed_coeff = 1
        self._score_text = text_component.TextComponent(
            game,
            text=f"Счет: {self._score}",
        )
        self.add_bonus(food.Food(self))

    def get_tick_rate(self) -> int:
        return self._tick_rate * self._speed_coeff

    def increase_speed_of_snake(self):
        self._speed_coeff *= 1.2

    def get_score(self) -> int:
        """Возвращает счет игрока"""

        return self._score

    def get_bonuses(self) -> list[abstract_bonus.AbstractBonus]:
        """Возвращает список бонусов на поле"""

        return self._bonuses

    def get_speed_coeff(self) -> int:
        """Возвращает коэффициент скорости игры"""

        return self._speed_coeff

    def get_tile_size(self) -> int:
        """Возвращает размер клетки на поле"""

        return self._tile_size

    def get_snake_color(self) -> pygame.Color:
        """Возвращает цвет змеи"""

        return self._snake_color

    def get_snake(self) -> snake.Snake:
        """Возвращает объект змеи"""

        return self._snake

    def remove_bonus(self, bonus: abstract_bonus.AbstractBonus) -> None:
        """Удаляет бонус с поля"""

        self._bonuses.remove(bonus)

    def add_bonus(self, bonus: abstract_bonus.AbstractBonus) -> None:
        """Добавляет бонус на поле"""

        self._bonuses.append(bonus)

    def update(self) -> None:
        """Обновляет сцену"""

        super().update()
        self._snake.update()

    def render(self) -> None:
        """Отрисовывает сцену"""

        super().render()

        self._score_text.render()

        self._snake.render()

        for bonus in self._bonuses:
            bonus.render()

    def game_over(self) -> None:
        """Завершает игру"""

        exit()

    def get_initial_snake_coordinates(self) -> coordinates.Coordinates:
        """Возвращает координаты начальной позиции змеи"""

        raw_x = math.floor(self._window_size.x / 2)
        raw_y = math.floor(self._window_size.y / 2)

        x = math.floor(raw_x / self._tile_size) * self._tile_size
        y = math.floor(raw_y / self._tile_size) * self._tile_size

        return coordinates.Coordinates(x, y)

    def provide_free_tile_coordinates(self) -> coordinates.Coordinates:
        """Возвращает координаты свободной клетки на поле"""

        while True:
            coordinates = self._create_random_tile_coordinates()

            if not self._is_tile_occupied(coordinates):
                return coordinates

    def _is_tile_occupied(self, coordinates: coordinates.Coordinates) -> bool:
        """Проверяет, занята ли клетка на поле"""

        if self._snake.is_occupying_tile_by_coordinates(coordinates):
            return True

        for bonus in self._bonuses:
            if bonus.is_occupying_tile_by_coordinates(coordinates):
                return True

        return False

    def increment_score_by_one(self):
        """Увеличивает счет игрока на 1"""

        self._score += 1
        self._score_text.set_text(f"Счет: {self._score}")

    def _create_random_tile_coordinates(self) -> coordinates.Coordinates:
        """Создает координаты случайной клетки на поле"""

        x_raw = random.randint(0, self._window_size.x)
        x_adjusted = math.floor(x_raw / self._tile_size) * self._tile_size

        y_raw = random.randint(0, self._window_size.y)
        y_adjusted = math.floor(y_raw / self._tile_size) * self._tile_size

        return coordinates.Coordinates(x_adjusted, y_adjusted)
