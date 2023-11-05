from __future__ import annotations

import pygame

from src.components.abstract_component import AbstractComponent
from src.utils import coordinates, colors
from src.game import game


class TextInputComponent(AbstractComponent):
    """Компонент поля ввода"""

    _coordinates: coordinates.Coordinates
    _text: str

    def __init__(self, game: game.Game, coordinates: coordinates.Coordinates):
        super().__init__(game)
        self._coordinates = coordinates
        self._text = ""

    def _get_rect(self) -> pygame.Rect:
        """Возвращает прямоугольник, в котором находится поле ввода"""

        return pygame.Rect(self._coordinates.x, self._coordinates.y, 400, 50)

    def get_text(self) -> str:
        """Возвращает текст, введенный в поле ввода"""

        return self._text

    def _handle_event(self, event: pygame.event.Event) -> None:
        """Обрабатывает события, связанные с полем ввода"""

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass

            elif event.key == pygame.K_BACKSPACE:
                self._text = self._text[:-1]

            else:
                self._text += event.unicode

    def update(self) -> None:
        """Обновляет состояние поля ввода"""

        for event in self.get_game().get_events():
            self._handle_event(event)

    def render(self):
        """Отрисовывает поле ввода"""

        font = pygame.font.SysFont("monospace", 32)
        text_surface = font.render(self._text, True, colors.Colors.WHITE)
        self.get_game().get_display().blit(
            text_surface, (self._get_rect().x + 5, self._get_rect().y + 5)
        )
        pygame.draw.rect(
            self.get_game().get_display(), colors.Colors.WHITE, self._get_rect(), 2
        )
