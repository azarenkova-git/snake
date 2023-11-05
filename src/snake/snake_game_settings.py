import pygame

from src.utils import colors


class SnakeGameSettings:
    """Класс для хранения настроек игры"""

    _snake_color: pygame.Color
    _number_of_tiles: int
    _speed_multiplication_coefficient: float
    _rate_of_random_bonuses: float
    _username: str

    def __init__(self):
        self._snake_color = colors.Colors.GREEN
        self._number_of_tiles = 32
        self._speed_multiplication_coefficient = 1.0
        self._rate_of_random_bonuses = 1.0

    def get_rate_of_random_bonuses(self) -> float:
        """Возвращает частоту появления бонусов"""

        return self._rate_of_random_bonuses

    def set_rate_of_random_bonuses(self, rate_of_random_bonuses: float) -> None:
        """Устанавливает частоту появления бонусов"""

        self._rate_of_random_bonuses = rate_of_random_bonuses

    def get_speed_multiplication_coefficient(self) -> float:
        """Возвращает коэффициент ускорения змеи"""

        return self._speed_multiplication_coefficient

    def set_speed_multiplication_coefficient(
        self, speed_multiplication_coefficient: float
    ) -> None:
        """Устанавливает коэффициент ускорения змеи"""

        self._speed_multiplication_coefficient = speed_multiplication_coefficient

    def get_number_of_tiles(self) -> int:
        """Возвращает количество клеток на поле"""

        return self._number_of_tiles

    def set_number_of_tiles(self, number_of_tiles: int) -> None:
        """Устанавливает количество клеток на поле"""

        self._number_of_tiles = number_of_tiles

    def get_snake_color(self) -> pygame.Color:
        """Возвращает цвет змеи"""

        return self._snake_color

    def set_snake_color(self, snake_color: pygame.Color) -> None:
        """Устанавливает цвет змеи"""

        self._snake_color = snake_color

    def get_tile_size(self) -> int:
        """Возвращает размер клетки на поле"""

        return 10

    def get_username(self) -> str:
        """Возвращает имя пользователя"""

        return self._username

    def set_username(self, username: str) -> None:
        """Устанавливает имя пользователя"""

        self._username = username
