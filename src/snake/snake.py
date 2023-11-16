from __future__ import annotations
from typing import Optional

import pygame

from src.components import abstract_component
from src.scenes import main_scene
from src.snake import snake_segment
from src.utils import direction, coordinates


class Snake(abstract_component.AbstractComponent):
    _segments: list[snake_segment.SnakeSegment]
    _head_segment: snake_segment.SnakeSegment
    _main_scene: main_scene.MainScene
    _direction: direction.Direction
    _last_segment_previous_coordinates: Optional[coordinates.Coordinates]

    def __init__(self, main_scene: main_scene.MainScene):
        super().__init__(main_scene.get_game())
        self._main_scene = main_scene
        self._segments = []
        self._head_segment = snake_segment.SnakeSegment(
            self,
            main_scene.get_initial_snake_coordinates(),
        )
        self._segments = [self._head_segment]
        self._direction = direction.Direction.RIGHT

    def get_main_scene(self) -> main_scene.MainScene:
        """Возвращает сцену, на которой находится змея"""

        return self._main_scene

    def update(self):
        """Изменяем положение головы змеи"""
        self._validate_direction_and_change()
        self._move_segments()
        self._check_for_boundaries()
        self._check_for_collisions_with_bonuses()

    def _validate_direction_and_change(self):
        """
        Изменяем направление движения змеи.
        Но только в том случае, если оно не прямо противоположно текущему
        """

        for event in self._game.get_events():
            if event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_UP
                    and self._direction != direction.Direction.DOWN
                ):
                    self._direction = direction.Direction.UP
                    break

                elif (
                    event.key == pygame.K_DOWN
                    and self._direction != direction.Direction.UP
                ):
                    self._direction = direction.Direction.DOWN
                    break

                elif (
                    event.key == pygame.K_LEFT
                    and self._direction != direction.Direction.RIGHT
                ):
                    self._direction = direction.Direction.LEFT
                    break

                elif (
                    event.key == pygame.K_RIGHT
                    and self._direction != direction.Direction.LEFT
                ):
                    self._direction = direction.Direction.RIGHT
                    break

    def _move_segments(self):
        """Перемещает голову змеи в нужном направлении и сдвигаем сегменты"""

        # сначала нужно получить координаты хвоста, чтобы сохранить их для потенциального добавления
        # нового сегмента змеи
        self._last_segment_previous_coordinates = self._segments[-1].get_coordinates()

        for segment, next_segment in zip(
            reversed(self._segments[:-1]), reversed(self._segments[1:])
        ):
            next_segment.move_to_segment(segment)

        self._head_segment.move_in_direction(self._direction)

    def _check_for_boundaries(self):
        """Проверка, что столкнулись с концами экрана или сами с собой"""

        if self._head_segment.is_out_of_bounds():
            self._main_scene.game_over()

        # голову не проверяем, она может столкнуться только со стеной (а не сама с собой)
        for segment in self._segments[1:]:
            # проверка на то, что голова врезалась в любой другой элемент змеи (закольцевалась)
            if segment.intersects_with(self._head_segment):
                self._main_scene.game_over()

    def _check_for_collisions_with_bonuses(self):
        """Проверка, что голова змеи столкнулась с бонусом"""

        for bonus in self._main_scene.get_bonuses():
            if self._head_segment.intersects_with(bonus):
                self._main_scene.remove_bonus(bonus)
                bonus.on_take()

    def render(self):
        """Отображаем все сегменты змеи"""

        for segment in self._segments:
            segment.render()

    def add_new_segment(self):
        """Добавляем сегмент к змее"""

        new_segment = snake_segment.SnakeSegment(
            self,
            self._last_segment_previous_coordinates,
        )

        self._segments.append(new_segment)

    def remove_last_segment(self):
        """Удаляем последний сегмент змеи"""

        if len(self._segments) > 1:
            self._segments.pop()

    def is_occupying_tile_by_coordinates(
        self, coordinates: coordinates.Coordinates
    ) -> bool:
        """Проверка, что тело змеи занимает тайл с указанными координатами"""

        for segment in self._segments:
            if segment.is_occupying_tile_by_coordinates(coordinates):
                return True

        return False

    def get_segments_count(self) -> int:
        """Возвращает количество сегментов змеи"""

        return len(self._segments)

    def get_head_segment(self) -> snake_segment.SnakeSegment:
        """Возвращает головной сегмент змеи"""

        return self._head_segment
