from __future__ import annotations
from collections import defaultdict
from typing import List

import pygame

from src.scenes import abstract_scene


class AbstractGame:
    """Абстрактный класс для работы с игрой. Содержит в себе активную сцену, является точкой входа в программу"""

    _events: list[pygame.event.Event]
    _mouse_pos: tuple[int, int]
    _active_scene: abstract_scene.AbstractScene
    _scores: defaultdict[str, List[int]]

    def __init__(self):
        pygame.init()
        self._scores = defaultdict(list)
        self._events = []
        self._mouse_pos = (0, 0)

    def get_scores(self) -> defaultdict[str, List[int]]:
        """Возвращает словарь с результатами игроков"""

        return self._scores

    def add_score(self, name: str, score: int):
        """Добавляет результат игрока в словарь"""

        self._scores[name].append(score)

    def set_scene(self, scene: abstract_scene.AbstractScene):
        """Устанавливает активную сцену и меняет заголовок окна/размер окна"""

        self._active_scene = scene

    def get_display(self) -> pygame.Surface:
        """Возвращает поверхность, на которой происходит отрисовка"""

        raise NotImplementedError

    def get_events(self) -> list[pygame.event.Event]:
        """Возвращает список событий, которые произошли за последний кадр"""

        return self._events

    def get_mouse_pos(self) -> tuple[int, int]:
        """Возвращает координаты мыши"""

        return self._mouse_pos
