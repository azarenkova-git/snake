from collections import defaultdict
from typing import Optional, List

import pygame
from pygame.time import Clock

from src.scenes import abstract_scene, start_scene


class Game:
    """Класс для работы с игрой. Содержит в себе активную сцену, является точкой входа в программу"""

    _fps_controller: Clock
    _play_surface: Optional[pygame.Surface]
    _active_scene: abstract_scene.AbstractScene
    _events: list[pygame.event.Event]
    _scores: defaultdict[str, List[int]]

    def get_scores(self) -> defaultdict[str, List[int]]:
        return self._scores

    def add_score(self, name: str, score: int):
        self._scores[name].append(score)

    def __init__(self):
        pygame.init()
        self._scores = defaultdict(list)
        self._events = []
        self._fps_controller = pygame.time.Clock()
        self.set_scene(start_scene.StartScene(self))
        self.start_game()

    def set_scene(self, scene: abstract_scene.AbstractScene):
        """Устанавливает активную сцену и меняет заголовок окна/размер окна"""

        self._active_scene = scene
        pygame.display.set_caption(scene.get_title())
        self._play_surface = pygame.display.set_mode(scene.get_window_size().to_tuple())

    def get_display(self) -> pygame.Surface:
        """Возвращает поверхность, на которой происходит отрисовка"""

        return self._play_surface

    def start_game(self):
        while True:
            self.game_tick()

    def game_tick(self):
        """Самый главный метод, который вызывается каждый кадр. Отвечает за обновление и отрисовку сцены"""

        self._events = pygame.event.get()

        # Сохраняем активную сцену в отдельную переменную, так как за время обновления сцены
        # может измениться активная сцена
        active_scene = self._active_scene

        active_scene.update()
        active_scene.render()

        pygame.display.flip()
        self._fps_controller.tick(self._get_tick_rate())

    def _get_tick_rate(self) -> int:
        if self._active_scene.get_tick_rate() < 5:
            return 5

        return self._active_scene.get_tick_rate()

    def get_events(self) -> list[pygame.event.Event]:
        """Возвращает список событий, которые произошли за последний кадр"""

        return self._events

    def get_mouse_pos(self) -> tuple[int, int]:
        """Возвращает координаты мыши"""

        return pygame.mouse.get_pos()
