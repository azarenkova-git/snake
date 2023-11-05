from __future__ import annotations

import pygame

from src.components import abstract_component
from src.game import game
from src.utils import coordinates, colors


class PanelComponent(abstract_component.AbstractComponent):
    _color: str
    _offset: coordinates.Coordinates
    _callback: callable
    _is_hovered: bool = False

    def __init__(
        self,
        game: game.Game,
        offset: coordinates.Coordinates,
        color: str,
        callback: callable,
    ):
        super().__init__(game)
        self._offset = offset
        self._color = color
        self._callback = callback

    def render(self) -> None:
        super().render()

        pygame.draw.rect(
            self._game.get_display(),
            self._color,
            self._get_rect(),
        )

        if self._is_hovered:
            pygame.draw.rect(
                self._game.get_display(),
                colors.Colors.WHITE,
                self._get_rect(),
                5,
            )

    def update(self) -> None:
        for event in self._game.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._get_rect().collidepoint(event.pos):
                    self._callback()

        mouse_pos = self._game.get_mouse_pos()

        self._is_hovered = self._get_rect().collidepoint(mouse_pos)

    def _get_rect(self) -> pygame.Rect:
        return pygame.Rect(
            self._offset.x,
            self._offset.y,
            100,
            100,
        )
