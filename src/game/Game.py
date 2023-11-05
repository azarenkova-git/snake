from typing import Optional

import pygame
from pygame.time import Clock

import src


class Game:
    """Класс для работы с игрой. Содержит в себе активную сцену, является точкой входа в программу"""

    _fps_controller: Clock
    _play_surface: Optional[pygame.Surface]
    _active_scene: src.scenes.AbstractScene
    _events: list[pygame.event.Event]

    def __init__(self):
        self._events = []
        self._fps_controller = pygame.time.Clock()
        self.set_scene(src.scenes.StartScene(self))

    def set_scene(self, scene: src.scenes.AbstractScene):
        """Устанавливает активную сцену и меняет заголовок окна/размер окна"""

        self._active_scene = scene
        pygame.display.set_caption(scene.get_title())
        self._play_surface = pygame.display.set_mode(scene.get_window_size().to_tuple())

    def get_display(self) -> pygame.Surface:
        """Возвращает поверхность, на которой происходит отрисовка"""

        return self._play_surface

    def game_tick(self):
        """Самый главный метод, который вызывается каждый кадр. Отвечает за обновление и отрисовку сцены"""

        self._events = pygame.event.get()

        # Сохраняем активную сцену в отдельную переменную, так как за время обновления сцены
        # может измениться активная сцена
        active_scene = self._active_scene

        active_scene.update()
        active_scene.render()

        pygame.display.flip()
        self._fps_controller.tick(23)

    def get_events(self) -> list[pygame.event.Event]:
        """Возвращает список событий, которые произошли за последний кадр"""

        return self._events

    # def show_score(self, choice=1):
    #     """Отображение результата"""
    #
    #     s_font = pygame.font.SysFont("monaco", 24)
    #     s_surf = s_font.render("Score: {0}".format(self.score), True, Colors.BLACK)
    #     s_rect = s_surf.get_rect()
    #     # дефолтный случай отображаем результат слева сверху
    #     if choice == 1:
    #         s_rect.midtop = (80, 10)
    #     # при game_overe отображаем результат по центру
    #     # под надписью game over
    #     else:
    #         s_rect.midtop = (360, 120)
    #     # рисуем прямоугольник поверх surface
    #     self._play_surface.blit(s_surf, s_rect)
    #
    # def game_over(self):
    #     """Функция для вывода надписи Game Over и результатов
    #     в случае завершения игры и выход из игры"""
    #
    #     go_font = pygame.font.SysFont("monaco", 72)
    #     go_surf = go_font.render("Game over", True, Colors.RED)
    #     go_rect = go_surf.get_rect()
    #     go_rect.midtop = (360, 15)
    #     self._play_surface.blit(go_surf, go_rect)
    #     self.show_score(0)
    #     pygame.display.flip()
    #     time.sleep(3)
    #     pygame.quit()
    #     sys.exit()
