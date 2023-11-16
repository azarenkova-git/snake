from __future__ import annotations
from typing import Optional, List

import pygame
from pygame.time import Clock

from src.scenes import abstract_scene, start_scene
from src.game import abstract_game


class RealGame(abstract_game.AbstractGame):
    """Класс для работы с игрой. Содержит в себе активную сцену, является точкой входа в программу"""

    _fps_controller: Clock
    _play_surface: Optional[pygame.Surface]

    def __init__(self):
        super().__init__()
        self._fps_controller = pygame.time.Clock()
        self.set_scene(start_scene.StartScene(self))
        self._start_game()

    def set_scene(self, scene: abstract_scene.AbstractScene):
        """Устанавливает активную сцену и меняет заголовок окна/размер окна"""

        super().set_scene(scene)

        pygame.display.set_caption(scene.get_title())

        self._play_surface = pygame.display.set_mode(scene.get_window_size().to_tuple())

    def get_display(self) -> pygame.Surface:
        """Возвращает поверхность, на которой происходит отрисовка"""

        return self._play_surface

    def _start_game(self):
        """Запускает игру"""

        while True:
            self._game_tick()

    def _game_tick(self):
        """Самый главный метод, который вызывается каждый кадр. Отвечает за обновление и отрисовку сцены"""

        self._events = pygame.event.get()
        self._mouse_pos = pygame.mouse.get_pos()

        # Сохраняем активную сцену в отдельную переменную, так как за время обновления сцены
        # может измениться активная сцена
        active_scene = self._active_scene

        active_scene.update()
        active_scene.render()

        pygame.display.flip()
        self._fps_controller.tick(self._get_tick_rate())

    def _get_tick_rate(self) -> int:
        """Возвращает частоту обновления сцены"""

        if self._active_scene.get_tick_rate() < 5:
            return 5

        return self._active_scene.get_tick_rate()
