from __future__ import annotations

import pygame

from src.components import abstract_component
from src.game import game
from src.utils import colors
from src.utils.coordinates import Coordinates


class TextComponent(abstract_component.AbstractComponent):
    _text: str
    _font: pygame.font.Font
    _coordinates: Coordinates

    def __init__(
        self,
        game: game.Game,
        text: str,
        coordinates: Coordinates = Coordinates(10, 10),
    ) -> None:
        super().__init__(game)
        self._text = text
        self._font = pygame.font.SysFont("monospace", 30)
        self._coordinates = coordinates

    def _get_rect(self) -> pygame.Rect:
        return pygame.Rect(
            self._coordinates.x,
            self._coordinates.y,
            self._font.size(self._text)[0],
            self._font.size(self._text)[1],
        )

    def render(self) -> None:
        super().render()

        self._game.get_display().blit(
            self._font.render(self._text, 1, colors.Colors.WHITE),
            self._coordinates.to_tuple(),
        )

    def set_text(self, text: str) -> None:
        """Устанавливает текст компонента"""

        self._text = text
