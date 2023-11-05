from __future__ import annotations

import pygame

from src.components import text_component
from src.utils import colors, coordinates
from src.game import game


class ButtonComponent(text_component.TextComponent):
    _hovered: bool
    _callback: callable

    def __init__(
        self,
        game: game.Game,
        text: str,
        coordinates: coordinates.Coordinates,
        callback: callable,
    ):
        super().__init__(game, text, coordinates)
        self._hovered = False
        self._callback = callback

    def update(self) -> None:
        super().update()

        mouse_pos = self.get_game().get_mouse_pos()

        self._hovered = self._get_rect().collidepoint(mouse_pos)

        events = self.get_game().get_events()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self._hovered:
                self._callback()

    def render(self) -> None:
        super().render()

        if self._hovered:
            pygame.draw.rect(
                self._game.get_display(),
                colors.Colors.WHITE,
                self._get_rect(),
                1,
            )
