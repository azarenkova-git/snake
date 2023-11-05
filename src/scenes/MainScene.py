import math
import random

import pygame

import src


class MainScene(src.scenes.AbstractScene):
    """Класс сцены игрового поля"""

    _tile_size: int
    _snake_color: pygame.Color
    _snake: src.snake.Snake
    _bonuses: list[src.tiles.AbstractBonus]
    _score: int
    _speed_coeff: int
    _score_text: src.components.TextComponent

    def __init__(self, game: src.game.Game):
        super().__init__(
            game,
            src.utils.Coordinates(self._tile_size * 64, self._tile_size * 64),
            "Игровое поле",
        )
        self._snake_color = src.utils.Colors.RED
        self._tile_size = 10
        self._snake = src.snake.Snake(self)
        self._bonuses = []
        self._score = 0
        self._speed_coeff = 1
        self._score_text = src.components.TextComponent(
            game,
            text=f"Счет: {self._score}",
        )

    def get_score(self) -> int:
        """Возвращает счет игрока"""

        return self._score

    def get_bonuses(self) -> list[src.tiles.AbstractBonus]:
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

    def get_snake(self) -> src.snake.Snake:
        """Возвращает объект змеи"""

        return self._snake

    def remove_bonus(self, bonus: src.tiles.AbstractBonus) -> None:
        """Удаляет бонус с поля"""

        self._bonuses.remove(bonus)

    def add_bonus(self, bonus: src.tiles.AbstractBonus) -> None:
        """Добавляет бонус на поле"""

        self._bonuses.append(bonus)

    def update(self) -> None:
        """Обновляет сцену"""

        super().update()
        self._snake.update()

    def render(self) -> None:
        """Отрисовывает сцену"""

        super().render()

        self._snake.render()

        for bonus in self._bonuses:
            bonus.render()

        self._score_text.render()

    def game_over(self) -> None:
        """Завершает игру"""

        exit()

    def get_initial_snake_coordinates(self) -> src.utils.Coordinates:
        """Возвращает координаты начальной позиции змеи"""

        raw_x = math.floor(self._window_size.x / 2)
        raw_y = math.floor(self._window_size.y / 2)

        x = math.floor(raw_x / self._tile_size) * self._tile_size
        y = math.floor(raw_y / self._tile_size) * self._tile_size

        return src.utils.Coordinates(x, y)

    def provide_free_tile_coordinates(self) -> src.utils.Coordinates:
        """Возвращает координаты свободной клетки на поле"""

        while True:
            coordinates = self._create_random_tile_coordinates()

            if not self._is_tile_occupied(coordinates):
                return coordinates

    def _is_tile_occupied(self, coordinates: src.utils.Coordinates) -> bool:
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

    def _create_random_tile_coordinates(self) -> src.utils.Coordinates:
        """Создает координаты случайной клетки на поле"""

        x_raw = random.randint(0, self._window_size.x)
        x_adjusted = math.floor(x_raw / self._tile_size) * self._tile_size

        y_raw = random.randint(0, self._window_size.y)
        y_adjusted = math.floor(y_raw / self._tile_size) * self._tile_size

        return src.utils.Coordinates(x_adjusted, y_adjusted)
