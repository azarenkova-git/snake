from __future__ import annotations

import pygame

from src.components import abstract_component
from src.game import game
from src.utils import colors


class TextComponent(abstract_component.AbstractComponent):
    _text: str
    _font: pygame.font.Font

    def __init__(self, game: game.Game, text: str):
        super().__init__(game)
        self._text = text
        self._font = pygame.font.SysFont("monospace", 75)

    def render(self) -> None:
        super().render()
        label = self._font.render(self._text, 1, colors.Colors.WHITE)
        self._game.get_display().blit(label, (0, 0))

    def set_text(self, text: str) -> None:
        """Устанавливает текст компонента"""

        self._text = text
